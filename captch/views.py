from django.shortcuts import render
from .my_captcha import FormWithCaptcha


# Create your views here.
def home(request):
    context = {
        'captcha': FormWithCaptcha,
    }
    return render(request, 'captch/index.html', context)
