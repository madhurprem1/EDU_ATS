from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# our new form
# class ContactForm(forms.Form):
# 	contact_name   = forms.CharField(required=True)
# 	contact_email  = forms.EmailField(required=True)
# 	# phone  = forms.CharField(required=True)
# 	form_content = forms.CharField(widget=forms.Textarea)

# # the new bit we're adding
# 	def __init__(self, *args, **kwargs):
# 		super(ContactForm, self).__init__(*args, **kwargs)
# 		self.fields['contact_name'].label = "Your name:"
# 		self.fields['contact_email'].label = "Your email:"
# 		self.fields['form_content'].label = "What do you want to say?"    

class ContactForm(forms.Form):
	from_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)	

	# the new bit we're adding
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['from_email'].label ="E - mail  :"
		self.fields['subject'].label = 	 "Subject :"
		self.fields['message'].label =   "Message:"
		
class SignUpForm(UserCreationForm):
	first_name = forms.CharField(required=False, help_text='Optional.')
	last_name = forms.CharField( required=False, help_text='Optional.')
	email = forms.EmailField(help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )    

		# Edit by bryan
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
		self.fields['username'].widget.attrs['style']  = 'width:400px; height:30px;'
		self.fields['first_name'].widget.attrs['style'] = 'width:400px; height:30px;'
		self.fields['last_name'].widget.attrs['style'] = 'width:400px; height:30px;'
		self.fields['email'].widget.attrs['style'] = 'width:400px; height:30px;'
		self.fields['password1'].widget.attrs['style'] = 'width:400px; height:30px;'
		self.fields['password2'].widget.attrs['style'] = 'width:400px; height:30px;'
		self.fields['username'].widget.attrs['placeholder']  = 'username'
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmed Password'
		
		# ## the new bit we're adding
	# def __init__(self, *args, **kwargs):
	# 	super(SignUpForm, self).__init__(*args, **kwargs)
	# 	self.fields['first_name'].label ="First Name"
	# 	self.fields['last_name'].label = "Last Name :"
	# 	self.fields['email'].label =   "E - mail:"
	# 	self.fields['password1'].label =   "password1:"
	# 	self.fields['password2'].label =   "password2:"

