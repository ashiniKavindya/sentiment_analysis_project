from flask import Flask, redirect,render_template,request
from helper import preprocessing,vectorizer,get_prediction 
from logger import logging
app = Flask(__name__)

logging.info("App started")

data=dict()
reviews='nothing'
data['input']=''


@app.route("/")
def index():
    data['reviews']=reviews
    data['input']=''
    logging.info("Rendering Home Page")
    return render_template('index.html',data=data)

@app.route("/",methods=['POST'])
def my_post():
    text=request.form['text']
    
    preprocessed_text=preprocessing(text)
    logging.info("Preprocessed text: %s", preprocessed_text)
    vectorized_text=vectorizer(preprocessed_text)
    logging.info("Vectorized text: %s", vectorized_text)
    prediction=get_prediction(vectorized_text)
    logging.info("Prediction: %s", prediction)
    if prediction=='positive':
        data['reviews']='positive'
 
    else:
        data['reviews']='negative'
    data['input']=text
    print(data['reviews'])
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(debug=True)