import cv2


imgcapture=cv2.videoCapture(0)
result=True

while(result):
	ret,frame=imgcapture.read()
	cv2.imwrite("test.jpg",frame)
	result=false
	print("Image Captured.....")

imgcapture.release()