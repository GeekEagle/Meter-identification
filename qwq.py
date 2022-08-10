import tensorflow as tf
import os
print(tf.test.is_gpu_available())
path = './test/'
files = os.listdir(path)
for file in files:
    oldname = path+file
    newname = oldname.replace("png","jpg")
    os.rename(oldname,newname)