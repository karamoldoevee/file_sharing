from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from webapp.base_views import SearchView
from webapp.forms import SimpleSearchForm
from webapp.models import File


class FileListView(SearchView):
    model = File
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

    def form_valid(self, form):
        self.object = File.objects.create(author=self.request.user, upload=form.cleaned_data['upload'],
                                          signature=form.cleaned_data['signature'], status=form.cleaned_data['status'])
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class FileUpdateView(UpdateView):
    model = File
    template_name = 'change.html'
    fields = ['signature', 'upload', 'status']
    context_object_name = 'file'


    def get_success_url(self):
        return reverse('webapp:index')


class FileDeleteView(DeleteView):
    template_name = 'delete.html'
    model = File
    context_object_name = 'file'
    success_url = reverse_lazy('webapp:index')
