
<div align="center">

# 🏠 House Price Prediction
### A Machine Learning Web Application using the Boston Housing Dataset

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-orange?style=flat-square&logo=scikit-learn)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

*Predict median house values using six regression models, deployed as a Flask web app.*

</div>

---

## 📌 Overview

This project trains and compares six machine learning regression models on the **Boston Housing Dataset** to predict the **Median Home Value (MEDV)**. The best-performing model (Random Forest) is serialized and served through a clean Flask web interface where users input property features and receive an instant price prediction.

---

## 🗂️ Project Structure

```
house_price_prediction/
│
├── app.py                        # Flask web application
├── house_price_prediction.ipynb  # Jupyter notebook (EDA + training)
├── HousingData.csv               # Dataset
├── model_rf.pkl                  # Saved Random Forest model
│
└── templates/
    └── index.html                # Prediction UI
```

---

## 📊 Dataset — Boston Housing

| Feature | Description |
|---------|-------------|
| CRIM | Per capita crime rate by town |
| ZN | Proportion of residential land zoned for lots over 25,000 sq ft |
| INDUS | Proportion of non-retail business acres per town |
| CHAS | Charles River dummy variable (1 if tract bounds river; 0 otherwise) |
| NOX | Nitric oxide concentration (parts per 10 million) |
| RM | Average number of rooms per dwelling |
| AGE | Proportion of owner-occupied units built prior to 1940 |
| DIS | Weighted distances to five Boston employment centres |
| RAD | Index of accessibility to radial highways |
| TAX | Full-value property-tax rate per $10,000 |
| PTRATIO | Pupil-teacher ratio by town |
| B | 1000(Bk - 0.63)² where Bk is the proportion of Black residents |
| LSTAT | % lower status of the population |
| **MEDV** | **Median value of owner-occupied homes in $1,000s (Target)** |

- **Total Records:** 506
- **Missing Values:** Handled via mean/std/median imputation

---

## 🤖 Models Trained

| Model | R² Score | Notes |
|-------|----------|-------|
| **Random Forest** ⭐ | ~0.87 | Best performer — saved as `model_rf.pkl` |
| Linear Regression | ~0.74 | Baseline |
| Ridge (α=0.01) | ~0.74 | L2 regularization |
| Lasso (α=0.01) | ~0.74 | L1 regularization |
| Decision Tree | ~0.69 | High variance |
| SVR | ~0.63 | Kernel-based |



## 🖥️ How to Use

1. Open `http://localhost:5000` in your browser
2. Enter values for **CRIM**, **ZN**, **INDUS**, and **CHAS**
3. Select a model (default: Random Forest)
4. Click **Predict House Price**
5. The predicted MEDV (×$1,000) is shown instantly

> The remaining 9 features are automatically filled with dataset averages.

---

## 🔗 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve the prediction UI |
| `/predict` | POST | Predict with one selected model |
| `/predict/all` | POST | Predict with all 6 models |
| `/metrics` | GET | Return model evaluation metrics |

**Example POST to `/predict`:**
```json
{
  "model": "Random Forest",
  "features": {
    "CRIM": 0.006, "ZN": 18, "INDUS": 2.31, "CHAS": 0
  }
}
```

---

## 📈 Exploratory Data Analysis

The notebook includes:
- Scatter plots: MEDV vs CRIM, RM, TAX, LSTAT
- Distribution plots: histogram, KDE, violin plot
- Correlation heatmap (Seaborn)
- Model comparison bar chart (R² scores)

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Web Framework:** Flask
- **ML Library:** scikit-learn
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Model Serialization:** Pickle

---

## 📄 Research Paper

An IEEE-format research paper accompanying this project is available in the repository:
📄 `House_Price_Prediction_IEEE.docx`


<div align="center">
Made with ❤️ | Boston Housing Dataset | scikit-learn
</div>
