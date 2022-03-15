import cv2
import dropbox
import time
import random

start_time = time.time()

def takeSnap():
    num = random.randint(0,100)
    #initializing cv2
    vcObj = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        
        ret,frame=vcObj.read()
        imgname = "img"+str(num)+".png"
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite(imgname,frame)
        start_time=time.time
        result=False
    return imgname
    print("snapshot taken")
    #releases the camera
    vcObj.release()
    cv2.destroyAllWindows()
    #closes all the window that might be opened while this process

def upload_file( img_name ):
     access_token = "sl.BD3rTK56WpYcyMOsKHR70sNEAcvKxNG6velBrjSdaHR3thMaCtFmZKq6u2wOuMV2ZECa8cLljbzaipyVDr_KTjFM82EtaxOdazbJ1EiqQGDJHyrCMNacliegfI8PS6mIM0dpc9CK4FCY"
     file =img_name
     file_from = file
     file_to = "/BrianSnapped/"+(img_name)
     dbx = dropbox.Dropbox(access_token)
     with open(file_from, 'rb') as f:
        # to resolve the path errors last parameter is added
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main ():
    while(True):
        if ( (time.time()-start_time  ) >= 5 ):
            name = takeSnap()
            upload_file(name)
main()
            