
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'ca'
loaded_model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        glucose = float(request.form['glucose'])
        BMI = float(request.form['BMI'])
        diaBP = float(request.form['diaBP'])
        sysBP = float(request.form['sysBP'])
        cigsPerDay = float(request.form['cigsPerDay'])
        totChol = float(request.form['totChol'])
        
        data = np.array([[age,glucose,BMI,diaBP,sysBP,cigsPerDay,totChol]])
        my_prediction = loaded_model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

        
        

if __name__ == '__main__':
	app.run(debug=True)