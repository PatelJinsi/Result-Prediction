from flask import Flask ,request, jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return "Result prediction api running"

@app.route('/predict', methods=['POST'])
def predict():
    data=request.json
    features=[[
        data['last grade'],
        data['study hours'],
    ]]
    
    prediction=model.predict(features)[0]
    return jsonify({
        "prediction" :int(prediction)
    })
    
import os
if __name__=="__main__" :
    port = int(os.environ.get('PORT',4000))
    app.run(host= '0.0.0.0', port=port)