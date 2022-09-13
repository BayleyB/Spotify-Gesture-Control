# README for Spotify-Gesture-Control

Last Updated: 9/13/2022

## Basic Description:

This program utilizes MediaPipe's machine learning API paired with OpenCV's computer vision library to recognize hand gestures that can be used to perform music control for Spotify. To enable playback control I leveraged Spotipy's Python library for the Spotify Web API which makes using it very intuitive.

## Files:

The following is a list of files in the project folder and a description of them.

### Code Files:
- main.py: This is the main code file for the program, it will trigger user authentication by grabbing the current user's username as well as starting the video capture for gesture recognition.
- gesture_recognition.py: This file contains all of the logic for recognizing the users gestures as well as making calls to the funtions in the spotify_functions.py file.
- spotify_functions.py: This is the file that directly interacts with the Spotify Web API by using functions built in to the Spotipy Python library.

### Extra Files:
- README.md: Contains program description, file description, setup, usage, and information referenced in the creation of this program.

## Setup:
- Install spotipy, mediapipe, and cv2 packages.
- Create a Spotify developer account and create a new application on your developer dashboard.
- Paste the Client ID and Client Secret of your newly created application into the spotify_functions.py file.
- Run main.py to start the program.
    - Note: The first time the program is ran it will require the user to authorize the program to have access to various aspects of their Spotify account.

## Preforming Gesture Controls:
### Play/Pause
![Imgur](https://i.imgur.com/tBqLWlq.png)
The user can play/pause music playback by holding up their index and middle finger at the same time. The program will determine the correct action to perform based on the current playback status. This action is also protected from repeated inputs if the gesture is held, so if the user would like to perform the action again they must put their hand back to a neutral postion and perform the gesture again.

### Next Song
![Imgur](https://i.imgur.com/mOtG1Vu.png)
The user can skip to the next song in the queue by holding up their index finger and pinky at the same time. This action also is protected from repeated inputs.

### Previous Song
![Imgur](https://i.imgur.com/YsVIbQD.png)
The user can go back to the previous song by holding up just their pinky. Just as the previous two actions this one is also protected from repeated inputs.

### Volume Control
![Imgur](https://i.imgur.com/EM6OA5Z.png)
The user can enter playback volume control mode by holding up their index and thumb only. Then the program calculates the distance between the users thumb and index finger, setting that to the maximum volume value possible. I would have liked to initialize that distance to the current playback volume but unfortunatly the Spotify API does not allow you grab the current playback volume percentage. By moving their index/thumb closer and further apart, the user can then adjust the playback volume of the music.

## References:

The following sources were referenced in the creation of this program. A short description of why they were referenced is below each source.

### [MediaPipe Hands Docs](https://google.github.io/mediapipe/solutions/hands.html)

This is the docs for MediaPipe's hand recognition solution used in the creation of this program. This API has the ability to recognize the position of various different landmarks on the users hand which I utilized in recognizing hand gestures that then are used to control music playback.

### [AI Hand Pose Estimation](https://www.youtube.com/watch?v=vQZ4IvB07ec)

I referenced this video when learning about MediaPipe's hand solution and OpenCV which led to a basic gesture recognition algorithm, that uses the positions of various hand lankmarks in a frame to estimate which hand gesture the user is attempting to show.

### [Real-Time Fingers Counter & Hand Gesture Recognizer](https://www.youtube.com/watch?v=epwlqHHbELE)

I referenced this video as well in creating a more advanced algorithm to more accurately recognize the described gestures above that are used for playback control.

### [Spotipy Docs](https://spotipy.readthedocs.io/en/2.19.0/)

This is the docs for the Spotipy python library that utilizes the Spotify web API. This was referenced to understand how to create an authorization token which gives access to certain aspects of a users Spotify account and what functions are made availiable to the developer.

### [Spotify API Authorization Scopes](https://developer.spotify.com/documentation/general/guides/authorization/scopes/#playlist-modify-private)

This was referenced to understand the Spotify authorization scopes that were needed to properly implement this program.