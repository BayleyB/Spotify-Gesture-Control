import mediapipe as mp
import spotify_functions as sf
import cv2
import math
import time

font = cv2.FONT_HERSHEY_COMPLEX

def start_capture():
    mp_hand_drawing = mp.solutions.drawing_utils #Helps with drawing hand landmarks
    mp_hands = mp.solutions.hands

    mediaCap = cv2.VideoCapture(0) #Set capture feed for webcam

    max_distance = -1 #Used for volume control
    play_pause_active = False #Used to avoid repeated play/pause actions
    next_prev_active = False #Used to avoid repeated next/prev song actions

    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: #defining hand tracking as hands within the loop
        while mediaCap.isOpened():
            _, frame = mediaCap.read() #Capture frame from webcam

            #Grab frame from camera and process it preforming hand detection
            image = cv2.flip(frame, 1)
            detection = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            image_height, image_width, _ = image.shape

            #List of finger tip landmarks for all fingers except the thumb
            finger_tip_ids = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, 
                            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]

            #Used to keep track of # of fingers up on each hand
            finger_count = {'LEFT': 0, 'RIGHT': 0}

            #Dictionary that will be used to detect if a finger is up or down in a captured frame, False will indicated finger is down, True will indicate it is up
            finger_up = {'RIGHT_THUMB': False, 'RIGHT_INDEX': False, 'RIGHT_MIDDLE': False, 'RIGHT_RING': False, 'RIGHT_PINKY': False,
                        'LEFT_THUMB': False, 'LEFT_INDEX': False, 'LEFT_MIDDLE': False, 'LEFT_RING': False, 'LEFT_PINKY': False}

            #If a hand was detected withing the captured frame, we want to draw it
            if detection.multi_hand_landmarks:
                for hand_index, hand in enumerate(detection.multi_handedness):
                    
                    #Label the hand as left or right
                    hand_lr = hand.classification[0].label

                    #Find the landmarks on the hand
                    hand_landmarks = detection.multi_hand_landmarks[hand_index]

                    #Loop throught the finger tip indexes
                    for tip_index in finger_tip_ids:
                        finger_name = tip_index.name.split("_")[0] #Figure out which finger we are looking at first

                        #If the finger tip is higher than the midpoint, update the value to true in the dictionary
                        if (hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index-2].y):
                            finger_up[hand_lr.upper()+"_"+finger_name] = True
                            finger_count[hand_lr.upper()] += 1

                    #Get coordinates of thumb tip
                    thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width
                    thumb_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height
                    thumb_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x

                    #Get coordinates of index finger tip
                    index_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width
                    index_tip_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height

                    #If the thumb is up, then set its value in the dictionary to true
                    if (hand_lr=='Right' and (thumb_tip_x < thumb_mcp_x)) or (hand_lr=='Left' and (thumb_tip_x > thumb_mcp_x)):
                        finger_up[hand_lr.upper() + "_THUMB"] = True
                        finger_count[hand_lr.upper()] += 1

                    #Calculate the distance between the thumb and index tip
                    thumb_index_distance = math.sqrt(((index_tip_x - thumb_tip_x)**2) + ((index_tip_y - thumb_tip_y)**2))
                    
                    #Determines if the user is in volume control mode which is gesture activated
                    volume_control_enabled = not(finger_up[hand_lr.upper() + '_MIDDLE']) and not(finger_up[hand_lr.upper() + '_RING']) and not(finger_up[hand_lr.upper() + '_PINKY'])

                    #Results in true if the user is giving the play pause gesture
                    play_pause_gesture = finger_up[hand_lr.upper() + '_INDEX'] and finger_up[hand_lr.upper() + '_MIDDLE'] and finger_count[hand_lr.upper()] == 2

                    next_song_gestrue = finger_up[hand_lr.upper() + '_INDEX'] and finger_up[hand_lr.upper() + '_PINKY'] and finger_count[hand_lr.upper()] == 2
                    previous_song_gesture = finger_up[hand_lr.upper() + '_PINKY'] and finger_count[hand_lr.upper()] == 1

                    if (volume_control_enabled):
                        #Reinitializes max distance to the current thumb/index distance which must be done every time gesture is activated
                        if(max_distance == -1):
                            max_distance = thumb_index_distance

                        #If the distance converted to a percentage is > than 100 it just sets it to 100 to avoid crashing
                        vol_percent = int (thumb_index_distance * 100 / max_distance)
                        if(vol_percent > 100): vol_percent = 100

                        #Used to control volume when volume control mode is enabled 
                        sf.adjust_volume(vol_percent)
                        
                        #Volume control UI
                        cv2.putText(image, "Max: " + str(max_distance), (25, 25), font, 1, (0, 0, 255), 2)
                        cv2.putText(image, "Current: " + str(thumb_index_distance), (25, 75), font, 1, (0, 0, 255), 2)
                        cv2.putText(image, "Percent: " + str(vol_percent) + "%", (25, 125), font, 1, (0, 0, 255), 2)
                        cv2.line(image, (int(thumb_tip_x), int(thumb_tip_y)), (int(index_tip_x), int(index_tip_y)), (0, 0, 255), 3)
                    else:
                        max_distance = -1
                    
                    #Checks to see if the play/pause gesture is still active to avoide repeated play/pause function calls
                    if(play_pause_gesture and (not play_pause_active)):
                        play_pause_active = True
                        sf.play_pause()
                        time.sleep(1)
                    elif((not play_pause_gesture) and play_pause_active):
                        play_pause_active = False

                    #If the next/prev gesture is active it will not preform the action to avoid repeated next/prev function calls
                    if(next_song_gestrue and (not next_prev_active)):
                        next_prev_active = True
                        sf.next_song()
                        time.sleep(1)
                    elif(previous_song_gesture and (not next_prev_active)):
                        next_prev_active = True
                        sf.prev_song()
                        time.sleep(1)
                    elif((not next_song_gestrue) and (not previous_song_gesture) and next_prev_active):
                        next_prev_active = False

                    #Draw hand landmarks onto processed frame
                    mp_hand_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS, mp_hand_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2))            

            cv2.imshow('Spotify View', image)

            #Pressing q will break from the loop and close out the window
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    mediaCap.release()
    cv2.destroyAllWindows()
    return