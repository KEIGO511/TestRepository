from flask import Flask,render_template,request,redirect,url_for
import os

app = Flask(__name__)

#入力テキストを逆順にする
def predict_with_ai(text):
    return text[::-1]

@app.route('/')
def index():
    return render_template('index.html')

#送信ボタンを押す
@app.route('/predict',methods=['POST'])

def predict():
    #テキストのあるなしの感知
    user_text = request.form.get('text','')
    #テキストがあるかどうかの分岐
    if not user_text:
        return redirect(url_for('index'))
    result = predict_with_ai(user_text)
    return render_template('index.html',input_text=user_text,output_text=result)

if __name__=='__main__':
    app.run(debug=True)
    