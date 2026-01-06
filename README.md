# Fake-News-Detection
# 📰 Fake News Detection Using Machine Learning

A machine learning pipeline to detect fake news articles using natural language processing and classification techniques. This project leverages text preprocessing, feature extraction (TF-IDF), and ML models to classify news as **real** or **fake**.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)

---

## 🚀 Features

- Binary classification of news articles: **Real** or **Fake**
- NLP preprocessing (stopwords removal, stemming)
- Feature extraction using **TF-IDF Vectorizer**
- Model training using **PassiveAggressiveClassifier**
- Performance evaluation (Accuracy, Confusion Matrix)
- Modular and easy-to-understand codebase

---

## 🛠️ Technologies Used

- Python 3.10
- Numpy
- Pandas
- Scikit-learn
- TQDM
- Matplotlib
- Joblib

---

## 📂 Project Structure
```bash
Fake-News-Detection/
├── data/ # Contains train/test datasets
├── models/ # Saved ML models (.pkl)
├── notebooks/ # Jupyter notebooks for experimentation
├── utils/ # Preprocessing and evaluation utilities
├── main.py # Script to train and evaluate models
├── predict.py # CLI tool to predict from custom input
├── requirements.txt
├── runtime.txt # Python version for Netlify (if deployed)
└── README.md

```
---

## 📊 Dataset

- **Source**: [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- Consists of two CSV files:
  - `True.csv`: Real news articles
  - `Fake.csv`: Fake news articles

---

## 🧠 Model Training

The primary model used is:

- **PassiveAggressiveClassifier** (from `sklearn.linear_model`)
  - Designed for large-scale online learning
  - Performs well in text classification tasks

Accuracy achieved: ~85.75%

---

## 🔄 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/Goutham7675/Fake-News-Detection.git
cd Fake-News-Detection
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Train the Model
```bash
python main.py
```
### 4. Predict Custom News
```bash
python predict.py
````
You'll be prompted to enter a news article or headline for prediction.

### 📈 Output
  1. Model accuracy

  2. Confusion matrix visualization

  3. Predictions on test dataset

  4. Custom CLI predictions

### 📌 Future Work
Integrate LSTM/Transformer-based models

Add web interface with Flask or Streamlit

Deploy model on Heroku/Netlify

### 👨‍💻 Developer
Goutham Reddy

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.


---
