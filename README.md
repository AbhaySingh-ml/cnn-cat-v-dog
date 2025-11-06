# 🐶🐱 CNN Cat vs Dog Classification

## 📘 Over
This project demonstrates a **Convolutional Neural Network (CNN)** model built to classify images of **cats and dogs**.  
It is a foundational deep learning project aimed at understanding **image classification**, **data preprocessing**, and **model evaluation** using **TensorFlow/Keras**.

---

## 🚀 Objective
The goal is to train a neural network that can accurately predict whether an image contains a **cat** or a **dog**.

---

## 🧠 Key Learnings
- Implementation of **CNNs for image classification**
- Image preprocessing and augmentation techniques
- Application of **Keras Sequential API**
- Performance evaluation using **accuracy**, **loss**, and **confusion matrix**
- Saving and loading trained models (`.h5` format)

---

## ⚙️ Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| Language | Python |
| Framework | TensorFlow / Keras |
| Data Handling | NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| IDE / Notebook | Jupyter / VS Code |
| Deployment (optional) | Streamlit |

---

## 🗂️ Project Structure

cnn-cat-v-dog/
│
├── dataset/ # Training and validation data
│ ├── train/
│ ├── test/
│
├── notebooks/
│ └── cat_dog_cnn.ipynb # Main notebook for model training
│
├── models/
│ └── dogs_vs_cats_model.h5 # Trained CNN model (linked externally)
│
├── images/ # Example input/output images
│
├── app.py # Streamlit app for inference (optional)
│
├── README.md # Project documentation
│
└── requirements.txt # Python dependencies



---

## 🔍 Model Architecture
- **Input Layer:** 128×128 RGB images  
- **Convolution + MaxPooling Layers:** 3 blocks  
- **Flatten Layer**  
- **Dense Layers:** Fully connected layers with ReLU activation  
- **Output Layer:** Sigmoid activation (binary classification)

---

## 📈 Training & Evaluation
- **Loss Function:** Binary Crossentropy  
- **Optimizer:** Adam  
- **Metrics:** Accuracy  
- **Epochs:** ~25–30  
- **Batch Size:** 32  

The model achieved an **accuracy of ~90%** on the validation dataset.

---

## 📦 Model File
The trained model file (`dogs_vs_cats_model.h5`) is large (>50MB) and cannot be previewed on GitHub.  

You can download it here once uploaded:  
📥 [Download Model from Google Drive](#) *(Add your link here after upload)*

---

## 🖥️ How to Run the Project
1. **Clone the repository**
   ```bash
   git clone https://github.com/AbhaySingh-ml/cnn-cat-v-dog.git
   cd cnn-cat-v-dog

