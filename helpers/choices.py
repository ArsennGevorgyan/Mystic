from users import forms


class MyForm(forms.Form):
    my_field = forms.ChoiceField(choices=[('', 'Select an option'), ('1', 'Option 1'), ('2', 'Option 2')])
