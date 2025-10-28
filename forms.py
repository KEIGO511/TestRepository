from wtforms import Form
from wtforms.fields import(
    StringField, IntegerField, PasswordField, DateField,
    RadioField, SelectField, BooleanField, TextAreaField,
    EmailField, SubmitField
)

class UserInfoForm(Form):
    name = StringField('名前：',render_kw={"placeholder":"（例）フラスク太郎"})
    age = IntegerField('年齢：',default=20)
    password = PasswordField('パスワード；')
    confirm_password = PasswordField('パスワード確認： ')
    email = EmailField('メールアドレス： ')
    birthday = DateField('生年月日：',format="%Y-%m-%d",render_kw={"placeholder":"yyyy/mm/dd"})
    gender = RadioField('性別：',choices=[('man','男性'),('woman','女性')],default='man')
    submit = SubmitField('送信')