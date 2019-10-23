from django import forms

class ContactForm(forms.Form):
    Name=forms.CharField(min_length=4,max_length=40,required=True,label="Name")
    Email=forms.EmailField(min_length=5,max_length=100,required=True,label="Email")
    Phno=forms.CharField(max_length=10,min_length=10,required=True)
    Commment=forms.CharField(widget=forms.Textarea)
    Gender=forms.ChoiceField(choices=(('Male','Male'),\
        ('Female','Female')),widget=forms.RadioSelect)
    Password=forms.CharField(min_length=4,max_length=10,widget=forms.PasswordInput)