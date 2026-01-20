# Flight-Price-Predictor

**Raw data is never ready for machine learning.**

Recently, I worked on feature engineering and data cleaning using a flight price dataset to transform raw, mixed-type data into a fully numeric, model-ready dataset ✈️📊

## 📌 Dataset overview

Source: Flight price data (Excel)

Initial shape: Multiple categorical, datetime, and numerical columns

Goal: Prepare clean features suitable for ML model training

## 🔧 Key steps I performed:

**1️⃣ Initial data inspection**
Checked shape, datatypes, and missing values using df.shape, df.info(), and df.isnull().sum() to understand data quality issues upfront.

**2️⃣ Handling missing values**
Identified columns with null values and treated them appropriately to ensure no data leakage or model bias.

**3️⃣ Datetime feature engineering**
Extracted meaningful features from date and time columns, such as:

  - Journey day and month

  - Departure and arrival hours/minutes

  - Total duration split into hours and minutes

This helped convert raw timestamps into useful numerical signals.

**4️⃣ Categorical encoding**
Applied One-Hot Encoding on categorical features like airline, source, and destination to convert them into machine-readable format.

**5️⃣ Dropping irrelevant columns**
Removed original categorical and redundant columns after encoding to reduce noise and dimensional redundancy.

**6️⃣ Target column alignment**
Repositioned the Price column to the end, clearly separating features vs target, which is a good modeling practice.

**7️⃣ Final dataset creation**
Concatenated engineered numerical features with encoded categorical features to create a fully numeric, clean dataset ready for ML training.

## ✅ Final outcome

  - No missing values

  - All columns numeric

  - Clear feature-target separation

  - Dataset ready for regression modeling

Feature engineering isn’t just about cleaning data — it’s about making data meaningful and usable.

Would love to hear how others approach feature engineering on real-world datasets 👇

#FeatureEngineering #DataAnalytics #MachineLearning #DataCleaning #Python #Pandas #LearningInPublic
