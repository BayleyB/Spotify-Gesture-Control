import gesture_recognition as gr
import spotify_functions as sf

#Grabs username to trigger account authentication
username = sf.get_user()
print("Starting gesture control for user: ", username)

#Starts gesture capturing
gr.start_capture()