from django import forms
from django.core import validators
from AppTwoWithModelForm.models import myModel

class myModelForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
    # No need to declare field here if you've done in models and don't want to manuplate
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    conf_email = forms.EmailField(label='Confirm Email', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta():
        model = myModel
        fields = ['name', 'email']
        # fields = '__all__'
        #exclude = ['botcatcher']

    def clean(self):
        clean_all = super().clean()
        email = clean_all['email']
        conf_email = clean_all['conf_email']
        if email != conf_email:
            raise forms.ValidationError('Email Id Mismatch!')
