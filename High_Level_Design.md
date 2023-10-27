# Full System Overview
## Module: gesture_recognition.py
- **Module Name**: gesture_recognition.py

- **Primary Objectives**: This module is designed to recognize hand gestures and use them to control a Spotify client. The hand gestures can control volume, play/pause, and next/previous song.

- **Critical Functions**: 
    - `start_capture()`: This is the main function that starts capturing video from the webcam, detects hand gestures, and performs corresponding Spotify actions.
    - `adjust_volume(vol_percent)`, `play_pause()`, `next_song()`, `prev_song()` from `spotify_functions` module: These functions are used to control the Spotify client based on the detected hand gestures.

- **Key Variables**: 
    - `mp_hand_drawing`, `mp_hands`: Used for hand recognition and drawing.
    - `mediaCap`: Captures video from the webcam.
    - `max_distance`: Used for volume control.
    - `play_pause_active`, `next_prev_active`: Used to avoid repeated play/pause and next/prev actions.
    - `finger_tip_ids`: Contains the ids of finger tips for gesture recognition.
    - `finger_count`, `finger_up`: Used to track the number of fingers up and their positions.

- **Interdependencies**: This module depends on the `mediapipe` module for hand recognition, `cv2` for video capture and image processing, and `spotify_functions` for controlling the Spotify client.

- **Core vs. Auxiliary Operations**: The core operations of this module are the hand gesture recognition and the corresponding Spotify actions. The auxiliary operations include video capturing, image processing, and UI display.

- **Operational Sequence**: The module first starts video capture, then it enters a loop where it continuously reads frames from the video, detects hand gestures in each frame, and performs corresponding Spotify actions based on the detected gestures.

- **Performance Aspects**: The performance of this module largely depends on the accuracy of hand recognition and the responsiveness of the Spotify client. Also, the video capture and image processing should be fast enough to provide a smooth user experience.

- **Reusability**: This module is quite specific to its task of controlling Spotify with hand gestures. However, the hand gesture recognition part can be reused for other applications that require hand gesture inputs. The Spotify control part can also be reused for other applications that need to control a Spotify client.
## Module: main.py
- **Module Name**: main.py

- **Primary Objectives**: This module is designed to implement gesture-based controls for a Spotify account. It uses a gesture recognition system to capture user gestures and translate them into commands for a Spotify account.

- **Critical Functions**:
  - `sf.get_user()`: This function is used to retrieve the username and trigger account authentication.
  - `gr.start_capture()`: This function starts the gesture capturing process.

- **Key Variables**: 
  - `username`: This variable holds the username obtained from the `sf.get_user()` function.

- **Interdependencies**: 
  - This module heavily depends on two other modules: `gesture_recognition` and `spotify_functions`. The `gesture_recognition` module is presumably responsible for the actual capturing and interpretation of user gestures, while the `spotify_functions` module likely contains functions for interacting with a Spotify account.

- **Core vs. Auxiliary Operations**: 
  - The core operation of this module is the gesture capturing process, started by `gr.start_capture()`. 
  - The auxiliary operation is the retrieval of the username and triggering of account authentication, done by `sf.get_user()`.

- **Operational Sequence**: 
  - First, the module imports the necessary other modules (`gesture_recognition` and `spotify_functions`). 
  - Then, it retrieves the username and triggers account authentication. 
  - Finally, it starts the gesture capturing process.

- **Performance Aspects**: 
  - Performance considerations are not explicitly mentioned in the provided code. However, the efficiency of the gesture recognition process and the responsiveness of the Spotify account to the commands sent could be significant performance considerations.

- **Reusability**: 
  - The `sf.get_user()` and `gr.start_capture()` functions seem to be reusable for any user who wants to control their Spotify account with gestures. However, this depends on the implementation details of these functions, which are not provided in the code snippet.
## Module: spotify_functions.py
- **Module Name**: The module name is "spotify_functions.py".

- **Primary Objectives**: The primary purpose of this module is to interact with the Spotify API to control the user's Spotify account. This includes getting the user's Spotify username, adjusting the volume, controlling the playback (play/pause), and navigating through songs (next/previous).

- **Critical Functions**: 
    - `get_user()`: Gets the current user's Spotify username.
    - `adjust_volume(vol_percent)`: Adjusts the volume to a given percentage (0-100).
    - `play_pause()`: Checks if music is playing and either plays or pauses it based on the current status.
    - `next_song()`: Skips to the next song in the queue.
    - `prev_song()`: Goes back to the previous song.

- **Key Variables**: 
    - `SPOTIPY_CLIENT_ID`: The client ID for the Spotify API.
    - `SPOTIPY_CLIENT_SECRET`: The client secret for the Spotify API.
    - `SPOTIPY_REDIRECT_URI`: The redirect URI for the Spotify API.
    - `scope`: The scope defines the level of access the application has to the user's Spotify account.
    - `sp`: An instance of the Spotipy class, which is used to interact with the Spotify API.

- **Interdependencies**: This module depends on the `spotipy` library and its `SpotifyOAuth` module to interact with the Spotify API.

- **Core vs. Auxiliary Operations**: Core operations include getting the user's Spotify username, controlling the playback, and navigating through songs. The auxiliary operation is adjusting the volume.

- **Operational Sequence**: The Spotipy object is first created with the necessary authentication details. Then, the various functions can be called as needed, such as getting the user's information, controlling playback, or adjusting the volume.

- **Performance Aspects**: The performance of this module largely depends on the responsiveness of the Spotify API. Since it involves making network requests, delays might occur if the network connection is slow or unstable.

- **Reusability**: The module is highly reusable. The functions are generic enough to be used in any application that needs to control a Spotify account. The authentication details would need to be replaced with the details for the account that is to be controlled.


## Flow Map (py)

![Flow Map (py)](flow_map_py.png)



## System Summary

This is a flowchart of a program with three main modules: `main`, `gesture_recognition`, and `spotify_functions`. 

The program starts with the `main` module, which calls two functions: `start_capture()` from the `gesture_recognition` module and `get_user()` from the `spotify_functions` module.

The `get_user()` function in the `spotify_functions` module is a leaf function, meaning it doesn't call any other functions. 

The `start_capture()` function in the `gesture_recognition` module, on the other hand, calls four other functions, all of which are also in the `spotify_functions` module. These functions are `adjust_volume()`, `next_song()`, `play_pause()`, and `prev_song()`. All of these are leaf functions as well, meaning they don't call any other functions.

In conclusion, the `main` module starts the program, calls the `gesture_recognition` module to start capturing gestures, and the `spotify_functions` module to get the user and perform various Spotify-related functions based on the captured gestures.
