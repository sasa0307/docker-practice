from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
class IndexView(View):
    def get(self, request):
        #todoリストを取得
        todo_list = Task.objects.all()
        
        context = {
            "todo_list": todo_list
        }
        
        #テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)
    
class AddView(View):
    def get(self, request):
        form = TaskForm()
        
        return render(request, "mytodo/add.html",{'form': form})
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        is_valid = form.is_valid()
        
        if is_valid:
            form.save()
            return redirect('/')
        
        #　データが正常じゃない場合 
        return render(request, 'mytodo/add.html',{'form':form})
    
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        
        task = Task.objects.get(id=task_id)
        task.complite = not task.complite
        task.save()
        
        return redirect('/')
    
class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
    
#ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
Update_task_complete = Update_task_complete.as_view()


