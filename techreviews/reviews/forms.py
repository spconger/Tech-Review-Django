from django import forms
from .models import TechProduct, TechReview

class TechProductForm(forms.ModelForm):
    class Meta:
        model=TechProduct
        fields='__all__'

class TechReviewForm(forms.ModelForm):
    class Meta:
        model=TechReview
        fields='__all__'