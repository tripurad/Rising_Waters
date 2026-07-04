# 🌊 Rising Waters – Flood Prediction System

## 📌 Project Overview

Rising Waters is a Machine Learning-based Flood Prediction System developed using Python and Flask. The application predicts the likelihood of flooding based on historical weather and environmental parameters such as rainfall, temperature, humidity, cloud cover, and geographical subdivision. The goal of the project is to support early flood prediction and assist disaster management authorities in making timely decisions.

---

## 🚀 Features

- Predicts flood occurrence using Machine Learning
- User-friendly web interface built with Flask
- Uses historical weather and rainfall data
- Instant prediction results
- Supports disaster management and early warning systems

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript
- Jupyter Notebook

---

## 📂 Project Structure

```
RISING-WATERS/
│
├── app.py
├── flood_model.pkl
├── flood dataset.csv
├── rising-proj.ipynb
│
├── templates/
│   ├── index.html
│   ├── chance.html
│   └── no_chance.html
│
├── static/
```

---

## 📊 Dataset

The project uses a historical flood prediction dataset containing weather and rainfall parameters including:

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Seasonal Rainfall
- Average June Rainfall
- Geographical Subdivision

---

## ⚙️ Machine Learning Models

The following algorithms were evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

The best-performing model was saved as `flood_model.pkl` and integrated with the Flask application.

---

## 💡 How It Works

1. Enter weather details.
2. Click **Predict Flood**.
3. The trained machine learning model processes the data.
4. The application displays either:
   - Flood Likely
   - No Flood

---

## 🔮 Future Enhancements

- Live Weather API integration
- GIS-based flood maps
- SMS alert system
- Mobile application
- Cloud deployment

---

## 👩‍💻 Author

**Tripura Dwarampudi**
