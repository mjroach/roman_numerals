from django import forms

class IntergerForm(forms.Form):
    input = forms.IntegerField(max_value=3999, min_value=1)