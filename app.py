from flask import Flask, render_template, request, redirect, url_for, flash,session
from forms import UserInfoForm
from flask_wtf import CSRFProtect
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = "dev-secret"   # 本番では環境変数で管理すること
csrf = CSRFProtect(app)

# 簡易ログ設定
logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=['GET','POST'])
def index():
    form = UserInfoForm()
    app.logger.debug("Request method: %s", request.method)
    app.logger.debug("Form data: %s", request.form)
    if form.validate_on_submit():
        app.logger.debug("Form validated OK. form.data: %s", form.data)
        # セッションに保存（パスワード等の敏感情報は保存しない）
        session['form_data'] = {
            'name': form.name.data,
            'age': form.age.data,
            'email': form.email.data,
            'birthday': form.birthday.data.isoformat() if form.birthday.data else None,
            'gender': form.gender.data
        }
        return redirect(url_for('result'))
    if request.method == 'POST':
        app.logger.debug("Form validation failed. errors: %s", form.errors)
        flash("フォーム送信に失敗しました。エラーを確認してください。", "danger")
    # 必ず index.html を返す
    return render_template("index.html", form=form)
    # ...existing code...
@app.route("/result")
def result():
    data = session.pop('form_data', None)
    if data is None:
        flash("表示する結果がありません。フォームから送信してください。", "warning")
        return redirect(url_for('index'))
    # result.html に dict を渡す（テンプレート側でキー参照する）
    return render_template("result.html", form=data)
    