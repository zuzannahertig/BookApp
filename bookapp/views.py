from django.shortcuts import render, get_object_or_404, redirect
from . models import Book, Text, Author, Period
from . forms import *
from . utils import *
import os
from DeepImageSearch import Index, LoadData, SearchImage

def get_image(request, text_id):
    text = Text.objects.get(pk=text_id)
    title = text.title
    p = text.file.path
    with open(p, 'r') as f:
        data = f.read()
    image = generate_image(data)
        
    context = {'title': title,
        'image': image
        }

    return render(request, 'bookapp/image.html', context)

def get_predictions(request, book_id):

    model_abs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images_6')

    image_list = LoadData().from_folder([model_abs_path])
    Index(image_list).Start()
    book = Book.objects.get(pk=book_id)
    title = book.title
    output = SearchImage().get_similar_images(image_path=book.image.path, number_of_images=5)
   
    similar_images = []
    paths = []

    for v in output.values():
        x = v.split('_6/')
        similar_images.append(x[1])
        paths.append(v)
   
    abs_paths = []
    for i in similar_images:
        p = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images_6/'+i)
        abs_paths.append(p)


    static_paths = []

    for i in similar_images:
        static_paths.append('bookapp/' + i)
    
    context = {'similar_images': similar_images, 'static_paths': static_paths, 'title': title}

    return render(request, 'bookapp/sim/similar.html', context)

def texts(request):
    all_texts = Text.objects.all()
    return render(request, 'bookapp/text/index.html',
                {'all_texts': all_texts})

def texts_details(request, text_id):
    action = 'Projekt o ID = ' + str(text_id)
    text = get_object_or_404(Text, pk=text_id)
    return render(request, 'bookapp/text/details.html', locals())

def texts_new(request):
    title = 'Nowy tekst'
    if request.method == 'POST':
        form = TextForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('teksty')
    else:
        form = TextForm()

    return render(request, 'bookapp/text/new.html', locals())

def texts_delete(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    text.delete()

    return redirect('teksty')

def texts_update(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    form = TextForm(request.POST or None, instance=text)

    if form.is_valid():
        form.save()
        return redirect('teksty')
    
    return render(request, 'bookapp/text/update.html', locals())

def books(request):
    all_books = Book.objects.all()
    return render(request, 'bookapp/book/index.html',
                {'action': 'Wyświetl książki', 'all_books': all_books})

def books_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookapp/book/details.html', locals())

def books_new(request):
    title = 'Nowa książka'
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('ksiazki')
    else:
        form = BookForm()

    return render(request, 'bookapp/book/new.html', locals())

def books_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()

    return redirect('ksiazki')

def books_update(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('ksiazki')

    return render(request, 'bookapp/book/update.html', locals())

def periods(request):
    all_periods = Period.objects.all()
    return render(request, 'bookapp/period/index.html',
                {'action': 'Wyświetl epoki', 'all_periods': all_periods})

def periods_details(request, period_id):
    period = get_object_or_404(Period, pk=period_id)
    return render(request, 'bookapp/period/details.html', locals())

def periods_new(request):
    title = 'Nowa epoka'
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            period = Period(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                beginning = form.cleaned_data['beginning'],
                end = form.cleaned_data['end']
            )
            period.save()
            return redirect('epoki')
    else:
        form = PeriodForm()

    return render(request, 'bookapp/period/new.html', locals())

def periods_delete(request, period_id):
    period = get_object_or_404(Period, pk=period_id)
    period.delete()

    return redirect('epoki')

def periods_update(request, period_id):
    period = get_object_or_404(Period, pk=period_id)
    form = PeriodForm(request.POST)

    if form.is_valid():
                period = Period(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    beginning = form.cleaned_data['beginning'],
                    end = form.cleaned_data['end']
                )
                period.save()
                return redirect('epoki')

    return render(request, 'bookapp/period/update.html', locals())

def authors(request):
    all_authors = Author.objects.all()
    return render(request, 'bookapp/author/index.html',
                {'action': 'Wyświetl autorów', 'all_authors': all_authors})

def authors_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author_id)
    return render(request, 'bookapp/author/details.html', locals())

def authors_new(request):
    title = 'Nowy autor'
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('autorzy')
    else:
        form = AuthorForm()

    return render(request, 'bookapp/author/new.html', locals())

def authors_delete(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    author.delete()
    
    return redirect('autorzy')

def authors_update(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    form = AuthorForm(request.POST or None, instance=author)

    if form.is_valid():
        form.save()
        return redirect('autorzy')

    return render(request, 'bookapp/author/update.html', locals())

# def index(response):
#     return render(response, 'bookapp/index.html')
    
def project(request):
    all_books = Book.objects.all()
    return render(request, 'bookapp/about.html',
                {'all_books': all_books})