# Import main library
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import joblib

# Import Flask modules
from flask import Flask, request, render_template

# Import pickle to save our regression model
import pickle 

# Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder = 'templates')

# Open our model 
model = pickle.load(open('redwine_model.pkl','rb'))

# Create our "home" route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

# Set a post method to yield predictions on page
@app.route('/predict',methods=['POST','GET'])   
def predict():
    
    if request.method == 'POST':
       try:  
        input1 = float(request.form["input1"])
        input2 = float(request.form["input2"])
        input3 = float(request.form["input3"])
        input4 = float(request.form["input4"])
        input5 = float(request.form["input5"])
        input6 = float(request.form["input6"])
        input7 = float(request.form["input7"])
        input8 = float(request.form["input8"])
        input9 = float(request.form["input9"])
        input10 = float(request.form["input10"])
        input11 = float(request.form["input11"])
        
        features = [[input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11]]
        print(features)
        
        # Load into app.py
        scaler = joblib.load(scaler.save) 
        scaled_features = scaler.fit_transform(features)
        
        prediction = model.predict(scaled_features)
        f"Prediction is {prediction}"
    
        if prediction[0]=="5":
            print("wine low quality")
            return render_template('index.html',
                               prediction_text='Wine is of LOW Quality!'
                               )
        elif prediction[0]=="6":
            return render_template('index.html',
                               prediction_text='Wine is of MEDIUM quality!'
                               )                          
        else:
            return render_template('index.html',
                               prediction_text='Wine is of HIGH quality!'
                              )
            
       except Exception as e:
        print('The Exception message is: ')
        return "Something is Wrong, Please enter all the features."
     
    else:
        return render_template('index.html')
    
@app.route('/uploadfile',methods=['POST','GET'])
def uploadfile():
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)