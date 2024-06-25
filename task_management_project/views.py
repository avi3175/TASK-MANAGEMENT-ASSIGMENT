from django.shortcuts import render
from task_app.models import TaskModel
from category.models import TaskCategory
def home(request):
    task_data = TaskModel.objects.all()
    category_data = TaskCategory.objects.all()
    return render(request,'base.html',{'data':task_data,'info':category_data})