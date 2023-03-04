import cv2
def detect_everything(path):
    window="bruh"
    img=path
    image_grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cascade_eyes=cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_eye.xml")
    cascade_face=cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
    cascade_up=cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_upperbody.xml")
    cascade_low=cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_lowerbody.xml")
    detected_eye=cascade_eyes.detectMultiScale(image_grey,minSize=(50,50))
    detected_face=cascade_face.detectMultiScale(image_grey,minSize=(50,50))
    detected_up=cascade_up.detectMultiScale(image_grey,minSize=(50,50))
    detected_down=cascade_low.detectMultiScale(image_grey,minSize=(50,50))
    if len(detected_eye)!=0 or len(detected_face)!=0 or len(detected_up)!=0 or len(detected_down)!=0:
        for (x,y,width,height) in (detected_eye):
            cv2.rectangle(img,(x,y),(x+height,y+width),(0,255,0),2)
        for (x,y,width,height) in (detected_face):
            cv2.rectangle(img,(x,y),(x+height,y+width),(0,0,0),2)
        for (x,y,width,height) in (detected_up):
            cv2.rectangle(img,(x,y),(x+height,y+width),(255,255,255),2)
        for (x,y,width,height) in (detected_down):
            cv2.rectangle(img,(x,y),(x+height,y+width),(255,0,0),2)
    return img

def edge(img):
    im_grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    im_blur=cv2.GaussianBlur(im_grey,(3,3),0)
    return cv2.Canny(im_blur,20,30)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

def skele(inp):
    proto="pose/mpi/pose_deploy_linevec_faster_4_stages.prototxt"
    weights="pose/mpi/pose_iter_160000.caffemodel"
    net=cv2.dnn.readNetFromCaffe(proto,weights)
    inpb=cv2.dnn.blobFromImage(inp,1/255,(368,368),(0,0,0),swapRB=False,crop=False)
    net.setInput(inpb)
    output=net.forward()
    points=[]
    for i in range(len()):
        probMap=output[0,i,:,:]
        minVal,prob,minLoc,point=cv2.minMaxLoc(probMap)
        x=(inp.size[0]*point[0])/output.shape[0]
        y=(inp.size[1]*point[1])/output.shape[1]
        if prob>0.8:
            cv2.circle(inp, (int(x), int(y)), 15, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            points.append((int(x),int(y)))
        return inp
while True:
    ret,frame=cap.read()
    cv2.imshow('bruh',skele(frame))
    cv2.waitKey(10)
