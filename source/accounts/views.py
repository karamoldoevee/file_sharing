from django.contrib.auth.models import User
from django.views.generic import DetailView


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
