# exportamos la redireccion reverse_lazy
from django.urls import reverse_lazy

# aqui hacemos in import para requerir que sea miebro del staff
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Vistas basadas en clases
from django.views.generic.list import ListView  # lectura del modelo
from django.views.generic.detail import DetailView  # lectura de un id del modelo
from django.views.generic.edit import CreateView  # crear formularios
from django.views.generic.edit import UpdateView  # Para actualizar campos
from django.views.generic.edit import DeleteView  # Para actualizar campos


# mi modelo
from .models import Page
from pages.forms import PageForm


# clase que se utiliza para requeirir que el usuario sea miembro del staff


# Create your views here.

# para crear una vista y pasarle un modelo se utiliza
#  ListView con el modelo completo  y para leerlo en el template le pasamos page_list
class PagesListViews(ListView):

    model = Page


# para crear una vista pasadole un id y mostrar solo un contenido
# especifico se utiliza DetailView y para leerlo en el template le pasamos page + nombre del modelo
class PageDatailViews(DetailView):
    model = Page


# ahora creamo crateviews este sirve para crear un formulario le pasamo un forms.py
# para editar los campos del modelo page y pasarle widges y editarlos desde el forms.py
# clase que se utiliza para requeirir que el usuario sea miembro del staff
@method_decorator(staff_member_required, name="dispatch")
class PageCreateViews(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages')


# undateviews ese clase trae el modelo y con los campos form actualiza su html
# luego con el metodo get success realiza un reverse a update y concatena la url
# con un ok para luego mostrar un mensaje con el html obtido por el GET
@method_decorator(staff_member_required, name="dispatch")
class PageUpdateViews(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse_lazy('update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name="dispatch")
class PageDeleteViews(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')
