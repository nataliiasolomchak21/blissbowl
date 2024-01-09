from django import forms
from .widgets import CustomClearableFileInput

from .models import Product, Category
from .models import Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        # Use a list of tuples directly from the Category model
        self.fields["category"].choices = [(c.id, str(c)) for c in categories]

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {"text": forms.Textarea(attrs={"rows": 3})}
