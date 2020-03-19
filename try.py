import cv2
import numpy as np

def main():

	img = cv2.imread("d1.jpg")
	height, width, layer = img.shape
	imgHSV = np.zeros((height, width, 3), np.uint8)
	imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	imgHue, imgSaturation, imgValue = cv2.split(imgHSV)
	#cv2.imshow("image3",imgValue)
	cv2.waitKey(0)

	return

if __name__ == "__main__":
    main()


#	img = cv2.imread("d1.jpg")
	#cv2.imshow("image1",img)

	#gray = extractValue(img)

	#cv2.imshow("image2",gray)	
	#height, width, layer = img.shape
	#imgHSV = np.zeros((height, width, 3), np.uint8)
	#imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #imgHue, imgSaturation, imgValue = cv2.split(imgHSV)
    #cv2.show("image3",imgValue)
    #cv2.waitKey(0)