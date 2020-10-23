from django import forms
from .models import ProductModel

class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = ('title', 'description', 'price', 'discount', 'quantity', 'available', 'category')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'price': 'Price(in Rs.)',
            'discount': 'Discount(in %)',
            'quantity': 'Quantity',
            'available': 'Available',
            'category': 'Category'
        }

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*awgs, **kwargs)
            self.fields['category'].empty_label = 'Select'