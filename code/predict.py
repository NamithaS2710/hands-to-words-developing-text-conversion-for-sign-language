import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import os
import xlrd
import cv2
import coll
import mediapipe as mp
import numpy as np
from playsound import playsound
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
import time
########Initialise random forest

s.starttls()
s.login("abninfotechcse01@gmail.com", "jvqocjwjrcpfzfkh")
message = "EMERGENCY"
local_path = (os.path.dirname(os.path.realpath('__file__')))

file_name = ('data1.csv')#file of total data
data_path = os.path.join(local_path,file_name)
print (data_path)
df = pd.read_csv(r''+data_path)

print (df)

units_in_data = 28 #no. of units in data

titles = []
for i in range(units_in_data):
    titles.append("unit-"+str(i))
X = df[titles]
y = df['letter']


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.5,random_state=2)
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
clf = RandomForestClassifier(n_estimators=30)#random forest
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
cmrf=confusion_matrix(y_test, y_pred)
print("1.Random Forest Accuracy")

print("Random Forest classification_report")
print(classification_report(y_pred, y_test, labels=None))
print("Random Forest confusion_matrix")

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("CONFUSION MATRIX OF RF")
print(cm)
tpr = float(cm[0][0])/np.sum(cm[0])
fpr = float(cm[1][1])/np.sum(cm[1])
plt.figure(figsize=(12, 12))
sns.heatmap(cm, annot=True, fmt=".0f", linewidths=.5, square = True, cmap = 'Blues');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Confusion Matrix of RF '
plt.title(all_sample_title, size = 15);
plt.show()

#########Begin predictions
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def get_prediction(image):
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        ImageData = coll.ImageToDistanceData(image, hands)
        DistanceData = ImageData['Distance-Data']
        image = ImageData['image']
        prediction = clf.predict([DistanceData])
        return prediction[0]


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    SpelledWord = ""
    while cap.isOpened():
            success, image = cap.read()
            if not success:
                        print("Ignoring empty camera frame.")
                        # If loading a video, use 'break' instead of 'continue'.
                        continue

            '''ImageData = HandDataCollecter.ImageToDistanceData(image, hands)
            DistanceData = ImageData['Distance-Data']
            image = ImageData['image']

            if cv2.waitKey(1) & 0xFF == 32:
                prediction = clf.predict([DistanceData])
                SpelledWord = str(prediction[0])
                #print(SpelledWord)'''

            try:
                SpelledWord = get_prediction(image)
                print(SpelledWord)
                if SpelledWord == "HAVE A GREAT DAY!":
                    print("yes")
                    # time.sleep(4)
                    
                elif SpelledWord == "EMERGENCY":
                    print("yes")
                    s.sendmail("abninfotechcse01@gmail.com", "abninfotechprojects@gmail.com", message)
                    playsound('3.wav')
                    # time.sleep(4)
                    
                elif SpelledWord == "A CUP OF COFFEE?":    
                    print("yes")
                    # time.sleep(4)
                    
                elif SpelledWord == "HAVE A BREAKFAST!":
                    print("yes")
                    # time.sleep(4)
                elif SpelledWord == "GOOD NIGHT! SLEEP WEEL.":
                    print("yes")
                    # time.sleep(4)
                    
                elif SpelledWord == "HOW ARE YOU?.":
                    print("yes")
                    # time.sleep(4)
                    
                else:
                    print("no_detection")
                    


                #cv2.putText(image,  SpelledWord, (50,50), 1, 2, 255)
                cv2.putText(image,SpelledWord,(50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (124,252,0), 5, cv2.LINE_AA)
                time.sleep(10)
            except:
                pass



 