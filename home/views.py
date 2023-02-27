from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from .models import Item


class AboutView(TemplateView):
    template_name = "home/about.html"


# Create your views here.

class ItemListView(ListView):
    model = Item
    template_name = "home/home.html"

class CommentGet(DetailView):
    model = Item
    template_name = "home/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Item
    form_class = CommentForm
    template_name = "home/item_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, *kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user # new
        comment = form.save(commit=False)
        comment.item = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        item = self.get_object()
        return reverse("item_detail", kwargs={"pk": item.pk})


class ItemDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "home/item_new.html"
    fields = ["title", "description", "price", "condition"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    template_name = "home/item_edit.html"
    fields = ["title", "description", "price", "condition"]
    

    def test_func(self):  # new
        obj = self.get_object()
        return obj.user == self.request.user

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = "home/item_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):  # new
        obj = self.get_object()
        return obj.user == self.request.user