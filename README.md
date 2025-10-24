# TestRepository

# flask_app

このプロジェクトは入力した文字の表示を次ページで行う簡易Flaskアプリです。

## 必要環境
- Python 3.10 以上

## 起動手順（ローカル）
Windows:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set FLASK_APP=app.py
python -m flask run

ブラウザで http://127.0.0.1:5000 を開くと動作確認できます。

## 今日の作業（2025-10-24）

### 概要
入門リハ：プロジェクトの起動確認とテンプレート基盤の追加を行いました。主にローカル起動手順の整備、ベーステンプレートと簡易スタイルの追加、フォーム送受信のエンドポイントを実装しました。

### 本日の作業内容（重要ポイント）
- ローカルでアプリを起動して動作確認（`python -m flask run`）。ブラウザでトップページ・CSS・フォーム送信の確認を実施。
- `templates/base.html`, `templates/index.html`, `templates/result.html`, `static/style.css` を追加して共通レイアウトを作成。
- `requirements.txt` と `.gitignore` を追加し、`__pycache__/` と `*.pyc` を無視するよう設定。
- 変更は PR（#1）を作成して main にマージ済み。

### 実行（短縮版）
1. 仮想環境を作成・有効化:
   - Git Bash:
     ```bash
     python -m venv venv
     source venv/Scripts/activate
     ```
2. 依存をインストール:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt

##重要なコミット（抜粋）
- 初期プッシュ: https://github.com/KEIGO511/TestRepository/commit/a08aa49
- app.py 更新: https://github.com/KEIGO511/TestRepository/commit/c9b56d1
- base/template・CSS 等の追加（PR マージ）: fea99b7（マージ済み）
- （参考）PR: https://github.com/KEIGO511/TestRepository/pull/1
- ※ コミットハッシュは git rev-parse --short <hash> で参照できます。特定コミットへのリンクは https://github.com/<ユー>/<repo>/commit/<hash> の形になります。

###問題点・対処
- 一時的に __pycache__/ がリポジトリに混入しました。リポジトリ側の追跡は解除済み（.gitignore を追加）。ローカルのキャッシュは任意で削除してください (rm -rf __pycache__)。
   
