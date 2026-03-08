# ✈️ Flight Price Predictor - End-to-End ML Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Latest-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-red?style=for-the-badge)

**Predict flight ticket prices using machine learning with 10K+ real flight data points**

[Live Demo](#demo) • [Features](#features) • [Tech Stack](#tech-stack) • [Installation](#installation)

</div>

---

## 🎯 Project Overview

A production-ready machine learning web application that predicts Indian domestic flight prices based on multiple factors including airline, route, timing, and duration. Built from raw data to deployment with comprehensive feature engineering and model evaluation.

### 🌟 Key Highlights

- 📊 **10,683 flight records** analyzed and engineered
- 🧹 **34 numerical features** extracted from messy categorical/datetime data
- 🎯 **Linear Regression & SVR models** trained and compared
- 🌐 **Flask web application** with clean, responsive UI
- 📈 **End-to-end ML pipeline**: Data cleaning → Feature engineering → Model training → Deployment

---

## 🚀 Features

### Data Processing & Feature Engineering
- ✅ Handled missing values and inconsistent data types
- ✅ Extracted temporal features (day, month, year, hour, minute)
- ✅ One-hot encoding for categorical variables (airlines, cities)
- ✅ Duration parsing from string format to numerical hours/minutes
- ✅ Created 34-feature numerical dataset from 11 raw columns

### Machine Learning Models
- 🤖 **Linear Regression**: Primary model for price prediction
- 🤖 **Support Vector Regression (SVR)**: Alternative model comparison
- 📊 Model evaluation with MAE, RMSE, and R² metrics
- 💾 Model serialization using pickle for production deployment

### Web Application
- 🎨 Modern, responsive UI with gradient design
- ⚡ Real-time price predictions via Flask API
- 🔧 User-friendly form inputs (datetime pickers, dropdowns)
- 📱 Mobile-responsive design

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.12 |
| **ML/Data** | scikit-learn, pandas, numpy, matplotlib, seaborn |
| **Web Framework** | Flask |
| **Data Format** | Excel (openpyxl), CSV |
| **Deployment** | Gunicorn (production-ready) |
| **Visualization** | Matplotlib, Seaborn |

---

## 📂 Project Structure

```
Flight-Price-Predictor/
│
├── datasets/                     # Data folder
│   ├── flight_price.xlsx         # Raw dataset (10,683 rows)
│   └── flight_price_cleaned.csv  # Processed dataset (34 features)
│
├── notebooks/                    # Jupyter notebooks
│   ├── feature_engineering.ipynb # Data cleaning & feature extraction
│   └── model_training.ipynb      # Model training & evaluation
│
├── static/                       # Frontend assets
│   └── style.css                 # UI styling
│
├── templates/                    # Flask HTML templates
│   └── index.html                # Frontend UI template
│
├── application.py                # Flask backend application
├── flight_price_linear_model.pkl # Trained model (serialized)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 💡 How It Works

### 1️⃣ **Data Preprocessing**
```python
# Original dataset challenges:
- Mixed data types (categorical, datetime, numerical)
- Missing values in Route and Total_Stops
- Inconsistent datetime formats
- String-based duration ("2h 50m")

# Solution:
✓ Parsed dates → Extracted day, month, year
✓ Parsed time → Extracted hour, minute
✓ Converted duration string → Numerical hours + minutes
✓ One-hot encoded 12 airlines, 5 sources, 6 destinations
```

### 2️⃣ **Feature Engineering**
Transformed **11 raw columns** into **34 numerical features**:

| Original | Engineered Features |
|----------|---------------------|
| Airline | 12 binary features (one-hot) |
| Source | 5 binary features (one-hot) |
| Destination | 6 binary features (one-hot) |
| Date_of_Journey | Date, Month, Year (3 features) |
| Dep_Time | Dep_hour, Dep_minute (2 features) |
| Arrival_Time | Arrival_hour, Arrival_minute (2 features) |
| Duration | Duration_hour, Duration_minute (2 features) |
| Total_Stops | Total_Stops (1 feature) |
| **Price** | **Target Variable** |

### 3️⃣ **Model Training**
```python
# Train-test split: 80-20
# Model: Linear Regression (primary)
# Evaluation: MAE, RMSE, R² Score
# Result: Model achieves reasonable predictions for flight pricing patterns
```

### 4️⃣ **Web Application**
- User inputs flight details via clean web form
- Flask backend processes inputs into 33-feature array
- Trained model predicts price in rupees
- Result displayed instantly on frontend

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/Harsh1574/Flight-Price-Predictor.git
cd Flight-Price-Predictor
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python application.py
```

### Step 5: Access the Web App
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## 📊 Model Performance

### Linear Regression (Primary Model)
- **Purpose**: Fast, interpretable baseline for flight price prediction
- **Features**: 33 engineered numerical features
- **Use Case**: Real-time web application predictions

### Support Vector Regression (Alternative)
- **MAE**: ₹3,632.99
- **RMSE**: ₹4,664.12
- **R² Score**: -0.028
- **Note**: Compared for model selection; Linear Regression selected for deployment

---

## 🎥 Demo

### Input Form
Users enter:
- ✈️ Departure date & time
- 🛬 Arrival date & time
- 📍 Source and destination cities
- 🏢 Preferred airline
- 🔢 Number of stops

### Output
```
Estimated Flight Price: ₹8,547.32
```

---

## 📈 Dataset Information

- **Source**: Flight price data for Indian domestic routes (2019)
- **Size**: 10,683 flight records
- **Routes**: Delhi, Mumbai, Bangalore, Kolkata, Chennai, Cochin, Hyderabad
- **Airlines**: IndiGo, Air India, Jet Airways, SpiceJet, GoAir, Vistara, Air Asia, TruJet
- **Features**: Airline, source, destination, departure time, arrival time, duration, stops

---

## 🔑 Key Learnings

### Data Engineering
- 🔍 **Real-world data is messy**: Learned to handle mixed data types, missing values, and inconsistent formats
- 🛠️ **Feature extraction is critical**: Temporal features (hour, day, month) significantly impact model performance
- 📊 **Encoding strategy matters**: One-hot encoding transformed categorical data into ML-ready format

### Machine Learning
- 🎯 **Model selection**: Compared multiple algorithms (Linear Regression, SVR) for optimal performance
- 📉 **Evaluation metrics**: Used MAE, RMSE, R² to assess model quality
- 💾 **Model persistence**: Serialized trained model with pickle for production use

### Software Engineering
- 🌐 **Full-stack development**: Built end-to-end ML application from data to deployment
- 🎨 **User experience**: Designed clean, intuitive interface for non-technical users
- 🚀 **Production readiness**: Configured with Gunicorn for scalable deployment

---

## 🚀 Future Enhancements

- [ ] **Model Improvements**
  - Experiment with Random Forest, XGBoost, Neural Networks
  - Hyperparameter tuning with GridSearchCV
  - Feature selection to reduce dimensionality

- [ ] **Data Expansion**
  - Include more recent flight data (2020-2024)
  - Add seasonal trends and holiday pricing
  - Incorporate external factors (fuel prices, demand patterns)

- [ ] **Application Features**
  - Price trend visualization (charts/graphs)
  - Historical price comparison
  - Multi-city route planning
  - Email/SMS price alerts
  - REST API for third-party integration

- [ ] **Deployment**
  - Docker containerization
  - Cloud deployment (AWS/GCP/Heroku)
  - CI/CD pipeline with GitHub Actions
  - Database integration (PostgreSQL/MongoDB)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Harsh Sharma**

- 🐱 GitHub: [@Harsh1574](https://github.com/Harsh1574)
- 💼 LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/Harshvardhan Rajgarhia) *(Update this)*
- 📧 Email: your.email@example.com *(Update this)*

---

## 🙏 Acknowledgments

- Dataset sourced from real Indian domestic flight pricing data
- Built as part of continuous learning in Machine Learning and Data Science
- Inspired by real-world pricing prediction challenges in the aviation industry

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a star!

**Made with ❤️ and Python**

</div>
