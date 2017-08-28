"""Building forms."""

from django import forms
from .models import GuestUser
from django.contrib.auth.hashers import check_password


class NewPostForm(forms.Form):
    """New post for user authenticated."""

    PostTitle = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'Title'}), required=True)
    PostImageURL = forms.URLField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'http://www.yourdomain.com/example.jpg'}),
        required=True)
    PostText = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Post content'}), required=True)
    PostVisible = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'switch-input'}), required=True)


class RegisterForm(forms.Form):
    """Register guests in the database."""

    FirstName = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'First name'}), required=True)
    LastName = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'placeholder': 'Last name'}), required=True)
    Email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'email@example.com'}), required=True)
    Password = forms.CharField(
        max_length=250, widget=forms.PasswordInput, required=True)
    VerifyPassword = forms.CharField(
        max_length=250, widget=forms.PasswordInput, required=True)
    TermAgree = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'switch-input'}), required=True)

    def clean(self):
        """Validate the new guest user."""
        email = self.cleaned_data['Email']
        model_ = GuestUser

        try:
            model_ = GuestUser.objects.get(
                Email=email)
            if model_:
                raise forms.ValidationError(
                    "This e-mail already exist in our database.")
        except model_.DoesNotExist:
            password = self.cleaned_data['Password']
            password_confirm = self.cleaned_data.get('VerifyPassword')

            if password and password_confirm:
                if password != password_confirm:
                    raise forms.ValidationError(
                        "The two password fields must match.")

        return self.cleaned_data


class LoginForm(forms.Form):
    """Login guest users checking the database."""

    Email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'email@example.com'}), required=True)
    Password = forms.CharField(
        max_length=250, widget=forms.PasswordInput, required=True)
    RememberMe = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'switch-input'}), required=False)

    def clean(self):
        """Validate if the password matches."""
        email = self.cleaned_data['Email']
        nohash_password = self.cleaned_data['Password']
        model_ = GuestUser

        if nohash_password:
            try:
                model_ = GuestUser.objects.get(
                    Email=email)
                if not check_password(nohash_password, model_.Password):
                    raise forms.ValidationError(
                        "Sorry, your password is wrong.")

            except model_.DoesNotExist:
                raise forms.ValidationError(
                    "No guest user was found with this e-mail.")
            except model_.MultipleObjectsReturned:
                raise forms.ValidationError(
                    "Something wrong with your login.")

        return self.cleaned_data


class CommentForm(forms.Form):
    """Comment a post."""

    CommentText = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Leave your comment about our post'}),
        required=True)
