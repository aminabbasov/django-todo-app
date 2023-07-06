from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import ReminderModel
from .forms import ReminderForm, RegisterForm, LoginForm


class ReminderRegisterView(SuccessMessageMixin, FormView):
    template_name = 'reminder/reminder_register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list-page')
    success_message = 'You have successfully registered!'

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)

        return super(ReminderRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        '''
        Реализовать messages об ошибках
        https://youtu.be/j7hzkm5BUs8?t=489
        '''
        return super().form_invalid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list-page')

        return super(ReminderRegisterView, self).get(*args, **kwargs)


class ReminderLoginView(SuccessMessageMixin, LoginView):
    template_name = 'reminder/reminder_login.html'
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list-page')
    success_message = 'You have successfully logged in!'

    def form_invalid(self, form):
        '''
        Реализовать messages об ошибках
        https://youtu.be/j7hzkm5BUs8?t=489
        '''
        # messages.error(self.request, 'Ошибка')        
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('list-page')


class ReminderLogoutView(LogoutView):
    next_page = 'login-page'


class ReminderListView(LoginRequiredMixin, ListView):
    model = ReminderModel
    template_name = 'reminder/reminder_list.html'
    context_object_name = 'reminders'

    def get_queryset(self):
        ordering = self.request.GET.get('sort')
        user_objects = ReminderModel.objects.filter(user=self.request.user)
        object_list = user_objects.filter(is_completed=False)

        if ordering:
            object_list = object_list.order_by(ordering)

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'active'

        return context


class ReminderArchiveListView(LoginRequiredMixin, ListView):
    model = ReminderModel
    template_name = 'reminder/reminder_list.html'
    context_object_name = 'reminders'

    def get_queryset(self):
        ordering = self.request.GET.get('sort')
        user_objects = ReminderModel.objects.filter(user=self.request.user)
        object_list = user_objects.filter(is_completed=True)

        if ordering:
            object_list = object_list.order_by(ordering)

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'archive'

        return context


def reminder_archive_view(request, pk):
    model = ReminderModel.objects.get(id=pk)
    model.is_completed = True
    model.save()
    return redirect('list-page')


def reminder_unarchive_view(request, pk):
    model = ReminderModel.objects.get(id=pk)
    model.is_completed = False
    model.save()
    return redirect('archive-page')


class ReminderSearchListView(LoginRequiredMixin, ListView):
    model = ReminderModel
    template_name = 'reminder/reminder_list.html'
    context_object_name = 'reminders'

    def get_queryset(self):
        search_input = self.request.GET.get("query")
        user_objects = ReminderModel.objects.filter(user=self.request.user)
        object_list = user_objects.filter(
            Q(title__icontains=search_input) | Q(selected_color__icontains=search_input)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get("query")
        context['url'] = 'search'
        context['search_input'] = search_input

        return context


class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = ReminderModel
    template_name = 'reminder/reminder_form.html'
    form_class = ReminderForm
    success_url = reverse_lazy('list-page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReminderCreateView, self).form_valid(form)


class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = ReminderModel
    template_name = 'reminder/reminder_form.html'
    form_class = ReminderForm
    context_object_name = 'reminder'
    success_url = reverse_lazy('list-page')


class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = ReminderModel
    template_name = 'reminder/reminder_delete.html'
    context_object_name = 'reminder'
    success_url = reverse_lazy('list-page')
