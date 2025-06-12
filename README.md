# 🎯 Face Detection & Image Annotation using OpenCV

This project demonstrates real-time **face and eye detection** using Haar cascades in OpenCV, along with static image annotation and drawing.

---

## 📁 Project Structure

```
FACE_DETECTION/
│
├── myvenv/                         
├── .gitignore                      
├── demo.py                         (Static image annotation)
├── eminem.jpg                      (Input image for demo.py)
├── face_detection.py               (ive webcam face + eye detection)
├── haarcascade_eye.xml             (cascade file for eye detection)
├── haarcascade_frontface_default.xml  
├── README.md                     
└── requirements.txt              
```
---

## 🧪 Features

- ✅ Real-time face and eye detection via webcam  
- ✅ Draw bounding boxes and label faces in real-time  
- ✅ Annotate and modify static images (e.g., add text, mask pixels)
- ✅ Use of `matplotlib` for image display and debugging

---

## 🔧 Setup Instructions

### 1. Clone the repository:
```bash
git clone <url>
pip install requirements.txt
cd face_detection
```

### Create and activate a virtual environment

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### 🚀 Run the Code

#### Face Detection via Webcam:

```bash
python face_detection.py
```

### 🧠 Haarcascade Files
```
The required Haarcascade XML files are included in this repo:

- haarcascade_frontalface_default.xml
- haarcascade_eye.xml

These are used internally by OpenCV to detect faces and eyes.
```
### 📦 Requirements
```
Installed via requirements.txt:
- opencv-python
- matplotlib
- numpy
```
### ✍️ Author
> *Saumya Gupta*
