from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})}


class EmailSendForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	to = forms.CharField()
	comments = forms.CharField(required=False,widget=forms.Textarea)




