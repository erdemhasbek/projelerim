# 🏀 EuroLeague Live Data Analytics & Scouting Dashboard

This project is a comprehensive data analysis tool that fetches live basketball data from the **Official EuroLeague API**. It processes team performance metrics, compares top teams with league averages, and provides data-driven scouting recommendations.

---

## 🚀 Project Overview

The goal of this project is to transform raw API data into actionable insights for basketball analysts and scouts. The pipeline performs the following:
1.  **Data Extraction:** Fetches real-time game data using REST API.
2.  **Data Engineering:** Cleans and processes raw JSON data into structured Pandas DataFrames.
3.  **Performance Metrics:** Calculates points scored, points conceded, 2PT/3PT distributions, and fastbreak efficiency.
4.  **Competitive Analysis:** Compares specific teams (e.g., Fenerbahçe and Anadolu Efes) against the league bests and averages.
5.  **Smart Scouting:** Suggests high-potential shooters based on 3-point efficiency metrics.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** * `Pandas`: For heavy-duty data manipulation.
    * `Matplotlib`: For high-quality performance visualizations.
    * `Requests`: For API communication.
    * `Numpy`: For mathematical operations.

## 📊 Key Features

### 1. Automated Data Pipeline
The system handles API requests with built-in error handling and request throttling to ensure stable data collection across multiple game codes.

### 2. Performance Comparison Chart
Generates a multi-bar chart comparing:
- **Offensive Power** (Scoring)
- **Defensive Strength** (Points Conceded)
- **Shot Selection** (2PT vs 3PT)
- **Transition Game** (Fastbreak points)

### 3. Scouting & Recruitment Logic
The `get_shooter_recommendations` function acts as a mini-scout. It analyzes player-based data to identify the most efficient 3-point shooters outside of the current team roster.

## 💻 How to Run

1.  Clone this repository using the personal SSH key:
    ```bash
    git clone git@github.com-personal:erdemhasbek/projelerim.git
    ```
2.  Install required libraries:
    ```bash
    pip install pandas matplotlib requests
    ```
3.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook EuroLeagueLiveDataAnalytics.ipynb
    ```

## 📝 Author

**Erdem Hasbek** *Istanbul Technical University (ITU)* *Artificial Intelligence and Data Engineering Student* ---
*Disclaimer: This project is developed for educational and analytical purposes using public API endpoints.*
