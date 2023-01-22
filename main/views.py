from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(response):
    return render(response, 'main/list.html')

def home(response):
    return render(response, 'main/home.html', {})

# def create(response):
#     if response.method == "POST":
#         form = CreateNewList(response.POST)
#         if form.is_valid():
#             n = form.cleaned_data["name"]
#             t = ToDoList(name=n)
#             t.save()
#         return HttpResponseRedirect("/list", n)
#     else:
#         form = CreateNewList()
#     return render(response, 'main/create.html', {"form":form})

def form(request):
    return render(request, 'main/form.html')

def show(request):
    error = False
    if request.POST:
        if 'first_name' and 'age' in request.POST:
            first_name = request.POST.get('first_name')
            age = request.POST.get('age')
        else:
            error = True
    else:
        error = True
    
    if not error and len(first_name) > 0 and age and int(age) > 0:
         
        if int(age) >= 18:
            age_range = 'pełnoletni/pełnoletnia'
        else:
            age_range = 'niepełnoletni/niepełnoletnia'

        return render(request, 'main/show.html', {'first_name': first_name,
        'age':age, 'age_range': age_range})
    else:
        return render(request, 'main/error.html')
