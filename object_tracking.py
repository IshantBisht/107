import cv2
import time
import math
P1=530
P2=300
XS=[]
YS=[]

video = cv2.VideoCapture("bb3.mp4")
tracker=cv2.TrackerCSRT_create()
returned,img=video.read()
beebox=cv2.selectROI("Tracking",img,False)
tracker.init(img,beebox)
print(beebox)

def drawbox(img,beebox):
    x,y,w,h=int(beebox[0]),int(beebox[1]),int(beebox[2]),int(beebox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    
def goal_track(img,beebox):
    x,y,w,h=int(beebox[0]),int(beebox[1]),int(beebox[2]),int(beebox[3])
    C1=x+int(w/2)
    C2=y+int(h/2)
    cv2.circle(img,(C1,C2),2,(0,0,255),5)
    dist=math.sqrt(((C1-P1)**2)+(C2-P2)**2)
    if(dist<=20):
        cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    XS.append(C1)
    YS.append(C2)
    for i in range(len(XS)-1):
       cv2.circle(img,(XS[i],YS[i]),2,(0,0,255),5)

while True:
    check,img = video.read() 
    success,beebox=tracker.update(img)
    if(success):
        drawbox(img,beebox)
    else:
        cv2.putText(img,"lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2) 
    goal_track(img,beebox) 

    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



