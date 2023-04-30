# from django.http import HttpResponse
# from django.urls import reverse
# from django.shortcuts import render, redirect, get_object_or_404

from .models import Todo
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Todo


class TodoIndexView(ListView):
    model = Todo
    context_object_name = 'todo_list'
    template_name = 'Todo/index.html'

    def get_queryset(self):
         return Todo.objects.all()

class TodoDeleteView(DeleteView):
    model = Todo
    fields = ['todo_id']
    success_url = reverse_lazy('Todo:index')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = []  # Or specify fields to be updated
    success_url = reverse_lazy('Todo:index')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.todo_status = 'Completed'
        todo.save()
        return super().form_valid(form)
    
class TodoCreateView(CreateView):
    model = Todo
    fields = ['todo_title']
    success_url = reverse_lazy('Todo:index')


# OLD VIEWS / NON-GENERIC VIEWS

# def create_todo(request):
#     if request.method == 'POST':
#         title = request.POST['todo_title']
#         todo = Todo.objects.create(todo_title=title)
#         return redirect('Todo:index')
#     else:
#         return render(request, 'Todo:index')

# def delete_record(request, todo_id):
#     # Retrieve the record by id
#     record = Todo.objects.get(id=todo_id)
#     if request.method == 'POST':
#         # Delete the record
#         record.delete()
#         # Redirect to a success page or another page in your app
#         return redirect('Todo:index')
#     else:
#         # Render a confirmation page to ask the user for confirmation before deleting the record
#         return redirect('Todo:index')

# def index(request):
#         todo_list = Todo.objects.all()
#         context = {
#             'todo_list': todo_list,
#         }
#         return render(request, "Todo/index.html", context)

# def update_status(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     todo.todo_status = "completed"
#     todo.save()
#     return redirect('Todo:index')