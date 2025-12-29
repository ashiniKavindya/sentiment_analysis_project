from flask import Flask, redirect,render_template,request
from helper import preprocessing,vectorizer,get_prediction 
app = Flask(__name__)

data=dict()
reviews='nothing'
data['input']=''


@app.route("/")
def index():
    data['reviews']=reviews
    data['input']=''

    return render_template('index.html',data=data)

@app.route("/",methods=['POST'])
def my_post():
    text=request.form['text']
    
    preprocessed_text=preprocessing(text)
    vectorized_text=vectorizer(preprocessed_text)
    prediction=get_prediction(vectorized_text)
    if prediction=='positive':
        data['reviews']='positive'
 
    else:
        data['reviews']='negative'
    data['input']=text
    print(data['reviews'])
    return render_template('index.html',data=data)

if __name__ == "__main__":
    app.run(debug=True)