from django import forms
from django.core import validators

def check_for_v(value):
    if value[0].lower() != 'v':
        raise forms.ValidationError('Need to start name with "V"')

class Base(forms.Form):
    name = forms.CharField(validators=[check_for_v])
    email = forms.EmailField(label='Email')
    verify_email = forms.EmailField(label='Verfiy Email')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # function name should be same as name of input varriable
    def clean_verify_email(self):
        all_clean_data = super().clean()
        print(all_clean_data)
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError("Emails don't match")

    """
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('GOTCHA BOT!')
        return botcatcher
    """
