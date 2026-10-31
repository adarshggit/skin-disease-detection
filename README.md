# 🏥 Skin Disease Detection and Prescription

## 📌 Description
This project is a **Skin Disease Detection System** that classifies skin diseases based on uploaded images. The system predicts the skin condition, provides a prescription page with details, and shows nearby skincare centers using an embedded **Google Maps iframe**.

## 🛠️ Tools & Technologies Used
- 🔥 **Flask** - Backend framework for handling requests
- 🤖 **TensorFlow/Keras** - Deep learning model for image classification
- 🖼️ **OpenCV & Keras Preprocessing** - Image processing and resizing
- 🏗️ **HTML, CSS, JavaScript** - Frontend for UI
- 📍 **HTML tag (iframe)** - For showing nearby skincare centers

## 📂 Project Structure
```
📦 Skin-Disease-Detection
 ┣ 📂 static  # Stores uploaded images
 ┣ 📂 templates  # HTML files
 ┣ 📜 final_model.keras  # Trained deep learning model
 ┣ 📜 app.py  # Main Flask application
 ┣ 📜 requirements.txt  # Dependencies list
 ┣ 📜 README.md  # Project documentation
```

## 🚀 How to Run
1. **Clone the Repository** 🖥️
   ```bash
   git clone https://github.com/yourusername/skin-disease-detection.git
   cd skin-disease-detection
   ```

2. **Install Dependencies** 📦
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App** ▶️
   ```bash
   python app.py
   ```

4. **Open in Browser** 🌍
   - Go to `http://127.0.0.1:5000/` in your browser.

## 🎯 Features
✅ Upload an image of the affected skin area 📸  
✅ Predicts one of the **7 skin diseases** using deep learning 🏥  
✅ Provides a **prescription page** with treatment details 📜  
✅ Displays **nearby skincare centers** using Google Maps 📍  

## 📊 Result
- The model predicts the disease from the following categories:
  - Cold sores
  - Ichthyosis
  - Ringworm
  - Vitiligo
  - Acne
  - Eczema
  - Psoriasis
- After prediction, it provides a detailed **prescription page**.
- The system also embeds a Google Maps iframe to show **nearby skin care locations**.

## 🏗️ Future Improvements
🔹 Improve accuracy by training on a larger dataset 📈  
🔹 Enhance UI/UX for a better user experience 🎨  
🔹 Implement a chatbot for skin consultation 🤖  

## 🤝 Contribution
Feel free to fork and contribute to this project! Pull requests are welcome. 🎉


---
🚀 **Developed by [Adarsha Gouda]** 👨‍💻

## 🖥️ Project Output

![Skin Disease Detection Output](screenshots/output.jpg)
