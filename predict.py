import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2

def cv2_to_pil(img): 
    # Since you want to be able to use Pillow (PIL)
    # print(img)
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('model/keras_model.h5')

# Replace this with the path to your image
# image = Image.open('test_photo.jpg')
# cam = cv2.VideoCapture(0)

def predict_image(frame):
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # ret_val, img = cam.read()
    # cv2.imshow("Camera", img)
    image = cv2_to_pil(frame)

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    # image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)

    return prediction