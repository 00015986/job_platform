from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    ROLE_CHOICES = (
        ('applicant', 'Applicant'),
        ('recruiter', 'Recruiter'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    email = forms.EmailInput()

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.save()
        return user

    def save(self, request):
        user = super().save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user


# class CustomSignupForm(SignupForm):
# def __init__(self, *args, **kwargs):
#     super(CustomSignupForm, self).__init__(*args, **kwargs)
#     for visible_field in self.visible_fields():
#         if isinstance(visible_field.field, forms.fields.BooleanField):
#             visible_field.field.widget.attrs['class'] = 'form-check-input'
#         else:
#             visible_field.field.widget.attrs['class'] = 'form-control'


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            if isinstance(visible_field.field, forms.fields.BooleanField):
                visible_field.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible_field.field.widget.attrs['class'] = 'form-control'

