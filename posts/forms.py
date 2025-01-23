from django import forms
from posts.models import Post
from posts.models import  Category


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

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,
                             required=False,
                             widget=forms.TextInput(attrs={"placeholder": "Search"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      required=False,
                                      widget=forms.Select())
    orderings =(
        ("created_at", "дата создания"),
        ("-created_at", "дата создания(по убыванию)"),

        ("updated_at", "дата обновления" ),
        ("-updated_at", "дата обновления(по убыванию)"),

        ("rate", "рейтинг"),
        ("-rate", "рейтинг(по убыванию)"),
    )
    ordering = forms.ChoiceField(
        choices=orderings, required=False, widget=forms.Select()
    )

