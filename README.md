## Hands to Words: Developing Text Conversion for Sign Language
This project aims to develop a video-based sign language recognition system that uses static hand gesture detection to translate signs into text or voice. 
By leveraging camera capture and machine learning, the system will compare user gestures with a pre-built dataset for accurate interpretation. 
It will provide real-time translation for the deaf and mute community, with additional features like voice-over for communication and emergency alerts via email or notifications. 
This solution offers a more user-friendly and effective alternative to sensor-based methods, improving accessibility in the digital world.


## About
The deaf and mute community faces challenges in digital communication due to the lack of accessible tools for real-time sign language translation. 
While human interpreters can easily understand sign language, machines require complex visual interfaces for accurate recognition. 
Current sensor-based solutions are cumbersome, highlighting the need for a more user-friendly, video-based system to translate sign language into text or voice, enabling better engagement with digital platforms.


## Features
- The system is designed to improve internet-based communication for the deaf and mute community.
- A video-based approach using static hand gesture recognition is more effective and user-friendly compared to a sensor-based approach.
- The system captures a sequence of images via camera to recognize the user's hand gestures.
- A pre-built dataset is used to compare the captured image for sign identification.
- Feature extraction focuses on the hand's position and orientation.
- Skin segmentation algorithms are utilized in this system, commonly used in computer vision applications.
- The system includes voice-over translation for the recognized signs.
- It provides alert emails and notifications for emergency signs.

## Requirements
* Operating System: Requires a 64-bit OS (Windows 10 or Ubuntu) for compatibility with deep learning frameworks.
* Development Environment: Python 3.6 or later is necessary for coding the sign language detection system.
* Deep Learning Frameworks: TensorFlow for model training, MediaPipe for hand gesture recognition.
* Image Processing Libraries: OpenCV is essential for efficient image processing and real-time hand gesture recognition.
* Version Control: Implementation of Git for collaborative development and effective code management.
* IDE: Use of VSCode as the Integrated Development Environment for coding, debugging, and version control integration.
* Additional Dependencies: Includes scikit-learn, TensorFlow (versions 2.4.1), TensorFlow GPU, OpenCV, and Mediapipe for deep learning tasks.

## System Architecture

![image](https://github.com/user-attachments/assets/93a8b849-fb23-4522-a744-ec5949873926)


## Output

#### Output1 - Hands to words
![image](https://github.com/user-attachments/assets/775184da-85bf-4bab-999c-01f3fead5f10)
![image](https://github.com/user-attachments/assets/616c5009-36c0-4a9c-a537-9a9b70962e6f)
![image](https://github.com/user-attachments/assets/e31bfca8-1e1c-4da0-83a6-6d33c9090fa1)

#### Output2 - Emergency Signals
![image](https://github.com/user-attachments/assets/d32cbbde-ff62-4df0-b5a7-8f156591d124)



Detection Accuracy: 95.9%


## Results and Impact
### 1. Accurate Sign Language Recognition: 
The system will accurately recognize and translate static hand gestures into text or voice, enabling real-time communication for the deaf and mute community.
### 2. User-Friendly Interface:
A video-based approach will simplify the process, making the system accessible and easy to use compared to sensor-based alternatives.
### 3. Emergency Alerts: 
The system will effectively send notifications and alert emails for emergency signs, enhancing safety for users.
### 4. Voice-Over Feature: 
Real-time voice-over translation will facilitate communication with non-sign language users, bridging the gap between signers and the wider community.
### 5. Broader Accessibility: 
The project will help integrate the deaf and mute community more effectively into digital platforms, promoting inclusion in a highly digitalized world. 
### 6. Enhanced Digital Inclusion: 
The system will provide greater independence and accessibility for the deaf and mute community, enabling easier participation in digital interactions.
### 7. Potential for Broader Applications: 
This technology can be expanded beyond personal communication to areas like customer service, healthcare, and education, where real-time sign language translation can be highly beneficial.
### 8. Reduction in Dependency: 
The system could reduce the reliance on human interpreters, offering an efficient and scalable solution for communication in diverse environments.


## Articles published / References
1. P. Bellot, G. de los Campos, and M. Pérez-Enciso, Can deep learning improvegenomicpredictionofcomplexhumantraits? Genetics,vol.210, no. 3, pp. 809819, Nov. 2018.
2. D. Liciotti, M. Bernardini, L. Romeo, and E. Frontoni, A sequential deep learning application for recognising human activities in smart Homes, Neurocomputing, vol. 396, pp. 501513, Jul. 2020.
3. S. Reddy, N. Srikanth, and G. S. Sharvani, Development of kid-friendly Youtube access model using deep learning, in Data Science and Security. Singapore: Springer, 2021, pp. 243250.
4. Q. Chen and V. Koltun, Photographic image synthesis with cascaded re nement networks, in Proc. IEEE Int. Conf. Comput. Vis., Oct. 2017, pp. 15111520.
5. R. Elakkiya and B. NATARAJAN, ISL-CSLTR: Indian sign language dataset for continuous sign language translation and recognition, Mendeley Data Repository, V1, 2021, doi: 10.17632/kcmpdxky7p.1.




