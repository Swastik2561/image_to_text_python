from __future__ import print_function
import cv2
from PIL import Image
import PIL.Image
from wand.image import Image
from pytesseract import image_to_string
import pytesseract

#with Image(filename='/root/Downloads/Aadhaar Information Updated.pdf') as img:
 #   print('width =', img.width)
  #  print('height =', img.height)
   # print('pages =', len(img.sequence))
   # print('resolution =', img.resolution)

#with img.convert('/root/Downloads/Aadhaar Information Updated.pdf') as converted:
 #   converted.save(filename='sample.png')


#img = cv2.resize(warped,(1350,1150))
#cv2.imshow("output",imS)
#cv2.imwrite('Output Image.PNG',imS)
#cv2.waitKey(0)

#Place the tesseract executable cmd in the below
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

#test data where you want it to be stored..
TESSDATA_PREFIX = '/root/scripts/'

#place the image path in the below statement
output = pytesseract.image_to_string(PIL.Image.open('/root/Downloads/GRE.png').convert('RGB'), lang='eng')

##output is displayed on the terminal
print(output)
