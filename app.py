from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# submit エンドポイントを定義（POST を受ける）
@app.route("/submit", methods=["POST"])
def submit():
    text = request.form.get("text", "")
    # ここで何か処理する（例：そのまま結果ページに渡す）
    return render_template("result.html", text=text)
    