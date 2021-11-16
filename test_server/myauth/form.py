from djano.forms import ModelForm


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']