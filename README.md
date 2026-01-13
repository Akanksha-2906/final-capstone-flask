Project – Flask ML Application
   The app predicts salary based on experience, projects, and certifications using a trained ML model.

Objectives
    Train and load an ML model
    Expose prediction functionality via Flask
    Demonstrate Git & GitHub usage

Features
    Flask web application
    Machine Learning model training
    REST API for predictions
    JSON-based input/output
    Modular project structure
    Ready for deployment

Tech Stack
    Programming Language: Python 3.10+
    Framework: Flask
    ML Library: Scikit-learn
    Data Handling: Pandas, NumPy
    Version Control: Git & GitHub

Project Structure
    
    final_capstone/
    │── app.py
    │── requirements.txt
    │── README.md
    │
    ├── ml/
    │   ├── train_model.py
    │   ├── model.pkl
    │   └── dataset.csv
    │
    ├── templates/
    │   └── index.html
    │
    └── static/

How to Run the Project (Step-by-Step)
1. Clone the Repository
git clone https://github.com/Akanksha-2906/final-capstone-flask
cd final-capstone-flask

2. Install Dependencies
pip install -r requirements.txt

3. Train the Machine Learning Model
cd ml
python train_model.py [This will generate model.pkl]

4. Run the Flask Application
cd ..
python app.py

5. Open in Browser
http://127.0.0.1:5000

Prediction API Usage
    Endpoint
    POST /predict
        Request Format (JSON)
        {
        "experience": 5,
        "projects": 7,
        "certifications": 2
        }

        Response Format
        {
        "predicted_salary": 60000
        }


[Note: /predict only supports POST requests.]

Machine Learning Details
    Model Type: Logistic / Regression Model
    Features Used: Experience, Projects, Certifications
    Target Variable: Salary
    Dataset: Custom CSV (small demo dataset)

Challenges Faced
    Missing model.pkl file
    GitHub merge conflicts
    HTTP method issues (GET vs POST)

(All issues were resolved during development.)