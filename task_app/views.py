from django.shortcuts import render,redirect
from .form import TaskForm
from .models import TaskModel
# Create your views here.


def task(request):
    # form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskForm()

    return render(request,'./task.html',{'form':form})




def edit(request, id):
    post = TaskModel.objects.get(pk=id)  
    post_form = TaskForm(instance=post)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:  
        form = post_form  

    return render(request, 'task.html', {'form': form})


def delete(request,id):
    post = TaskModel.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
