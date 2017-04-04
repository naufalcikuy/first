from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import PostForm
from .models import Post
from .models import Knowledge
from .forms import HistoryForm
from .models import History


def knowledge_list(request):
    knowledges = Knowledge.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'kelola/post_list.html', {'knowledges': knowledges})
   # post = get_object_or_404(Post, pk = pk)


def post_detail(request, pk):
    knowledge = get_object_or_404(Knowledge, pk=pk)
    return render(request, 'kelola/post_detail.html', {'knowledge': knowledge})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            knowledge = form.save(commit=False)
            #knowledge.author = request.user
            knowledge.published_date = timezone.now()
            knowledge.save()
            return redirect('post_detail', pk=knowledge.pk)
    else:
        form = PostForm()
    return render(request, 'kelola/post_edit.html', {'form': form})# Create your views here.

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'kelola/post_edit.html', {'form': form})

def show_knowledge(request):
    return render(request, 'kelola/show_knowledge.html')

def show_history(request):
    return render(request, 'kelola/show_history.html')

def show_event(request):
    return render(request, 'kelola/show_event.html')

def new_history(request):
    # history = get_object_or_404(History)
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.author = request.user
            history.published_date = timezone.now()
            history.save()
            return redirect('new_history')
    else:
        form = HistoryForm()
    return render(request, 'kelola/new_history.html', {'form': form})

