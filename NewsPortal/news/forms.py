from django import forms


class ContactAuthor(forms.Form):

    userMail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    userName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
