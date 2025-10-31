from flask_wtf import FlaskForm
from wtforms.fields import(
    StringField, IntegerField, PasswordField, DateField,
    RadioField, SelectField, BooleanField, TextAreaField,
    EmailField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo,NumberRange
)

class UserInfoForm(FlaskForm):
    name = StringField(
        '名前：',
        validators=[DataRequired(message='名前は入力必須です')],
        render_kw={"placeholder":"（例）フラスク太郎"}
        )
    
    age = IntegerField(
        '年齢：',
        validators=[NumberRange(min=18, max=100, message='入力範囲は18歳から100歳です')],
        default=20
        )
    
    password = PasswordField(
        'パスワード；',
        validators=[
            Length(min=1, max=10, message='パスワードの長さは1文字以上10文字以内です'),
            EqualTo('confirm_password',message='確認用パスワードと一致しません')
            ]
        )
    
    confirm_password = PasswordField('パスワード確認： ')
    
    email = EmailField(
        'メールアドレス：',
        validators=[Email(message='有効なメールアドレスを入力してください')]
        )
    
    birthday = DateField(
        '生年月日：',
        validators=[DataRequired(message='生年月日は入力必須です')],
        format="%Y-%m-%d",
        render_kw={"placeholder":"yyyy/mm/dd"}
        )
    
    gender = RadioField('性別：',choices=[('man','男性'),('woman','女性')],default='man')
    
    submit = SubmitField('送信')