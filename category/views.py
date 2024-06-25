from django.shortcuts import render,redirect
from .form import TaskCategoryForm
# Create your views here.





def category(request):
    # form = TaskCategoryForm
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = TaskCategoryForm()

    return render(request,'./taskCategory.html',{'form':form})