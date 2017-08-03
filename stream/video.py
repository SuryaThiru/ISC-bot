import cv2
import numpy as np


class USBCamera:
	def __init__(self):
		self.cam = cv2.VideoCapture(0)

		self.w = 800
		self.h = 600

		self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.w)
		self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.h)

	def get_frame(self):
		success, frame = self.cam.read()

		if success:
			frame = cv2.resize(frame, (self.w, self.h))
		else:
			frame = np.zeros((self.h, self.w, 3), np.uint8)
			cv2.putText(frame, 'No camera', (40, 60), cv2.FONT_HERSHEY_SIMPLEX,
						1, (255, 255, 255), 1)

		ret, jpeg = cv2.imencode('.jpg', frame)
	    
		return jpeg.tostring()
