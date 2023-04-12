# Drowsiness Alert System

This is a project for creating a basic drowsiness alert system using OpenCV and Dlib. It is designed to send push notifications to users’ emails and phones by detecting a driver getting drowsy while operating a motor vehicle by analyzing their eye movement.

## Requirements
Make sure the following packages are installed:
- OpenCV
- Dlib
- Numpy
- Math
- STMP 
- Http.client
- Urllib

Steps for setting up phone notification:
1. Download Pushover application on phone app.
2. Go to: https://pushover.net
3. Create an account to obtain required API tokens


Additionally, please make sure to download dlib's pre-trained model "Shape_Predictor_68_face_landmarks" file is locally available. 
You can also download from the following link: https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat

## How to Use
1. Clone or download the project from GitHub.
2. Install the required libraries and download the shape predictor file as described in the requirements section.
3. Open the Drowsiness_alert_system.py file in a IDE or text editor.
4. In "send_alert()" function, update email and password information to send alerts to your email.
5. In "phone_Notifications()" function, please provide your app token and user token for phone alerts.
6. Run the Drowsiness_alert_system.py file. Make sure your webcam is turned on as the system will start the webcam and begin analyzing eye movements.
7. If the person's eyes are closed for over 3 seconds, notifications will be sent to the user's email and phone.
8. Press x to quit the program.

## How It Works
The drowsiness alert system works by detecting eye movements using OpenCV and Dlib. It analyzes the position of the person's eyes and determines whether 
the eyes are open or closed based on the verticle line thickness. If the thickness falls below a certain threshold, the system assumes the person's eyes
are closed, and if the thickness remains below the threshold for longer than 3 seconds, then it triggers the alarm.

## How to Contribute
If you would like to contribute, please follow these steps:

1. Fork the project on GitHub.
2. Clone the forked project to your local machine.
3. Make your changes to the code along with comments.
4. Test your changes to ensure that they work as expected.
5. Create a pull request on GitHub with your changes.

Please ensure that your pull request includes a detailed description of the changes you have made and the reasoning behind them. 

## Author 
Mithil Patel

