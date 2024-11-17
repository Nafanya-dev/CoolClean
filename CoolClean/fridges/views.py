from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from CoolClean.fridges.forms import FridgeForm
from CoolClean.fridges.models import Fridge, FridgeImage
from CoolClean.mixin import AuthorizationRequiredMixin


PRODUCT_URL = '/fridges'


class FridgeListView(ListView):
    model = Fridge
    template_name = 'product_list.html'
    context_object_name = 'products'
    extra_context = {
        'product_url': PRODUCT_URL,
        'detail_url': 'detail-fridge-page',
        'update_url': 'update-fridge-page',
    }

    def get_queryset(self):
        return Fridge.objects.prefetch_related('images').all()


class FridgeDetailView(DetailView):
    model = Fridge
    template_name = 'fridges/detail_fridge.html'
    context_object_name = 'product'
    extra_context = {
        'product_url': PRODUCT_URL
    }

    def get_queryset(self):
        return Fridge.objects.prefetch_related('images').all()


class FridgeCreateView(AuthorizationRequiredMixin,
                       SuccessMessageMixin, CreateView):
    model = Fridge
    form_class = FridgeForm
    template_name = 'create_form.html'
    extra_context = {
        'title': 'Холодильник',
        'button': 'Добавить'
    }

    def form_valid(self, form):
        fridge = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            FridgeImage.objects.create(fridge=fridge, image=image)
        return super().form_valid(form)

    success_url = reverse_lazy('fridge-list-page')
    success_message = 'Товар успешно добавлен'


class FridgeUpdateView(AuthorizationRequiredMixin,
                       SuccessMessageMixin, UpdateView):
    form_class = FridgeForm
    model = Fridge
    template_name = 'create_form.html'
    extra_context = {
        'title': 'Холодильник',
        'button': 'Изменить',
        'product_url': PRODUCT_URL
    }

    def form_valid(self, form):
        fridge = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            FridgeImage.objects.create(fridge=fridge, image=image)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_images'] = FridgeImage.objects.filter(fridge=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('detail-fridge-page', kwargs={'pk': self.object.pk})

    success_message = 'Данные товара изменены'


class FridgeDeleteView(AuthorizationRequiredMixin,
                       SuccessMessageMixin, DeleteView):
    model = Fridge
    template_name = 'delete_product.html'
    context_object_name = 'product'

    success_url = reverse_lazy('fridge-list-page')
    success_message = 'Позиция удалена'


@require_http_methods(["DELETE"])
def delete_image(request, image_id):
    try:
        image = FridgeImage.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'success': True})
    except FridgeImage.DoesNotExist:
        return JsonResponse({'success': False}, status=404)
