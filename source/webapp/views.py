from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.base_views import SearchView
from webapp.forms import SimpleSearchForm
from webapp.models import File


class FileListView(SearchView):
    queryset = File.objects.filter(status='public')
    template_name = 'file/list.html'
    context_object_name = 'files'

    ordering = ['-created_at']

    paginate_by = 10

    paginate_orphans = 1

    search_form = SimpleSearchForm

    def get_filters(self):
        return Q(signature__icontains=self.search_value)


class FileDetailView(DetailView):
    template_name = 'file/detail.html'
    context_key = 'file'
    model = File


class FileCreateView(CreateView):
    model = File
    template_name = 'add.html'
    fields = ['signature', 'upload', 'status']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            if request.user.is_authenticated:
                self.object.author = request.user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('webapp:index')


class FileUpdateView(PermissionRequiredMixin, UpdateView):
    model = File
    template_name = 'change.html'
    fields = ['signature', 'upload', 'status']
    context_object_name = 'file'
    permission_required = 'webapp.change_file'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:index')


class FileDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = File
    context_object_name = 'file'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_file'
    permission_denied_message = "Доступ запрещён"
