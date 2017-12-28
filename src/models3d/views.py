from django.contrib.auth.models import User
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import ModelCreateForm
from .models import Model
from .processing import Processor
from badges.models import Collector


class ModelCreateView(CreateView):
    form_class = ModelCreateForm
    model = Model
    success_url = '/'

    def form_valid(self, form):
        model = form.save(commit=False)
        user = User.objects.get(pk=self.request.user.pk)
        model.user = user
        model.save()

        if user.models.count() >= 5 and not Collector.objects.filter(user=user).exists():
            collector = Collector(user=user)
            collector.save()

        processor = Processor()
        processor.configure(model.file.path)
        model.weight = processor.weigh()
        model.vertice_count = processor.count_vertices()
        model.save()

        return super(ModelCreateView, self).form_valid(form)


class ModelListView(ListView):
    queryset = Model.objects.all()


class ModelsView(View):
    def post(self, request, *args, **kwargs):
        return ModelCreateView.as_view()(request)

    def get(self, request, *args, **kwargs):
        return ModelListView.as_view()(request)


class ModelDetailView(DetailView):
    queryset = Model.objects.all()
    slug_field = 'name'
    slug_url_kwarg = 'name'
