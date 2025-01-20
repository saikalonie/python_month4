from django import forms
from posts.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["image", "title", "description"]

# class PostCreateForm(forms.Form):
#     image = forms.ImageField(required=False)
#     title = forms.CharField(max_length=100, required=True)
#     description = forms.CharField(max_length=256, required=True)


    def clean(self):
        cleaned_data = super().clean()
        """cleaned_data = {'title': 'title', ...}"""
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        if (title and description) and title.lower() == description.lower():
            raise forms.ValidationError("Title and description should be different")
        return cleaned_data

