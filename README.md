Iris Species Predictor Web App

A simple and interactive Flask web application that predicts the species of an Iris flower based on user-provided measurements (sepal length, sepal width, petal length, petal width). This app uses a pre-trained machine learning model and label encoder to make real-time predictions through a browser form.

* Project Overview

The app loads a pickled scikit-learn model and label encoder, takes four float inputs from a web form, and shows the predicted species on the same page using HTML templates. This makes it easy to test and visualize the model’s output in a browser.

* Features

✔️ Input form to enter Iris flower measurements
✔️ Uses a trained ML model (pickle file) to predict species
✔️ Shows prediction results on the same page
✔️ Clean Flask structure with templates

* Project Structure
iris_flask_app/
├── templates/
│   └── index.html
├── iris_model.pkl
├── label_encoder.pkl
├── app.py
├── requirements.txt
└── README.md

* Installation

Clone the repository

git clone https://github.com/yourusername/iris-flask-app.git
cd iris-flask-app


Create & activate a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

* Running the App

Start the Flask development server:

python app.py


Open your browser and go to:

http://127.0.0.1:5001/


Fill in the flower measurements and submit to see the predicted species.

* How It Works

The app imports the saved model and label encoder via pickle.load.

The user enters values into a form in index.html.

Flask receives these values via POST on the / route.

The model predicts the class, and the label encoder decodes it to the species name.

The prediction result is rendered back into the form page.

* Models Used

Machine Learning model (iris_model.pkl)

Label encoder (label_encoder.pkl) to map numeric classes to species names

Both are loaded at app startup.

* Dependencies

List of packages required:

Flask
numpy
scikit-learn


Install them via:

pip install Flask numpy scikit-learn


Or via the requirements.txt:

pip install -r requirements.txt

*Example: Using the App

Once the server is running:

Enter:

Sepal Length: 5.1

Sepal Width: 3.5

Petal Length: 1.4

Petal Width: 0.2

The app will display:

Predicted Species: setosa

*Tips

Run with debug=True in development for live reloading.

Consider deploying with a proper WSGI server (like Gunicorn) for production.
This project is open for modification and reuse.

If you’d like, I can also generate a sample index.html that matches your Flask fo
