# 🎬 Movie Success Prediction using XGBoost and Fuzzy C-Means Clustering

## 📘 Overview
This project aims to predict the **success of movies** based on various features such as budget, genre, director, cast popularity, and production details.  
It combines **machine learning** and **unsupervised clustering** techniques to analyze data and provide insights into movie performance.

## 🧠 Methodology

### 1️⃣ XGBoost Model
- Used for **Movie Success Prediction** (Hit/Flop/Moderate).
- Extracted key features like:
  - Genre
  - Cast
  - Director
  - Plot
- Trained and evaluated the model using metrics such as **accuracy**, **precision**, and **recall**.
- Achieved the highest accuracy among all models tested (compared to Random Forest and CNN).

### 2️⃣ Fuzzy C-Means Clustering
- Applied for **Target Audience Prediction**.
- Helps in grouping audiences with similar viewing patterns or preferences.
- Unlike K-Means, Fuzzy C-Means allows a movie to belong to multiple audience clusters with different probabilities.
- The clustering excludes **age** as a feature to maintain general audience segmentation.

## 🧩 Technologies Used
- **Python**
- **Pandas**, **NumPy**
- **XGBoost**
- **Scikit-learn**
- **Matplotlib**, **Seaborn**
- **Fuzzy C-Means (fcmeans library)**

## 🧪 Results
- **XGBoost Accuracy:** 92%  
- **Random Forest Accuracy:** 86%  
- **CNN Accuracy:** 80%  
- **Fuzzy C-Means:** Identified 3 optimal audience clusters based on preferences and engagement.

## 📊 Key Insights
- Budget and IMDB ratings are strong predictors of movie success.
- Audience preferences vary significantly by genre and release timing.
- Fuzzy clustering helps understand overlapping audience interests more effectively than traditional methods.

## 🚀 Future Enhancements
- Integrate sentiment analysis from social media data.
- Include trailer engagement metrics (views, likes, comments).
- Build a web-based dashboard for real-time prediction and visualization.


- [Fuzzy C-Means Paper](https://ieeexplore.ieee.org/document/1077009)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
