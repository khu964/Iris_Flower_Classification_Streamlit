import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import streamlit as st

# =========================
# Title
# =========================
st.title(" Iris Flower Species Prediction")

st.markdown("""
### About Project
This app predicts Iris flower species using Machine Learning and Streamlit.
""")

# =========================
# Load Dataset
# =========================
df = pd.read_csv("IRIS.csv")

# =========================
# Show Dataset
# =========================
if st.checkbox(" Show Dataset"):
    st.dataframe(df)

# =========================
# Show Statistics
# =========================
if st.checkbox("Show Statistics"):
    st.write(df.describe())

# =========================
# Sidebar Inputs
# =========================
st.sidebar.title(" Flower Measurements")

sepal_length = st.sidebar.slider(
    "Sepal Length (cm)", 4.0, 8.0, 5.1
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)", 2.0, 4.5, 3.5
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)", 1.0, 6.9, 1.4
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)", 0.1, 2.5, 0.2
)

# =========================
# Features and Target
# =========================
X = df[['sepal_length', 'sepal_width',
        'petal_length', 'petal_width']]

y = df['species']

# =========================
# Train-Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# Train Model
# =========================
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# =========================
# Model Accuracy
# =========================
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

st.success(f" Model Accuracy: {accuracy:.2%}")

# =========================
# Prediction
# =========================
features = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

if st.button(" Predict Species"):

    prediction = model.predict(features)

    st.success(
        f" Predicted Iris Species: {prediction[0]}"
    )

    if prediction[0] == "Iris-setosa":

        st.image(
            "setosa.jpg",
            caption="Iris Setosa"
        )

        st.info(
            "Setosa is a small flower with short petals and sepals."
        )

    elif prediction[0] == "Iris-versicolor":

        st.image(
            "versicolor.jpg",
            caption="Iris Versicolor"
        )

        st.info(
            "Versicolor is a medium-sized flower with moderate petals and sepals."
        )

    elif prediction[0] == "Iris-virginica":

        st.image(
            "virginica.jpg",
            caption="Iris Virginica"
        )

        st.info(
            "Virginica is a larger flower with long petals and sepals."
        )

st.snow()
