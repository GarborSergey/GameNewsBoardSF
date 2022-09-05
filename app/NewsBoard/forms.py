from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from captcha.fields import CaptchaField

from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    captcha = CaptchaField()

    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'content',
        ]
