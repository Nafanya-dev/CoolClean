from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from CoolClean.washers.forms import WasherForm
from CoolClean.washers.models import Washer, WasherImage
from CoolClean.mixin import AuthorizationRequiredMixin


PRODUCT_URL = '/washers'


class WasherListView(ListView):
    model = Washer
    template_name = 'product_list.html'
    context_object_name = 'products'
    extra_context = {
        'product_url': PRODUCT_URL,
        'detail_url': 'detail-washer-page',
        'update_url': 'update-washer-page',
    }

    def get_queryset(self):
        return Washer.objects.prefetch_related('images').all()


class WasherDetailView(DetailView):
    model = Washer
    template_name = 'washers/detail_washer.html'
    context_object_name = 'product'
    extra_context = {
        'product_url': PRODUCT_URL
    }

    def get_queryset(self):
        return Washer.objects.prefetch_related('images').all()


class WasherCreateView(AuthorizationRequiredMixin,
                       SuccessMessageMixin, CreateView):
    model = Washer
    form_class = WasherForm
    template_name = 'create_form.html'
    extra_context = {
        'title': 'Стиральная машина',
        'button': 'Добавить'
    }

    def form_valid(self, form):
        washer = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            WasherImage.objects.create(washer=washer, image=image)
        return super().form_valid(form)

    success_url = reverse_lazy('washer-list-page')
    success_message = 'Товар успешно добавлен'


class WasherUpdateView(AuthorizationRequiredMixin,
                       SuccessMessageMixin, UpdateView):
    form_class = WasherForm
    model = Washer
    template_name = 'create_form.html'
    extra_context = {
        'title': 'Стиральная Машина',
        'button': 'Изменить',
        'product_url': PRODUCT_URL
    }

    def form_valid(self, form):
        washer = form.save()
        images = self.request.FILES.getlist('images')
        for image in images:
            WasherImage.objects.create(washer=washer, image=image)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_images'] = WasherImage.objects.filter(washer=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('detail-washer-page', kwargs={'pk': self.object.pk})

    success_message = 'Данные товара изменены'


class WasherDeleteView(AuthorizationRequiredMixin,
                       SuccessMessageMixin, DeleteView):
    model = Washer
    template_name = 'delete_product.html'
    context_object_name = 'product'

    success_url = reverse_lazy('washer-list-page')
    success_message = 'Позиция удалена'


@require_http_methods(["DELETE"])
def delete_image(request, image_id):
    try:
        image = WasherImage.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'success': True})
    except WasherImage.DoesNotExist:
        return JsonResponse({'success': False}, status=404)
