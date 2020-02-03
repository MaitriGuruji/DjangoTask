from django import forms
from .models import UsrReg,User,UsrPost,Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm,PasswordChangeForm


class ChangeForm(UserChangeForm):
    password = forms.CharField(label='',widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model= User
        fields = ('username','image','first_name','last_name','phone_no','password')

    def __init__(self, *args, **kwargs):
        super(ChangeForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['phone_no'].label = ''

        self.fields['username'].widget.attrs['type'] = 'email'
        self.fields['image'].widget.attrs['type'] = 'image'
        self.fields['first_name'].widget.attrs['type'] = 'text'
        self.fields['last_name'].widget.attrs['type'] = 'text'
        self.fields['phone_no'].widget.attrs['type'] = 'text'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_no'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['image'].widget.attrs['id'] = 'image'
        self.fields['first_name'].widget.attrs['id'] = 'fname'
        self.fields['last_name'].widget.attrs['id'] = 'lname'
        self.fields['phone_no'].widget.attrs['id'] = 'phone_no'

class ChangePass(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePass, self).__init__(*args, **kwargs)

        # self.fields['username'].label = ''
        self.fields['old_password'].label = ''
        self.fields['new_password1'].label = ''
        self.fields['new_password2'].label = ''

        # self.fields['username'].widget.attrs['type'] = 'email'
        self.fields['old_password'].widget.attrs['type'] = 'password'
        self.fields['new_password1'].widget.attrs['type'] = 'password'
        self.fields['new_password2'].widget.attrs['type'] = 'password'

        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'

        # self.fields['username'].widget.attrs['id'] = 'username'
        self.fields['old_password'].widget.attrs['id'] = 'password'
        self.fields['new_password1'].widget.attrs['id'] = 'password1'
        self.fields['new_password2'].widget.attrs['id'] = 'password2'

        self.fields['old_password'].widget.attrs['placeholder'] = 'Enter Old Password'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter New Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'


class AuthForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['password'].label = ''

        self.fields['username'].widget.attrs['class']= 'fadeIn second'
        self.fields['password'].widget.attrs['class'] = 'fadeIn second'

        self.fields['username'].widget.attrs['id'] = 'login'
        self.fields['password'].widget.attrs['id'] = 'password'

        self.fields['username'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'

class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields = ('username','first_name','last_name','phone_no', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            # self.fields['password1'].help_text = '<small><li style="color:Gray; list-style-type:none;">Can not be a commonly used.<li style="color:Gray; list-style-type:none;">At least 8 character not entirely numeric.</small>'
            self.fields['password1'].help_text = ''
            self.fields['password2'].help_text =''

            self.fields['username'].label = ''
            self.fields['first_name'].label = ''
            self.fields['last_name'].label = ''
            # self.fields['email'].label = ''
            self.fields['phone_no'].label = ''
            self.fields['password1'].label = ''
            self.fields['password2'].label = ''

            self.fields['username'].widget.attrs['type'] = 'email'
            self.fields['first_name'].widget.attrs['type'] = 'text'
            self.fields['last_name'].widget.attrs['type'] = 'text'
            # self.fields['email'].widget.attrs['type'] = 'email'
            self.fields['phone_no'].widget.attrs['type'] = 'text'
            self.fields['password1'].widget.attrs['type'] = 'password'
            self.fields['password2'].widget.attrs['type'] = 'password'


            self.fields['username'].widget.attrs['class']= 'fadeIn first'
            self.fields['first_name'].widget.attrs['class']= 'fadeIn second'
            self.fields['last_name'].widget.attrs['class']= 'fadeIn third'
            # self.fields['email'].widget.attrs['class'] = 'fadeIn fourth'
            self.fields['phone_no'].widget.attrs['class']= 'fadeIn fifth'
            self.fields['password1'].widget.attrs['class'] = 'fadeIn sixth'
            self.fields['password2'].widget.attrs['class'] = 'fadeIn seventh'

            self.fields['username'].widget.attrs['id'] = 'username'
            self.fields['first_name'].widget.attrs['id'] = 'fname'
            self.fields['last_name'].widget.attrs['id'] = 'lname'
            # self.fields['email'].widget.attrs['id'] = 'email'
            self.fields['phone_no'].widget.attrs['id'] = 'phone_no'
            self.fields['password1'].widget.attrs['id'] = 'password1'
            self.fields['password2'].widget.attrs['id'] = 'password2'

            self.fields['username'].widget.attrs['placeholder'] = 'Enter Email'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
            # self.fields['email'].widget.attrs['placeholder'] = 'Confirm Email'
            self.fields['phone_no'].widget.attrs['placeholder'] = 'Enter Phone No'
            self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
            self.fields['password2'].widget.attrs['placeholder'] = 'Enter confirm Password'


class PostForm(forms.ModelForm):
    class Meta:
        model = UsrPost
        fields = ('title','content')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].label = ''
        self.fields['content'].label = ''

        self.fields['title'].widget.attrs['type'] = 'text'
        self.fields['content'].widget.attrs['type'] = 'text'

        self.fields['title'].widget.attrs['class']= 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['id'] = 'title'
        self.fields['content'].widget.attrs['id'] = 'content'

        self.fields['title'].widget.attrs['placeholder'] = 'Enter title'
        self.fields['content'].widget.attrs['placeholder'] = 'Enter Content'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['text'].label = ''
        self.fields['text'].widget.attrs['type'] = 'text'
        self.fields['text'].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget.attrs['id'] = 'title'
        self.fields['text'].widget.attrs['placeholder'] = 'Enter Comment'


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UsrReg
        fields = ['name','email','password','confirm_password','phone_no']
