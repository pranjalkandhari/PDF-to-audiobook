import sys
#from english_words import english_words_alpha_set
import random
from fpdf import FPDF

import sys
import io

#Files for PDF Miner:
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

#Files for PDF OCR reader:
import fitz
from PIL import Image
import pytesseract
from pytesseract import image_to_string

#Making Image from PDF:
from pdf2image import convert_from_path

#Files for test to speech:
from gtts import gTTS

#For calculating time:
import time

#Changing the standard input to input.txt to get real string
sys.stdin = open('input.txt', 'r')

def lcs(X , Y): 
    m = len(X)
    n = len(Y)  
    L = [[None]*(n+1) for i in range(m+1)] 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n] 

def extractPDFText(pdfFilePath): #Returns text in the pdf
    with open(pdfFilePath , 'rb') as fh:
        completeText = ""
        for page in PDFPage.get_pages(fh , caching = True , check_extractable = True):
            resourceManager = PDFResourceManager()
            fakeFileHandle = io.StringIO()

            converter = TextConverter(resourceManager , fakeFileHandle)

            pageInterpreter = PDFPageInterpreter(resourceManager , converter)

            pageInterpreter.process_page(page)

            text = fakeFileHandle.getvalue()

            completeText += text
            completeText += " "

            converter.close()
            fakeFileHandle.close()

        return completeText

def extractPDFusingOCR(pdfFilePath , maxLimitOfPages = 100): #Returns text in the images of the pdf
    completeText = ""
    images = convert_from_path(pdfFilePath)
    for img in images:
        completeText += image_to_string(img,lang="eng")

    return completeText


