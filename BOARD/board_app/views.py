from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post, Response
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import ResponseFilter
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-dateCreation')


class AddList(LoginRequiredMixin, CreateView):
    permission_required = 'board_app.add_post'
    model = Post
    template_name = 'add.html'
    fields = ['author', 'category', 'title', 'content']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.postAuthor = self.request.user
        return super().form_valid(form)


class PostEdit(LoginRequiredMixin, UpdateView):
    permission_required = 'board_app.change_post'
    template_name = 'edit.html'
    fields = ['author', 'category', 'title', 'content']
    success_url = '/posts/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class ResponseAdd(LoginRequiredMixin, CreateView):
    model = Response
    template_name = 'response_add.html'
    fields = ['post','text']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.responseAuthor = self.request.user
        form.instance.post = Post.objects.get(pk=self.request.GET.get('post_id'))
        return super().form_valid(form)

    def get_initial(self):
        post_id = self.request.GET.get('post_id')
        if post_id:
            post = Post.objects.get(pk=post_id)
            return {'post': post}
        return {}

    def email(request, self):
        html_content = render_to_string(
            'response_email.html',
            {
                'author': request.Post.author,
            }
        )
        message = EmailMultiAlternatives(
            'Добавлен новый отклик на вашу запись',
            '',
            'Kirill2.5.9@yandex.ru',
            [request.author.email],
        )
        message.attach_alternative(html_content, 'text/html')
        try:
            message.send()
        except Exception as e:
            print(f"Error sending email: {e}")
        return HttpResponseRedirect(self.get_success_url())


class ResponseList(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'response_list.html'
    context_object_name = 'responses'

    # def get_queryset(self):
    #     return Response.objects.filter(post__postAuthor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ResponseDelete(DeleteView):
    template_name = 'response_delete.html'
    queryset = Response.objects.all()
    success_url = '/posts/response_list/'