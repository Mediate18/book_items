from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
import django_tables2

from ..forms import *
from ..filters import *
from ..tables import *



# DocumentScan views
class DocumentScanTableView(ListView):
    model = DocumentScan
    template_name = 'generic_list.html'

    def get_queryset(self):
        return DocumentScan.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DocumentScanTableView, self).get_context_data(**kwargs)
        filter = DocumentScanFilter(self.request.GET, queryset=self.get_queryset())

        table = DocumentScanTable(filter.qs)
        django_tables2.RequestConfig(self.request, ).configure(table)

        context['filter'] = filter
        context['table'] = table

        context['action'] = _("add")
        context['object_name'] = "documentscan"
        context['add_url'] = reverse_lazy('add_documentscan')

        return context


class DocumentScanDetailView(DetailView):
    model = DocumentScan


class DocumentScanCreateView(CreateView):
    model = DocumentScan
    template_name = 'generic_form.html'
    form_class = DocumentScanModelForm
    success_url = reverse_lazy('documentscans')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _("add")
        context['object_name'] = "documentscan"
        return context

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            messages.add_message(self.request, messages.SUCCESS,
                                 _("Your changes will be sent to a moderator for reviewing."))
        return super().form_valid(form)


class DocumentScanUpdateView(UpdateView):
    model = DocumentScan
    template_name = 'generic_form.html'
    form_class = DocumentScanModelForm
    success_url = reverse_lazy('documentscans')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _("update")
        context['object_name'] = "documentscan"
        return context

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            messages.add_message(self.request, messages.SUCCESS,
                                 _("Your changes will be sent to a moderator for reviewing."))
        return super().form_valid(form)


class DocumentScanDeleteView(DeleteView):
    model = DocumentScan
    success_url = reverse_lazy('documentscans')



# SourceMaterial views
class SourceMaterialTableView(ListView):
    model = SourceMaterial
    template_name = 'generic_list.html'

    def get_queryset(self):
        return SourceMaterial.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SourceMaterialTableView, self).get_context_data(**kwargs)
        filter = SourceMaterialFilter(self.request.GET, queryset=self.get_queryset())

        table = SourceMaterialTable(filter.qs)
        django_tables2.RequestConfig(self.request, ).configure(table)

        context['filter'] = filter
        context['table'] = table

        context['action'] = _("add")
        context['object_name'] = "sourcematerial"
        context['add_url'] = reverse_lazy('add_sourcematerial')

        return context


class SourceMaterialDetailView(DetailView):
    model = SourceMaterial


class SourceMaterialCreateView(CreateView):
    model = SourceMaterial
    template_name = 'generic_form.html'
    form_class = SourceMaterialModelForm
    success_url = reverse_lazy('sourcematerials')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _("add")
        context['object_name'] = "sourcematerial"
        return context

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            messages.add_message(self.request, messages.SUCCESS,
                                 _("Your changes will be sent to a moderator for reviewing."))
        return super().form_valid(form)


class SourceMaterialUpdateView(UpdateView):
    model = SourceMaterial
    template_name = 'generic_form.html'
    form_class = SourceMaterialModelForm
    success_url = reverse_lazy('sourcematerials')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _("update")
        context['object_name'] = "sourcematerial"
        return context

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            messages.add_message(self.request, messages.SUCCESS,
                                 _("Your changes will be sent to a moderator for reviewing."))
        return super().form_valid(form)


class SourceMaterialDeleteView(DeleteView):
    model = SourceMaterial
    success_url = reverse_lazy('sourcematerials')



# Transcription views
class TranscriptionTableView(ListView):
    model = Transcription
    template_name = 'generic_list.html'

    def get_queryset(self):
        return Transcription.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TranscriptionTableView, self).get_context_data(**kwargs)
        filter = TranscriptionFilter(self.request.GET, queryset=self.get_queryset())

        table = TranscriptionTable(filter.qs)
        django_tables2.RequestConfig(self.request, ).configure(table)

        context['filter'] = filter
        context['table'] = table

        context['action'] = _("add")
        context['object_name'] = "transcription"
        context['add_url'] = reverse_lazy('add_transcription')

        return context


class TranscriptionDetailView(DetailView):
    model = Transcription


class TranscriptionCreateView(CreateView):
    model = Transcription
    template_name = 'generic_form.html'
    form_class = TranscriptionModelForm
    success_url = reverse_lazy('transcriptions')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _("add")
        context['object_name'] = "transcription"
        return context

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            messages.add_message(self.request, messages.SUCCESS,
                                 _("Your changes will be sent to a moderator for reviewing."))
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = TranscriptionModelForm(request.POST)
        if form.is_valid():
            transcription = form.save(commit=False)
            transcription.author = request.user

            if not self.request.user.is_superuser:
                messages.add_message(self.request, messages.SUCCESS,
                                     _("Your changes will be sent to a moderator for reviewing."))

                from simplemoderation.models import Moderation
                from django.forms.models import model_to_dict
                moderation = Moderation(
                    editor=request.user,
                    action='C',  # Create
                    data=model_to_dict(transcription, fields=[field.name for field in transcription._meta.fields]),
                )
                moderation.save()
            else:
                transcription.save()

            from django.shortcuts import redirect
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class TranscriptionUpdateView(UpdateView):
    model = Transcription
    template_name = 'generic_form.html'
    form_class = TranscriptionModelForm
    success_url = reverse_lazy('transcriptions')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = _("update")
        context['object_name'] = "transcription"
        return context

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            messages.add_message(self.request, messages.SUCCESS,
                                 _("Your changes will be sent to a moderator for reviewing."))
        return super().form_valid(form)


class TranscriptionDeleteView(DeleteView):
    model = Transcription
    success_url = reverse_lazy('transcriptions')