okStr = '''

Smart Trafﬁc Light Management System For Emergency Vehicle
Nitin Vohra1[0000-0002-6952-0763], Pranjal Kandhari2[0000-0001-9065-737X], Abhinav Gupta3[0000-0002-4707-0108], Shilpa Gupta4[0000-0002-5243-659X], Arpit Shrotiya5[0000-0003-0918-8989] and Rohit Dev6[0000-0002-2228-0184]
1-6 Bharati Vidyapeeth’s College Of Engineering, New Delhi1nitinvohra92@gmail.com
2pranjalkandhari@gmail.com
3abhinavgupt99@gmail.com
4shilpa.gupta@bharatividyapeeth.edu
5arpit.shrotriya5945@gmail.com
6rohitdevs.kmh2@gmail.com
Abstract. As of right now, there are uncountable individuals ranging from adolescents to elderly irrespective of being adhering to a single age-group who become victims of heinous road accidents in India. Giving the claim a more profound relevance, as economic times have mentioned, close to 1,51,417 individuals were killed in road accidents. Out of which, 69.6 percent of deaths were caused due to road rage and then due to delay in the arrival of an ambulance to the scene. Of course, a lot of factors play a major role in the circumstances. Our proposed system stresses the time delays caused by redundant, inefﬁcient trafﬁc jams to rectify this problem and improves it with deﬁned logical methods which would be constructively helpful for the society as a whole. The most effective route to the accident is calculated and displayed and then a combined array of servers with a central controller determines the location of the ambulance and changes the trafﬁc lights adaptive to shorten the time-delay for the victim as minuscule as possible, with less to none human interference. The implementation of the proposed system is done with keeping the safety of emergency vehicles in mind, giving them a better course of action to follow.
Keywords: Emergency Vehicle, CCTV cameras, Trafﬁc Junction
Introduction
Vehicle safety at crossroads has been a problem for governments in many major cities around the world to address for too long we cannot even imagine. India is a developing country with a second-largest population in the whole world. Despite being an incredibly fast-growing economy. The country is severely affected by road congestion caused by vehicle overcrowding and slow infrastructure development in space allocated and adhering cost. Which further results in causing hindrance in the systematic execution of norms and services. Many different, innovative systems have been proposed but still, older timing circuits are used by today’s systems to reﬂect the responses in an orderly fashion. But, the current systems don’t account for different test cases experienced in emergencies resulting in loss of valuable time. In most of today’s scenarios, the ambulances are caught up in the trafﬁc jams en route to a near-death victim. As congestion often results in wastage of time and productivity. Driving to the accident scene in a safe manner and quickly is a major challenge for emergency vehicles, particularly as trafﬁc is increasingly heavy and trafﬁc patterns in modern cities have become more complex. So making both an effective and adaptive system is a task bigger than we can perceive. Thus, the Smart Trafﬁc Light Management System takes the computer vision as well as Internet of Things (IoT) approach to further implement that by switching trafﬁc lights for emergency vehicles, mainly ambulance on the designated shortest path which is regulated through a nexus of servers and maintaining personnel approach through a custom application to facilitate the proper functioning and creating an effortless experience for patient recovery by the respective vehicles saving many innocent lives in the process. Further, the system can be deployed further for a plethora of emergency vehicles to further regulating the trafﬁc for our country. Thus, making a better solution altogether.
Literature Survey
Increasing Traffic problems is a huge concern in cities nowadays. Growing population results in the number of vehicles being increased in cities [1]. This results in congestion on roads which increases the traveling time. [2] Ayush K.R. Mittal, et. al, have discussed the Green Wave system, which basically turns all the red lights into green lights thereby granting permission to emergency vehicles. The green wave system has a drawback that on being suddenly changed due to the alteration of green wave traffic problems can be caused. This leads to the increase in the vehicles in the queue of a green wave which leads to vehicles not being able to reach the green light in time and once the wave is disturbed, its disturbance can cause a major increase in traffic problems. In these situations, a green wave will grow until the line of vehicles becomes too big hence stopping vehicles to reach the green light. This is called as over-saturation [3-5]. [6] Q. Zang, et. al, studied the utilization and implementation of RFID in VANETs. In the proposed mechanism RFID is embedded in each vehicle to identify the vehicles with the help of computers till the time the tag is present within the vehicle. Its limitation is it can cover and detect within a brief distance only. [7] Rashmi Hegde, et. al., an ambulance system was proposed an automatic route clearance using RFID and GPS- based system. The disadvantage of this system is that it wouldn’t work for the ambulance if the starting point and the endpoint of the trip are not known in advance. [8] Chang Guo, et,. al inspected some factors related to traffic and proposed a mechanism based on a distributed transportation system. In it, a method was proposed to calculate the speed from source to destination. This method will only show the alternative routes or the shortest routes but not the area with traffic congestion. [9] N.B. Soni, et., al, studied numerous technologies and sensors for reducing traffic congestion across the country. The study examined the Ultrasonic sensors, Adaptive Traffic Control System (ATCS) and Inductive Loop Detectors (ILD). The technique proposed leads to an increase in traffic on the streets. [10] Sarika B.Kale, et., al, has proposed a smart ambulance that consists of Temperature sensor and Heart Beat sensor. The big disadvantage of this is that all ambulances must have more special instruments other than the medical ones. [11] Aman Dubey, et., al, proposed an image processing technique that uses Micro-controller which is installed on the traffic light along with the 4 cameras that are installed on it. The technique uses Open-CV as a tool for implementation. Which leads to the decline in private detection range and quality. Thus it needs to be trained accurately.    [12] J. Naga Harsha, et., al, studied the Density-based Traffic System by using a Microwave/Millimeter-wave radio detection, ranging and Magnetic Detector (Magnetometer). This technology has varied problems like false detection because of multi-path propagation and magnetic detectors will have to be compelled to be embedded in the pavement which might need multiple detectors to notice smaller vehicles. [13] Anna Merine George, et., al, used the Adaptive Neuro-Fuzzy Inference System (ANFIS) to improve traffic conditions. This study has some disadvantages since it’s a simulation-based technique and it cannot be embedded on a real-time basis, where the simulation sometimes occurs as statistics, probability, and overview of what’s happening in the computer model. [14] Anthony Theodore, et al., proposed a system using simulation which has the capability to simulate real-time traffic flow using CDS. The limitation of the model is that it is created only by considering the area of Minneapolis, MN. [15] W. Wen proposed an expert system using six simulation models for solving the problem of road congestion. The results of the proposed solution proved to be efficient as they observed a sharp drop in average waiting time at traffic signals. [16] S. Sharma, et al., proposed the solution by giving priority to the emergency vehicle using RFID. The limitation of this work that the communication between the controller and the emergency vehicle is not discussed. [17] Karthikeyan offered a solution for detecting emergency vehicles using a ZigBee receiver.
Proposed Model

Fig. 1. Flow diagram of proposed model-1        Fig. 2. Flow diagram of proposed model-2
The proposed model of the Trafﬁc Management System provides a solution to solve the problem of trafﬁc management at the trafﬁc signals to give priority to emergency vehicles so that to save time in the absence of some supervision. It will be done by triggering an alert by the system to turn the trafﬁc lights green when the emergency vehicle is in the range of trafﬁc signals and triggering it back to normal when the emergency vehicle crosses the junction. This system act as a medium to provide communication between various Internet of Things (IoT) devices and emergency vehicles.
Proposed System-1
This proposed system detects emergency vehicles using CCTV cameras that are placed near the traffic signal. On detection, it triggers the traffic signal and brings the traffic signal lights back to normal scheduling once the emergency vehicle passes the crossing. 
Here, two processes are involved:
     
     Fig. 3. Ambulance detection using Open CV           Fig. 4. R-CNN Architecture
a) Emergency Vehicle detection using CCTV cameras.
 This module will be responsible for the detection of ambulances using CCTV cameras which are placed near the trafﬁc signal. When an emergency vehicle comes in the range of the CCTV camera, then by using R-CNN we will detect the ambulance. We have detected an ambulance using R-CNN, or Region-based Convolutional Neural Network, which consists of 3 steps: 
1) The input image is scanned for all the possible objects using selective search, generating more than a thousand region proposals. 
2) After that, we ran a convolutional neural net (CNN) on top of every region proposals found in step 1. 
3) In the last step, the output of each CNN is of feeding it into:
a)  A Support-Vector Machine (SVM) to classify the region.
b) Into a module to tighten the bounding box of the object using linear regression if such an object exists. So, in simple terms, we ﬁrst proposed the regions, then extracted features from them, and then classiﬁed those regions based on the features extracted. R-CNN is very intuitive but very slow so to cover up this limitation we have used Faster R-CNN that resembled the original R-CNN in many ways but has overcome the limitation of its detection speed through two main augmentations: 
i) Feature extraction is performed over the image and after the regions are proposed, thus only running one CNN over the entire image instead of a thousand CNN’s over a thousand overlapping regions.
ii) The neural network is extended for predictions instead of creating a new model by replacing the SVM with a softmax layer.

b) Trafﬁc signal triggering after the detection of the emergency vehicle 
When the ambulance is detected in the CCTV camera placed near the trafﬁc signals then our central server will send a triggering signal to the microcontroller which is attached to the trafﬁc signals which will then help in switching trafﬁc signals. The trafﬁc signal triggering module is responsible for changing the trafﬁc signals. The function which will help in triggering the trafﬁc signal will take real-time data captured by the CCTV camera as the input and will send a trigger signal as an output to the microcontroller. When the triggering signal is received to the microcontroller then it will override the trafﬁc signal and switch it to green for making away so that an emergency vehicle can proceed easily. Once an emergency vehicle is no longer visible in the CCTV camera then the microcontroller turns the trafﬁc signal to its conventional mode after a predeﬁned constant time-lapse.
Proposed System-2
This proposed system provides a real-time location of the emergency vehicle to the centralized server which manages triggering of signals to the trafﬁc signals. The ambulance the driver will constantly use GPS to send its real-time location to the central server (this will be done using the GPS module of the driver’s smartphone). Our central server will constantly map the coordinates received from the driver and the coordinates of trafﬁc signals already stored in our database. Once when the distance between the trafﬁc light and the ambulance crosses a threshold then the central system will trigger a signal to change the signal to green if it is red. This mechanism will help to clear the path of the emergency vehicle at trafﬁc signals at peak time or at junctions where the problem of congestion is very common. The basic activity ﬂow diagram of the system is shown in Fig. 2. Our system is divided into four modules:
    •   Registration and Authentication of the Emergency Vehicle Driver
Each emergency vehicle driver must be behaving a smartphone with a properly working GPS module and the provided mobile application installed in it. Also, it is worth noting that the system tracks the locations of the driver and not the emergency vehicle. The major beneﬁt of this is cost-effectiveness as no new GPS module has to be implemented in an emergency vehicle. Therefore, saving the cost of the numerous modules implemented and their recurring maintenance cost. Another aspect of this solution involves concerns regarding taking undue advantage of this system by the drivers and using it for personal use (as the trafﬁc light system is being affected by the driver’s location). To resolve this issue we give an option to the driver to be ofﬂine while not driving the emergency vehicle and also we can monitor whether the driver is using the application when not on duty and hence necessary action can be taken against the driver. Another feature that can be added is to connect the driver’s attendance database to our system. This will help in the easy attendance of the driver and also managing their working hours. After the Authentication is done the driver can access the app using their email ID which can also act as a unique ID for our database. 
                         
Fig. 5. Login page of App    Fig. 6. Live location of Emergency Vehicle      

    •   Detecting the location of the emergency vehicle
The location of the driver is based on the location of the app of the driver’s smartphone location. We receive the location of the driver’s application on a real-time database (for example ﬁrebase). We receive the location of the driver in the form of latitude and longitude coordinates. Additionally, to improve the efﬁciency of our system we can also receive the trafﬁc density of the location where the emergency vehicle is present using Google Maps Application Program Interface (API) (explained in C). Another feature that is included is to show the shortest route to the driver to reach the hospital. Here one point is worth noting, this system largely depends on the accuracy of the location received by the smartphone application. Hence, a good internet connection and a properly functional GPS module is a must for the working of this system. 
               
  Fig. 7. Traffic light intersection               Fig. 8. Optimized path according to traffic      
    •   Algorithm to schedule trafﬁc signals in accordance with the Emergency vehicle.
 The central system (this processing will take place on a cloud-based server) will constantly monitor the real-time location of the vehicle and will be constantly mapping it with the coordinates of the trafﬁc signals. Once an emergency vehicle comes in the vicinity of a trafﬁc light (after crossing a threshold value) we turn the trafﬁc light to green for a speciﬁc amount of time. The upper limit to the time has to be speciﬁed as in case of heavy trafﬁc, the emergency vehicle might take too long to pass the trafﬁc signal and hence causing trafﬁc blockage on other sides of the crossing. Now we cannot simply turn on the green signal by taking vicinity as a parameter even if the emergency vehicle is moving away from the trafﬁc light. So to handle this case we also need to store some previous location on the emergency vehicle in order to interpret the direction on the emergency vehicle. We will turn the nearest trafﬁc light to green as shown in Fig.8. Also, we can use the same directional approach to ﬁnd if the ambulance has passed the crossing. Once we detect it, we can put the trafﬁc light back to its normal schedule. Another noticeable point is that the threshold value will change on different trafﬁc conditions which can be handled by the following approach:
    Threshold distance = x*c    (1)
In the above equation, x is the variable and c is a constant Trafﬁc intensity can be categorized into three levels (which will be provided by Google Maps API): High, medium, and low respectively. In the case of multiple emergency vehicles, we can prioritize them accordingly: 
    •   Advanced Life Support Ambulance (Max priority) 
    •    Basic Life support Ambulance 
    •    Patient transfer Ambulance 
Also, if multiple ambulances of the same priority come in the vicinity of trafﬁc lights of the same crossing then the priority will be given to the ambulance with the shortest distance from the crossing. 
    •   Triggering Mechanism after the trafﬁc signal is scheduled according to the ambulance. 
When the vehicle crosses a deﬁned stretch the central server relays a trigger signal to the respective micro-controller which is attached to the trafﬁc signals which will help in switching trafﬁc signals. The trafﬁc signal triggering module is bonded for switching the signal conferring with the deﬁned stretch, calculated using the trafﬁc intensity and the live location of the ambulance at that moment of time. The function which will help in triggering the trafﬁc signal will take trafﬁc intensity and the live location of the ambulance as input and will send a trigger signal as an output to the micro-controller according to the threshold distance calculated. When the triggering signal is received by the micro-controller then it will override the trafﬁc signal and switch it to green for making away so that an emergency vehicle can proceed easily. On the passing of the vehicle across the trafﬁc light and upon crossing a deﬁnite stretch after which the micro-controller turns the trafﬁc signal back to its previous case.
 Comparison Between the two proposed Solutions :
Table 1. Comparison between two proposed solutions
Features
Using CCTV Camera
Using smartphone GPS
Average Waiting Time
Low, the traffic light is turned green when the EV is detected by CCTV but due to the lower range the system does not work on large traffic jams or when line of sight is blocked.
Lower, the traffic light is turned green when the EV crosses the variable threshold distance which can vary according to the traffic intensity at that moment of time.
Range
Less, since the detection is dependent on the camera quality and angle.
More, since it can vary according to traffic intensity at that moment of time.
Dependencies
Range and camera angle.
Human error and GPS. 
Efficiency
Good because it will help EV to pass traffic signal but can fail where traffic intensity is more or line of sight is obstructed.
Better as it will help EV to pass and have a variable threshold distance which can vary real-time according to traffic intensity.
Scheduling as per the priority of emergency
No
Yes, we can prioritize according to type of ambulance.
Conclusion
In conclusion, we observed that the conventional method was unable to remedy the plight of ambulance getting stuck at traffic signals which often lead to the casualty of patients. So in order to solve this problem we suggested two solutions to improve the probability of saving a life by eliminating unnecessary time delay at traffic congestion near traffic lights. Considering the dependencies and limitations of the CCTV camera it does not prove to be a good solution in commonly occurring cases.  Also, looking at the huge number of smartphones available in India and good internet connectivity in cities (which are the major spots for traffic jams) the Proposed System 2 (using smartphone's GPS) proves to be a better solution in most cases.
References
Blaise Kelly B.eng MSc A Green Wave Reprieve, http://gse.cat.org.uk/ papers?download=6%3Ablaise-kellya-green-wave-reprieve, last accessed 2016/07/23.
Ayush K.R. Mittal, Deepika Bhandari:  A Novel Approach to Implement Green Wave system and Detection of Stolen Vehicles. In: Proc. IEEE Conference on Advanced Computing, pp 1055-1059 (2013).
Lisa Zyga Physics of  green waves could make city traffic flow more smoothly, https://phys.org/news/2013-05-physics-green-city-traffic-smoothly.html, last accessed 2020/06/23.
Sarika B. Kale, Gajanan P. Dhok: Design of Intelligent Ambulance and Traffic Control. In: International Journal of Innovative Technology and Exploring Engineering (IJITEE), Volume-2, Issue-5, ISSN, pp. 2278-3075 (2013). 
S. Sharma, A. Pithora, G. Gupta, M. Goel, M. Sinha: Traffic light priority control for emergency vehicle using RFID. In: Int. J. Innov. Eng.Technol., vol. 2, no. 2, pp. 363–366 (2013).
Q.Zhang, M.A.Almulla, A.Boukerche: An Improved Scheme for Key Management of RFID In Vehicular Adhoc Networks. In: IEEE Latin America Transactions, vol. 11, no. 6,pp. 1286 - 1294 (2013).
Rashmi Hegde, Rohith R. Sali, Indira M.S: RFID and GPS based Automatic Lane Clearance System for Ambulance.In: International Journal of Advanced Electrical and Electronics Engineering, vol.2, no.3, pp.102- 107 (2013). 
Chang Guo, Demin Li, Guanglin Zhang, Menglin Zhai: Real-Time Path Planning In Urban Area via VANET-Assisted Traffic Information Sharing. In: IEEE Transactions On Vehicular Technology, pp. 5635 – 5649 (2018).
N.B.Soni, Jaideep Saraswat: A Review of IoT Devices for Traffic Management System. In: IEEE Xplore Complaint, Volume-2, Issue-5, pp. 1052-1055 (2017).
Sarika B. Kale, and Gajanan P. Dhok: Design of Intelligent Ambulance and Traffic Control. In:  International Journal of Innovative Technology and Exploring Engineering (IJITEE) ISSN: 2278-3075, Volume-2, Issue-5, pp. 211-214 (2013).
 Aman Dubey, Akshdeep, Sagar Rane: Implementation of an Intelligent Traffic Control System and Real-Time Traffic Statistics Broadcasting. In: IEEE International Conference On Electronics, Communication and Aerospace Technology Volume 2, pp 33-37 (2017).
 Naga Harsha.J, Nikhil Nair, Sheena Mariam Jacob, J.John Paul: Density Based Smart Traffic System with Real-Time Data Analysis Using IoT. In: IEEE International Conference On Current Trends toward Converging Technologies, pp 1-6 (2018).
Anna Merine George, V.I.George, Mary Ann George IoT: Based Smart Traffic Light Control System. In : IEEE International Conference on Control, Power, Communication and Computing Technologies (ICCPCCT), pp 148-151 (2018).
Anthony Theodore Chronopoulos, Charles Michael Johnston: A Real-Time Traffic Simulation System. In: IEEE Transactions on Vehicular Technology, vol. 47, no. 1, pp. 321-331 (1998).
W. Wen: A dynamic and automatic traffic light control expert system for solving the road congestion problem. In: Expert Systems with Applications, vol. 34, pp. 2370–2381 (2008). 
 S. Sharma, A. Pithora, G. Gupta, M. Goel,  M. Sinha: Traffic light priority control for emergency vehicle using RFID. In: Int. J. Innov. Eng.Technol, vol. 2, no. 2, pp. 363–366 (2017).
 Karthikeyan V.: Intelligent Traffic Control System for Congestion Control, Emergency Vehicle Clearance and Stolen Vehicle Detection. In: Asian Journal of Applied Science and Technology (AJAST), Volume 1, Issue 1, pp. 122-125 (2017).  
 A. A. George, A. Krishna, T. Dias, A. S. Vargheese, R. S. Divya:  Golden aid an emergency ambulance system. In: 2017 International Conference on Networks and Advances in Computational Technologies (NetACT), Thiruvanthapuram, pp. 473-476 (2017).



 '''





