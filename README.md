## Description 
This repository contains an Exploratory Data Analysis (EDA) and modeling approach for exoplanet transit detection using a dataset of Kepler Objects of Interest (KOIs). The dataset includes various features related to exoplanet properties and their disposition status.

The goals of this project are as follows:
- Understand the dataset through EDA to identify patterns, trends, and relationships.
- Develop and evaluate machine learning models using MATLAB to predict exoplanet dispositions.
- Visualize key insights from the data and model results.

## Dataset 
The dataset consists of 50 columns with information such as period, duration, impact, planetary radius, temperature, and more for each Kepler Object of Interest (KOI). The target variable is the "koi_disposition," which indicates whether an object is a confirmed exoplanet, false positive, or candidate.

The Kepler Exoplanet Search Results dataset contains over 10,000 rows of data on exoplanet candidates discovered by NASA's Kepler spacecraft. Our model uses this data to predict whether a given signal is a transit of an exoplanet across its host star.

You can get the dataset from here [Kepler Exoplanet Search Results](https://www.kaggle.com/datasets/nasa/kepler-exoplanet-search-results)

## Approach

1. **Data Preprocessing**: Handle missing values, clean the dataset, and prepare features for analysis.
2. **Exploratory Data Analysis**: Gain insights into the dataset through various visualizations and statistical analysis.
3. **Machine Learning Modeling**: Utilize MATLAB to develop machine learning models (e.g., decision trees, SVMs) for exoplanet disposition prediction.
4. **Model Evaluation**: Assess model performance using appropriate metrics (e.g., accuracy, precision, recall).
5. **Visualization**: Create visualizations to present key findings from EDA and model results.

## Visualizations

A variety of visualizations were generated to explore the dataset and showcase insights:

- Histograms and KDEs for feature distributions.
- Box plots and violin plots to compare features by disposition.
- Pair plots and scatter plots to visualize relationships.
- Correlation heatmaps with dendrograms.
- Interactive plots using Plotly for dynamic exploration.

## Plots 
Logistic Regression - 

![ROC - Logistic regression](https://github.com/wittyicon29/Exo-Transit-Regression/assets/99320225/f4dad2e2-b05f-4c8d-9680-88688da494ef)

Random Forest -

![ROC - RF](https://github.com/wittyicon29/Exo-Transit-Regression/assets/99320225/af5313ea-043e-43c2-b78b-d37997b24fac)

SVM -

![ROC - SVM](https://github.com/wittyicon29/Exo-Transit-Regression/assets/99320225/42266557-83b6-434a-bb2e-f7c7c0b60396)

MLP -

![ROC - MLP](https://github.com/wittyicon29/Exo-Transit-Regression/assets/99320225/4ab9e86d-c5bb-44e9-a4ea-22aab7455320)


Mesh Plot Normalizaed Features - 

![Normalized Features](https://github.com/wittyicon29/Exo-Transit-Regression/assets/99320225/67cc442f-6e53-4d8c-8740-ecbaaccf26a6)

## Usage

1. Clone this repository:
   ```sh
   git clone https://github.com/wittyicon29/Exo-Transit-Regression.git
   ```
2. Navigate to the repository:
   ```sh
   cd Exo Transit Regression
   ```
3. Install the required dependencies
4. Run the MATLAB scripts for data preprocessing, EDA, and modeling.
5. Explore the generated visualizations in the "Visualizations" folder.
6. Modify the code and analysis as needed for your specific research questions.

##
License
This project is licensed under the MIT License.
Feel free to contribute, provide feedback, and share your findings!
