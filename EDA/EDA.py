import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("cumulative.csv")
data

data.head().T

data.info()

data.describe().T

data.isnull().sum()

data.dropna(subset=['koi_disposition'], inplace=True)
data.fillna(0, inplace=True)

plt.figure(figsize=(8, 6))
sns.countplot(x='koi_disposition', data=data)
plt.title("Target Variable Distribution")
plt.show()

sns.pairplot(data, vars=['koi_period', 'koi_duration', 'koi_depth', 'koi_prad', 'koi_teq'])
plt.suptitle("Pair Plot of Numerical Features")
plt.show()

corr_matrix = data.corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='koi_disposition', y='koi_period', data=data)
plt.title("Exoplanet Period by Disposition")
plt.xticks(rotation=45)
plt.show()

selected_features = ['koi_impact', 'koi_duration', 'koi_prad', 'koi_teq']
data[selected_features].hist(bins=20, figsize=(12, 8))
plt.suptitle("Histograms of Selected Features")
plt.show()

numerical_features = data.select_dtypes(include=['float64', 'int64']).columns
for feature in numerical_features:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[feature], bins=20)
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.show()

categorical_features = data.select_dtypes(include=['object']).columns
for feature in categorical_features:
    plt.figure(figsize=(8, 6))
    sns.countplot(x=feature, data=data)
    plt.title(f"Distribution of {feature}")
    plt.xticks(rotation=45)
    plt.show()

for feature in numerical_features:
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='koi_disposition', y=feature, data=data)
    plt.title(f"{feature} Distribution by Disposition")
    plt.xticks(rotation=45)
    plt.show()

selected_features = ['koi_impact', 'koi_prad', 'koi_teq']
pd.plotting.scatter_matrix(data[selected_features], figsize=(12, 12), diagonal='hist')
plt.suptitle("Scatter Matrix of Select Features")
plt.show()

sns.pairplot(data[numerical_features], diag_kind='kde')
plt.suptitle("Pair Plot with KDE")
plt.show()

import plotly.express as px

for feature in numerical_features:
    fig = px.histogram(data, x=feature, color='koi_disposition', title=f"Distribution of {feature} by Disposition")
    fig.show()

for feature in numerical_features:
    fig = px.box(data, x='koi_disposition', y=feature, title=f"{feature} by Disposition")
    fig.show()

fig = px.scatter_3d(data, x='koi_impact', y='koi_prad', z='koi_teq', color='koi_disposition', title="Interactive 3D Scatter Plot")
fig.show()
