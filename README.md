# 🌸 Iris Flower Species Prediction

A simple Machine Learning web application built with Streamlit that predicts the species of an Iris flower based on sepal and petal measurements. The application uses a Random Forest Classifier trained on the Iris dataset and provides an interactive interface for users to make predictions.

## 🚀 Features

* Predict Iris flower species
* Interactive Streamlit user interface
* Sidebar sliders for flower measurements
* Dataset visualization
* Statistical summary of the dataset
* Flower images and descriptions
* Machine Learning model built using Random Forest Classifier

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn

## 📂 Project Structure

```text
Iris_Flower_Prediction/
│
├── app.py
├── iris.csv
├── setosa.jpg
├── versicolor.jpg
├── virginica.jpg
└── README.md
```

## 📊 Dataset

The project uses the famous Iris dataset, which contains measurements of iris flowers:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The target variable is the flower species:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

## ▶️ Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder:

```bash
cd Iris_Flower_Prediction
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

## 🎯 How It Works

1. Enter flower measurements using the sidebar sliders.
2. Click the **Predict Species** button.
3. The trained machine learning model predicts the flower species.
4. The application displays the predicted species along with an image and description.

## 📸 Preview

This application provides an interactive interface where users can explore the dataset and predict Iris flower species in real time.



Aspiring Frontend Developer and Machine Learning Enthusiast.
