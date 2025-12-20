from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Email Address')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    
    class Meta:
        fields = ['name', 'email', 'message']