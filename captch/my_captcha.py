from django import forms
from captcha.fields import ReCaptchaField

# You Can Give Any Name For file.

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()
