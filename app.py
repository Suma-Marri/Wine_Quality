# Import main library
import numpy as np

# Import Flask modules
from flask import Flask, request, render_template

# Import pickle to save our regression model
import pickle 

# Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder = 'templates')

# Open our model 
model = pickle.load(open('model.pkl','rb'))

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
        
        
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        
        prediction = model.predict(final_features)
        print(f"Prediction is {prediction}")
    
        if prediction[0]=="1":
            print("wine low quality")
            return render_template('index.html',
                               prediction_text='Wine is of LOW Quality!'
                               )
        elif prediction[0]=="2":
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