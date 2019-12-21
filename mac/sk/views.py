from django.db.models import Q
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.urls import path
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import BookForm
from .models import Book
from django.contrib import messages


def index(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage(location='sk/static/sk/media')
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        context['url'] = fs.url(name)
    return render(request, 'sk/html/index.html', context)


def cr(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cr')
    else:
        form = BookForm()
    return render(request, 'sk/html/check_result.html', {
        'form': form, 'books': books,
    })


def cur(request):
    books = Book.objects.all()
    return render(request, 'sk/html/check_uploaded_result.html', {
        'books': books
    })


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Book.objects.filter(Q(Surname__icontains=srch) |
                                        Q(Name__icontains=srch) |
                                        Q(Std__icontains=srch) |
                                        Q(Mo_No__icontains=srch)

                                        )
            if match:
                return render(request, 'sk/html/search.html', {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect('search')
    return render(request, 'sk/html/search.html')


