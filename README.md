Used Car Price Predictor

A Machine Learning web application that predicts the resale price of used cars based on features like kilometers driven, car age, fuel type, transmission, seller type, and ownership history.

📌 Project Overview

This project demonstrates an end-to-end ML workflow:

✔ Data preprocessing and feature engineering
✔ Model training using Random Forest Regressor
✔ Model serialization using Pickle
✔ Web application built with Flask
✔ User-friendly frontend form for predictions

🧠 Machine Learning Model

Algorithm: Random Forest Regressor

Dataset: CarDekho used car dataset

Features Used:

Kilometers Driven

Car Age

Fuel Type

Seller Type

Transmission

Owner Type

The model learns pricing patterns from historical resale data and predicts estimated selling price.

🌐 Web Application

The Flask app allows users to input car details and instantly get a predicted resale value.

User Inputs:

Kilometers Driven

Car Age

Fuel Type

Seller Type

Transmission

Ownership History

🛠 Tech Stack
Category	Tools Used
Language	Python
ML Library	Scikit-Learn
Web Framework	Flask
Frontend	HTML, CSS
Model Storage	Pickle
▶ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/Used-Car-Price-Predictor.git
cd Used-Car-Price-Predictor
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Train the model (if not already trained)
python model_training.py
4️⃣ Run the web app
python app.py

Open in browser:

http://127.0.0.1:5000
📂 Project Structure
Used-Car-Price-Predictor/
│
├── app.py                  # Flask web app
├── model_training.py       # ML training script
│
├── data/
│   └── car_data.csv
│
├── model/
│   └── car_price_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
🎯 Future Improvements

Add more car features (brand, engine size)

Improve model accuracy with hyperparameter tuning

Deploy the app online

👨‍💻 Author

Ayush Dutta
Machine Learning Enthusiast