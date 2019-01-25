from subprocess import call
import sys
import os

img_path=sys.argv[1]

for f in os.listdir(img_path):
    call(["python", "facenet/src/face_recognition_image.py", img_path + "/" + f])
