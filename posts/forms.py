from django import forms
from posts.models import Post, Group

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text',)

    def check_text(self):
        checked_text = self.cleaned_data['text']
        if checked_text is None:
            raise forms.ValidationError("Пост должен содержать текст")
        return checked_text


