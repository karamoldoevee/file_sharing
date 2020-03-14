from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.models import File
from webapp.forms import FileForm


class FileListView(ListView):
    model = File
    template_name = 'file/list.html'
    context_object_name = 'files'

    ordering = ['-created_at']

    paginate_by = 10

    paginate_orphans = 1


class FileCreateView(CreateView):
    model = File
    template_name = 'add.html'
    form_class = FileForm

    def form_valid(self, form):
        self.object = File.objects.create(author=self.request.user, upload=form.cleaned_data['upload'],
                                          signature=form.cleaned_data['signature'],
                                          created_at=form.cleaned_data['created_at'])

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class FileUpdateView(UpdateView):
    model = File
    template_name = 'change.html'
    fields = FileForm
    context_object_name = 'file'

    def get_success_url(self):
        return reverse('webapp:index')


class FileDeleteView(DeleteView):
    template_name = 'delete.html'
    model = File
    context_object_name = 'file'
    success_url = reverse_lazy('webapp:index')