liStr = okStr.split()
initalLen = len(liStr)
print("Number of Words in Original string =",initalLen)
print("--------------------------------------------------")

initialTime = time.time()
pdfPath = 'PDFFiles/txt2.pdf' #Take care that the string in the input.txt is of this PDF

#Using Direct text extraction:
pdfTextFromMiner = extractPDFText(pdfPath)
time1 = time.time()
print("TEXT EXTRACTED FROM DIRECT TEXT EXTRACTION")
print("TIME TAKEN=",(time1-initialTime))
print()

#Using PDF to image and OCR
pdfTextFromOCR = extractPDFusingOCR(pdfPath)
time2 = time.time()
print("TEXT EXTRACTED FROM PDF TO IMAGE AND OCR")
print("TIME TAKEN=",(time2-initialTime))
print("--------------------------------------------------")

print("RATIO OF (Time of Direct Ext)/(Time of OCR)" , ((time1-initialTime)/(time2-initialTime)))
print("RATIO OF (Time of OCR)/(Time of Direct Ext)" , ((time2-initialTime)/(time1-initialTime)))
print("--------------------------------------------------")

liPDF1 = pdfTextFromMiner.split()
liPDF2 = pdfTextFromOCR.split()
print('Lenghts of Original, Direct text extraction and OCR Technique Strings are:')
print(len(liStr) , len(liPDF1) , len(liPDF2))
print("--------------------------------------------------")
ctr = 0

for i in range(0 , min((len(liStr) , len(liPDF1)))):
    if(liStr[i] != liPDF1[i]):
        ctr += 1
print('LCS of Original list of Words and Text Miner list:')
lcs1 = lcs(liStr , liPDF1)
print(lcs1)
print('Accuracy of Direct text extraction =' , ((lcs1/initalLen)*100) )
print()

print('LCS of Original list of Words and OCR Technique list:')
lcs2 = lcs(liStr , liPDF2)
print(lcs2)
print('Accuracy of OCR Technique =' , ((lcs2/initalLen)*100) )
print()













