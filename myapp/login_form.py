class SignUpForm(forms.ModelForm):
 username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
 password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
 
 class Meta:
  model = SignUp
  fields = ['username','password']