from flask import Flask, render_template, request, redirect, url_for,flash
from forms import UserInfoForm
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = "dev-secret"   # 本番では環境変数で管理すること
csrf = CSRFProtect(app)

# submit エンドポイントを定義（POST を受ける）
@app.route("/", methods=['GET','POST'])
def index():
    form = UserInfoForm(request.form)
    if request.method == 'POST':
        return render_template('result.html',form=form)
    
    # 正常処理（例: 結果ページへ）
    if request.method == 'GET':
        return render_template("index.html", form=form)
    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
    