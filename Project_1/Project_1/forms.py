from django import forms

class usersForm(forms.Form):
    fname=forms.CharField(
        label="First Name",
        required=False,
        widget=forms.TextInput(
            attrs={'class':"form-control"}
            ))
    lname=forms.CharField(label="Last Name",widget=forms.TextInput())
    email=forms.EmailField(label="Email")