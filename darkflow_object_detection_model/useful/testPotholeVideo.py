import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np
import time

option = {
	'model':'./cfg/yolov2-tiny-voc-1c.cfg',
	'load': 5500,
	'threshold': 0.1
}

tfnet = TFNet(option)

capture = cv2.VideoCapture('<*******path-to-input-video*******>')

colors = [tuple(255 * np.random.rand(3)) for i in range(5)]

count = 0

while(capture.isOpened()):
	stime = time.time()
	ret, frame = capture.read()
	results = tfnet.return_predict(frame)
	if ret:
		for color, result in zip(colors, results):
			tl = (result['topleft']['x'], result['topleft']['y'])
			br = (result['bottomright']['x'], result['bottomright']['y'])
			label = result['label']
			confidence = result['confidence']
			frame = cv2.rectangle(frame, tl, br, color, 7)
			percentageConfidence = round(confidence*100,2)
			frame = cv2.putText(frame, label+": "+str(percentageConfidence)+"%", tl,cv2.FONT_HERSHEY_PLAIN, 2, color, 4)
			#cv2.imwrite("frames/frame%d.jpg" %count, frame)
			plt.imsave("frames/frame%d.png" %count, frame)
			count = count+1
		cv2.imshow('frame', frame)
		cv2.imwrite("frames/frame%d.jpg" %count, frame)
		print('FPS {:.1f}'.format(1 / (time.time() - stime)))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		capture.release()
		cv2.destroyAllWindows()
		break
