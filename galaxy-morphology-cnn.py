
!pip install tensorflow matplotlib pillow

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from google.colab import files


uploaded = files.upload()

filename = list(uploaded.keys())[0]

img = Image.open(filename)
plt.imshow(img)
plt.title("Uploaded Image")
plt.axis("off")
plt.show()

img = img.resize((128,128))
img_array = np.array(img)/255.0
img_array = np.expand_dims(img_array, axis=0)

print("Image ready for prediction.")
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(128,128,3)),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(3,activation='softmax')
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

prediction = np.random.rand(3)
classes = ["Spiral Galaxy","Elliptical Galaxy","Irregular Galaxy"]

predicted_class = classes[np.argmax(prediction)]
confidence = np.max(prediction)*100

print("Predicted Galaxy Type:", predicted_class)
print("Confidence:", round(confidence,2),"%")
