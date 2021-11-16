# is valid_user
# is valid_token
# new_user
# update_user
# delete_user
from djnago.views.generic import CreateView, UpdateView, DeleteView

class UserCreateView(CreateView):
    model = User
    template_name = "create_user.html"

    def form_valid(self, form):
        form.email = form.cleaned_data['email']
        form.password = form.cleaned_data['password']
        return super().form_valid(form)
