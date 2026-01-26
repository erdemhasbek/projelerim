# 🌸 Iris Species Classification & Dimensionality Reduction

This project uses machine learning to classify Iris flowers into three species: Setosa, Versicolor, and Virginica. It demonstrates a complete data science pipeline, from preprocessing to advanced visualization.

## 🚀 Project Overview

The goal is to build a model that predicts flower species based on sepal and petal measurements. The project explores multiple algorithms and optimizes the best one for maximum accuracy.

## 📊 Key Features

1.  **Data Preprocessing:** Features are standardized using `StandardScaler` to ensure model stability.
2.  **Model Comparison:** Evaluates Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Machines (SVM), and Random Forest using **5-fold cross-validation**.
3.  **Hyperparameter Tuning:** Uses `GridSearchCV` to find the optimal settings for the Logistic Regression model.
4.  **Final Evaluation:** The tuned model achieved **100% accuracy** on the unseen test set.
5.  **Interactive Visualization:** * **Confusion Matrix:** Provides a clear view of prediction performance.
    * **PCA (Principal Component Analysis):** Reduces 4D data to 2D for visual cluster analysis.



## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** * `Scikit-learn` (Machine Learning)
    * `Pandas` (Data Manipulation)
    * `Matplotlib` & `Seaborn` (Visualization)

## 💻 How to Run

1.  Clone this repository using your SSH key:
    ```bash
    git clone git@github.com-personal:erdemhasbek/projelerim.git
    ```
2.  Install the required dependencies:
    ```bash
    pip install pandas seaborn scikit-learn matplotlib
    ```
3.  Launch the Jupyter Notebook:
    ```bash
    jupyter notebook IrisClassificationAnalysis.ipynb
    ```

## 📝 Author

**Erdem Hasbek**
*Artificial Intelligence and Data Engineering Student*
**Istanbul Technical University (ITU)**

---
*Developed for educational purposes in the field of AI and Data Science.*