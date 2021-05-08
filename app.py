import numpy as np
from flask import Flask, render_template,request
import pickle 

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of web-app
@app.route('/')
def home():
    return render_template('index.html')

#To run the predict button in the web-app
@app.route('/predict', methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = np.round(prediction[0], 2)
    return render_template('index.html', prediction_text='Predicted NBA Salary: ${}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)