from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm, RegisterUserForm, LoginUserForm


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('?').filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            return redirect('login')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.post_id = self.kwargs.get('pk')
        self.object.name = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'User/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'User/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def Logout(request):
    logout(request)
    return redirect('home')
