from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

from posts import models, forms
from groups.models import Group

# Create your views here.

# https://docs.djangoproject.com/en/dev/ref/models/querysets/#select-related

"""
select_related works by creating an SQL join and including the fields of the related object in the
SELECT statement. For this reason, select_related gets the related objects in the same database query.
However, to avoid the much larger result set that would result from joining across a ‘many’ relationship,
select_related is limited to single-valued relationships - foreign key and one-to-one.

prefetch_related, on the other hand, does a separate lookup for each relationship, and does the ‘joining’ in Python.
This allows it to prefetch many-to-many and many-to-one objects, which cannot be done using select_related,
in addition to the foreign key and one-to-one relationships that are supported by select_related.
It also supports prefetching of GenericRelation and GenericForeignKey, however,
it must be restricted to a homogeneous set of results. For example,
prefetching objects referenced by a GenericForeignKey is only supported if the query is restricted to one ContentType.
"""

class PostList(LoginRequiredMixin, SelectRelatedMixin, generic.ListView):
    model = models.Post
    # related models
    # SQL joining, for one-to-one relation, for specific relation
    select_related = ('user', 'group')  # try to make comment it, logic will remain same because 'GroupMember' model has already 'unique' filtering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = Group.objects.filter(members__in=[self.request.user])
        context['other_groups'] = Group.objects.all()
        return context

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
                                             # SQL joining, for many-to-many relation
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
