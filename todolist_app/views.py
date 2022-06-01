
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView, 
    CreateView, 
    UpdateView, 
    DetailView,
    DeleteView,
)

from .forms import  TaskItemForm
from .models import  TaskItem, TaskList




# Views depending on Category

class ToDoView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = "todolist_app/todo.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list_todo"] = TaskList.objects.filter(category="To-Do", created_by=self.request.user)
        return context

class PersonalView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = "todolist_app/personal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list_personal"] = TaskList.objects.filter(category="Personal", created_by=self.request.user)
        return context

class WorkView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = "todolist_app/work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list_work"] = TaskList.objects.filter(category="Work", created_by=self.request.user)
        return context

class ShoppingView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = "todolist_app/shopping.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list_shopping"] = TaskList.objects.filter(category="Shopping", created_by=self.request.user)
        return context

class WishlistView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = "todolist_app/wishlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_list_wishlist"] = TaskList.objects.filter(category="Wishlist", created_by=self.request.user)
        return context



# List Detail View
class ListDetail(LoginRequiredMixin, DetailView):
    model = TaskList
    template_name = "todolist_app/list_detail.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = TaskList.objects.prefetch_related('taskitem_set').all()
        return context



# Create Lists and Tasks
class ListCreate(LoginRequiredMixin, CreateView):
    model = TaskList
    template_name = "todolist_app/list_create.html"
    fields = ["category","title", ]
    
    def form_valid(self, form, ):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('todo'))

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a new list"
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = TaskItem
    template_name = "todolist_app/task_create.html"
    form_class = TaskItemForm

    def get_success_url(self):
        return self.request.GET.get('next', reverse('todo'))
        
    def get_initial(self):
        initial_data = super(TaskCreate, self).get_initial()
        todo_list = TaskList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self,**kwargs):
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context["todo_list"] = TaskList.objects.get(id=self.kwargs["list_id"])
        context["title"] = "Add a new task item"
        return context

    


# Edit Lists and Tasks
class ListEdit(LoginRequiredMixin, UpdateView):
    model = TaskList
    fields = ["category", "title",]
    template_name = "todolist_app/list_edit.html"
    
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse('todo'))

    def get_context_data(self,**kwargs):
        context = super(ListEdit, self).get_context_data()
        context["title"] = "Edit item"
        return context

class TaskEdit(LoginRequiredMixin, UpdateView):
    model = TaskItem
    template_name = "todolist_app/task_edit.html"
    form_class = TaskItemForm

    def get_success_url(self):
        return self.request.GET.get('next', reverse('todo'))

    def get_context_data(self,**kwargs):
        context = super(TaskEdit, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context



# Delete List and Tasks
class ListDelete(LoginRequiredMixin, DeleteView):
    model = TaskList
    template_name = "todolist_app/list_confirm_delete.html"
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('todo'))

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = TaskItem
    template_name = "todolist_app/task_confirm_delete.html"
    
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('todo'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context