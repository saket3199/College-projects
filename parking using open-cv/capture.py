# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:57:11 2019

@author: Saket Mishra
"""

import cv2
#import matplotlib as plt
def park():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Parking_project")
    img_counter =0
    print("ESC to exit and Space to Capture")
    while True:
        ret, frame = cam.read()
    #img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    #cv2.resizeWindow(frame,250,250)
        cv2.imshow("Parking",frame)
    #plt.title("Parking")
        if not ret:
            break
    
        k=cv2.waitKey(1)
    
        if k%256 ==27:
            print("Exiting.....")
        elif k%256 ==32:
            img_name ="Parked vehicles{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            print("{} captured".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()
