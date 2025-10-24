from flask import Flask,render_template,request,redirect,url_for
import os

app = Flask(__name__)

def predict_with_ai(text):
    return text[::-1]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    user_text = request.form.get('text','')
    if not user_text:
        return redirect(url_for('index'))
    result = predict_with_ai(user_text)
    return render_template('index.html',input_text=user_text,output_text=result)

if __name__=='__main__':
    app.run(debug=True)
    