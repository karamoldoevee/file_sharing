from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.base import View

from webapp.base_views import SearchView
from webapp.forms import SimpleSearchForm, AnonymousFileForm, FileForm
from webapp.models import File, Private


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
    form_class = AnonymousFileForm

    def get_form(self, form_class=None):
        if self.request.user.is_authenticated:
            form_class = FileForm
        return super(FileCreateView, self).get_form(form_class)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            if request.user.is_authenticated:
                self.object.author = request.user
            else:
                self.object.status = 'public'
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileUpdateView(PermissionRequiredMixin, UpdateView):
    model = File
    template_name = 'change.html'
    fields = ['signature', 'upload', 'status']
    context_object_name = 'file'
    permission_required = 'webapp.change_file'
    permission_denied_message = "Доступ запрещён"

    def get_success_url(self):
        return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})


class FileDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = File
    context_object_name = 'file'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_file'
    permission_denied_message = "Доступ запрещён"


class AddToPrivate(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        file = get_object_or_404(File, pk=request.POST.get('pk'))
        Private.objects.get_or_create(user=user, file=file)
        return JsonResponse({'pk': file.pk})


class DeleteFromPrivate(LoginRequiredMixin, View):
    permission_required = 'webapp.delete_private'

    def post(self, request, *args, **kwargs):
        user = request.user
        file = get_object_or_404(File, pk=request.POST.get('pk'))
        Private.objects.filter(file=file, user=user).delete()
        return JsonResponse({'pk': file.pk})
