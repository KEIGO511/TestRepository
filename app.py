from flask import Flask, render_template, request, redirect, url_for,flash

app = Flask(__name__)
app.secret_key = "dev-secret"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# submit エンドポイントを定義（POST を受ける）
@app.route("/submit", methods=["POST"])
def submit():
    text = (request.form.get("text") or "").strip()
    errors = []
    if not text:
        errors.append("テキストは必須です。")
    elif len(text) > 200:
        errors.append("テキストは200文字以内にしてください。")
        
    if errors:
        for e in errors:
            flash(e)
        return redirect(url_for("index"))
    
    # 正常処理（例: 結果ページへ）
    return render_template("result.html", text=text)
    