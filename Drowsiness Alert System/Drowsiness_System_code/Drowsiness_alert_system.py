# Importing library
import cv2
import numpy as np
import dlib
import math
import smtplib
import http.client, urllib

# Activating camera to detect a face
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
score = 0

# Calculating midpoint
def midpoint(p1,p2):
    return int((p1.x + p2.x)/2),int((p1.y + p2.y)/2)

# detecting eye landmarks and measuring vertical distance
def lankmark(points,face_landmarks):
    # drawing ver and hori line for each eye
    l_left_p = (face_landmarks.part(points[0]).x,face_landmarks.part(points[0]).y)
    l_right_p = (face_landmarks.part(points[3]).x,face_landmarks.part(points[3]).y)
    l_mid_top = (midpoint(face_landmarks.part(points[1]),face_landmarks.part(points[2])))
    l_mid_bot = (midpoint(face_landmarks.part(points[4]),face_landmarks.part(points[5])))
     
    # Drawing horizontal and verticle lines 
    hori_line = cv2.line(frame,l_left_p,l_right_p,(0,150,100),2)
    ver_line = cv2.line(frame,l_mid_top,l_mid_bot,(0,150,100),2)
        
    #checking for the distance between the line
    l_hori_len = math.sqrt((l_right_p[0]-l_left_p[0])**2 + (l_right_p[1]-l_left_p[1])**2)
    l_ver_len = math.sqrt((l_mid_top[0]-l_mid_bot[0])**2 + (l_mid_top[1]-l_mid_bot[1])**2)
    
    return l_ver_len

# setting up email alert
def send_alert():
    try:
        # Connecting to the email server to send emails
        smtp_object = smtplib.SMTP('smtp.gmail.com',587)
        smtp_object.ehlo()
        smtp_object.starttls()
        email = 'email123@gmail.com'
        password = 'password'
        smtp_object.login(email,password) # app password, not gmail password 
        
        # Formatting email and then sending it
        from_add = email
        to_add = email
        subject = 'Drowsiness Alert'
        message = 'ACTION REQUIRED! The driver is fall asleep while the vehicle is in motion. '
        msg = 'Subject: '+ subject + '\n' + message
        smtp_object.sendmail(from_add,to_add,msg)
        print('Email sent successfully ')
    except:
        print('Oops! Something went wrong.')

# Function to connect to pushover api to send push notifications to user's phone
def phone_Notifications():
    # Establishing connection to API
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    
    # Required API tokens
    app_token = 'app_token'
    user_token = 'user_token'
    
    # Connecting to API
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": app_token,
        "user": user_token,
        "title": "Drowiness Alert",
        "message": "ACTION REQUIRED! The driver is fall asleep while the vehicle is in motion."
      }), { "Content-type": "application/x-www-form-urlencoded" })
    # Fetching information 
    conn.getresponse()
    print('Successfully sent notification to your phone!')

while True:
    # ret will reture whether a camera is been used
    # return numpy array of frame
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale image
    faces = detector(gray)
    
#     print("Number of faces detected: {}".format(len(faces)))
    for i in faces:
        x1,y1 = i.left(),i.top()
        x2,y2 = i.right(),i.bottom()
#         cv2.rectangle(frame,(x1,y1),(x2,y2),(150,0,150),2)
        
        #calling the landmark file
        landmarks = predictor(gray,i)
        
        left_eye = lankmark([36,37,38,39,40,41],landmarks)
        right_eye = lankmark([42,43,44,45,46,47],landmarks)
        avg_eyeLen = (left_eye + right_eye)/2
        print(avg_eyeLen)
        if avg_eyeLen < 10:
            print('Eyes closed!')
            score += 1
            timer = score/5.3
            
            # If eyes are closed for longer than 3 seconds, send email alert and phone notification
            if round(timer,1) == 3.0:
                print("Alarm triggered!\n")
                send_alert()
                phone_Notifications()
            
            # Display eyes status and timer on the screen
            cv2.putText(frame,f'timer:{timer:2f}',(100,650),cv2.FONT_HERSHEY_TRIPLEX,2,(100, 150, 20),3)
            cv2.putText(frame,'Closed',(100,700),cv2.FONT_HERSHEY_TRIPLEX,2,(255, 0, 0),3)
        else:
            # Display eyes status and timer on the screen
            score,timer = 0,0
            cv2.putText(frame,f'timer:{timer:2f}',(100,650),cv2.FONT_HERSHEY_TRIPLEX,2,(100, 150, 20),3)
            cv2.putText(frame,'Open',(100,700),cv2.FONT_HERSHEY_TRIPLEX,2,(0, 0, 255),3)
        
    # display face
    cv2.imshow('frame',frame)
    
    # key required to end the loop
    if cv2.waitKey(1) == ord('x'):
        break
        
cap.release()
cv2.destroyAllWindows()