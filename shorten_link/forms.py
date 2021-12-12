from captcha.fields import CaptchaField
from django.forms import ModelForm

from .models import Link


class LinkForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Link
        fields = "__all__"
