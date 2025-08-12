import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Path to your trained model file
model_path = r"D:\Projects_expriment\CNN-Introduction\dogs_vs_cats\dogs_vs_cats_model.h5"

# Load the trained model
model = tf.keras.models.load_model(model_path)

def predict_image(img_path):
    """
    Predicts whether the image is of a dog or a cat.
    Args:
        img_path (str): Path to the image file
    """
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction
    prediction = model.predict(img_array)[0][0]
    label = "Dog" if prediction > 0.5 else "Cat"

    # Display result
    plt.imshow(image.load_img(img_path))
    plt.title(f"Prediction: {label} ({prediction:.2f})")
    plt.axis("off")
    plt.show()

# Use the image path you provided
# test_image_path = r"D:\Projects_expriment\CNN-Introduction\dogs_vs_cats\test\dogs\dog.5.jpg"
test_image_path = r"D:\Projects_expriment\CNN-Introduction\dogs_vs_cats\train\cats\cat.241.jpg"
predict_image(test_image_path)
