from django.shortcuts import render
from .models import Directory,DirectoryItem
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Вьюшка на главную страницу с списком всех справочников
def index(request):
    list_directories = Directory.objects.all()
    paginator = Paginator(list_directories, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'directory/index.html', {'posts': posts})


# Вьюшка на страницу с списком всех элементов
def directory_items(request):
    list_directory_items = DirectoryItem.objects.all()
    paginator = Paginator(list_directory_items, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'directory/directory_items.html', {'posts': posts})



def by_directory_items(request, id):
    directory_items = DirectoryItem.objects.filter(parent=id)
    directories = Directory.objects.all()
    current_directories = Directory.objects.get(pk=id)
    paginator = Paginator(directory_items, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'directory_items': directory_items,
        'directories': directories,
        'current_directories': current_directories,
        'posts': posts,
    }
    return render(request, 'directory/by_directory_items.html', context)



def by_directory_items_basic(request):
    directories = Directory.objects.all()
    context = {
        'directory_items': directory_items,
        'directories': directories,
    }
    return render(request, 'directory/by_directory_items_basic.html', context)


def directories_bydate_basic(request):
    directories = Directory.objects.all()
    context = {
        'directories': directories,
    }
    return render(request, 'directory/directories_bydate_basic.html', context)

def directories_bydate(request, date):

    directories = Directory.objects.all()
    current_directories = Directory.objects.get(pk=id)
    paginator = Paginator(directories, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'directories': directories,
        'current_directories': current_directories,
        'posts': posts,
    }
    return render(request, 'directory/directories_bydate.html', context)
