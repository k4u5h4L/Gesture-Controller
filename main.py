"""
this is file is to be run in your console
"""

from press_key import press
from predict import predict_image
import cv2
import time


def main():
    vid = cv2.VideoCapture(0)

    while True:
        # time.sleep(0.5)
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)

        pred = predict_image(frame)

        # ind = pred[0].index(max(pred[0]))
        print(pred)

        # if ind == 0:
        #     press("a")
        #     print("left")
        # elif ind == 1:
        #     press("d")
        #     print("right")
        # elif ind == 2:
        #     press("w")
        #     print("nothing")
        # else:
        #     press("P")
        #     print("both")
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()