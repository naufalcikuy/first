from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from .forms import PostForm, HistoryForm, BabyBioForm, edit_member_form, new_event_form, edit_knowledge_form, edit_event_form
from .models import Post, Knowledge, BabyBio, History, Event
from django.contrib.auth.decorators import login_required



def knowledge_list(request):
    knowledges = Knowledge.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'kelola/post_list.html', {'knowledges': knowledges, 'events': events})
   # post = get_object_or_404(Post, pk = pk)

@login_required(login_url='/admin/login/')
def show_admin(request):
    knowledges = Knowledge.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'kelola/post_list.html', {'knowledges': knowledges, 'events': events})


def post_detail(request, id_knowledge):
    knowledge = get_object_or_404(Knowledge, id=id_knowledge)
    return render(request, 'kelola/post_detail.html', {'knowledge': knowledge})

@login_required(login_url='/admin/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            knowledge = form.save(commit=False)
            #knowledge.author = request.user
            knowledge.published_date = timezone.now()
            knowledge.save()
            return redirect('post_detail', id_knowledge=knowledge.id)
    else:
        form = PostForm()
    return render(request, 'kelola/post_edit.html', {'form': form})# Create your views here.





@login_required(login_url='/admin/login/')
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
    knowledges = Knowledge.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'kelola/show_knowledge.html', {'knowledges': knowledges})

def show_history(request):
    check_height = History.objects.none()
    check_weight = History.objects.none()
    check_head = History.objects.none()
    check_immunization = History.objects.none()

    nomorbalita= request.GET.get('nomorbalita', None)
    
    if nomorbalita:
        check_height = History.objects.filter(check="height").filter(baby_id__id_baby=int(nomorbalita))
        check_weight = History.objects.filter(check="weight").filter(baby_id__id_baby=int(nomorbalita))
        check_head = History.objects.filter(check="headcircumference").filter(baby_id__id_baby=int(nomorbalita))
        check_immunization = History.objects.filter(check="immunization").filter(baby_id__id_baby=int(nomorbalita))
    return render(request, 'kelola/show_history.html', {'check_height': check_height, 'check_weight': check_weight, 'check_head': check_head, 'check_immunization': check_immunization})

def show_event(request):
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'kelola/show_event.html', {'events': events})

@login_required(login_url='/admin/login/')
def show_pengetahuan(request):
    knowledges_health = Knowledge.objects.all().filter(category="Health")
    knowledges_growing = Knowledge.objects.all().filter(category="Growing")
    knowledges_development = Knowledge.objects.all().filter(category="Development")
    knowledges_immunization = Knowledge.objects.all().filter(category="Immunization")
    knowledges = Knowledge.objects.all()
    return render(request, 'kelola/kelola_pengetahuan.tmpl', {'knowledges_health': knowledges_health, 'knowledges_growing': knowledges_growing, 'knowledges_development': knowledges_development, 'knowledges_immunization': knowledges_immunization, 'knowledges': knowledges})

def show_health(request):
    knowledges_health = Knowledge.objects.all().filter(category="Health").filter(published_date__lte=timezone.now()).order_by('-published_date')
    knowledges = Knowledge.objects.all()
    return render(request, 'kelola/health_knowledge.html', {'knowledges_health': knowledges_health,'knowledges': knowledges})

def show_grow(request):
    knowledges_growing = Knowledge.objects.all().filter(category="Growing").filter(published_date__lte=timezone.now()).order_by('-published_date')
    knowledges = Knowledge.objects.all()
    return render(request, 'kelola/grow_knowledge.html', {'knowledges_growing': knowledges_growing,'knowledges': knowledges})

def show_development(request):
    knowledges_development = Knowledge.objects.all().filter(category="Development").filter(published_date__lte=timezone.now()).order_by('-published_date')
    knowledges = Knowledge.objects.all()
    return render(request, 'kelola/development_knowledge.html', {'knowledges_development': knowledges_development,'knowledges': knowledges})

def show_immun(request):
    knowledges_immunization = Knowledge.objects.all().filter(category="Immunization").filter(published_date__lte=timezone.now()).order_by('-published_date')
    knowledges = Knowledge.objects.all()
    return render(request, 'kelola/immun_knowledge.html', {'knowledges_immunization': knowledges_immunization,'knowledges': knowledges})    
    



@login_required(login_url='/admin/login/')
def new_knowledge(request):
    knowledges_health = Knowledge.objects.all().filter(category="Health")
    knowledges_growing = Knowledge.objects.all().filter(category="Growing")
    knowledges_development = Knowledge.objects.all().filter(category="Development")
    knowledges_immunization = Knowledge.objects.all().filter(category="Immunization")
    return render(request, 'kelola/knowledge_new.html', {'knowledges_health': knowledges_health, 'knowledges_growing': knowledges_growing, 'knowledges_development': knowledges_development, 'knowledges_immunization': knowledges_immunization})

def delete_knowledge(request):
    knowledges_health = Knowledge.objects.all().filter(category="Health")
    knowledges_growing = Knowledge.objects.all().filter(category="Growing")
    knowledges_development = Knowledge.objects.all().filter(category="Development")
    knowledges_immunization = Knowledge.objects.all().filter(category="Immunization")
    return render(request, 'kelola/knowledge_delete.html', {'knowledges_health': knowledges_health, 'knowledges_growing': knowledges_growing, 'knowledges_development': knowledges_development, 'knowledges_immunization': knowledges_immunization})

@login_required(login_url='/admin/login/')
def show_pemeriksaan(request):
    check_height = History.objects.all().filter(check="height")
    check_weight = History.objects.all().filter(check="weight")
    check_head = History.objects.all().filter(check="headcircumference")
    check_immunization = History.objects.all().filter(check="immunization")

    nomorbalita= request.GET.get('nomorbalita', None)
    
    if nomorbalita:
        check_height = check_height.filter(baby_id__id_baby=int(nomorbalita))
        check_weight = check_weight.filter(baby_id__id_baby=int(nomorbalita))
        check_head = check_head.filter(baby_id__id_baby=int(nomorbalita))
        check_immunization = check_immunization.filter(baby_id__id_baby=int(nomorbalita))
    '''if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.author = request.user
            history.published_date = timezone.now()
            history.save()
            history.update_status()
            history.save()
            #itung
    else:
        form = HistoryForm()
        '''  

    return render(request, 'kelola/kelola_pemeriksaan.html', {'check_height': check_height, 'check_weight': check_weight, 'check_head': check_head, 'check_immunization': check_immunization})
    

@login_required(login_url='/admin/login/')    
def show_anggota(request):
    member_baby = BabyBio.objects.all()
    return render(request, 'kelola/kelola_anggota.html', {'member_baby': member_baby})

def detail_member(request, id_bayi):
    member_baby = get_object_or_404(BabyBio, id_baby=id_bayi)
    return render(request, 'kelola/detail_member.html', {'member_baby': member_baby})


@login_required(login_url='/admin/login/')
def edit_member(request, id_bayi):
    member_baby = get_object_or_404(BabyBio, id_baby=id_bayi)
    if request.method=="POST":
        form = edit_member_form(request.POST, instance = member_baby)
        if form.is_valid():
            member_baby = form.save(commit = False)
            member_baby.published_date = timezone.now()
            member_baby.save()
            return redirect('detail_member', id_bayi=id_bayi)
    else:
        form = edit_member_form(instance = member_baby)
    return render(request, 'kelola/edit_member.html', {'member_baby': member_baby, 'form': form})

def detail_knowledge(request, id_knowledge):
    knowledges = get_object_or_404(Knowledge, id=id_knowledge)
    return render(request, 'kelola/detail_knowledge.html', {'knowledges': knowledges})

@login_required(login_url='/admin/login/')
def edit_knowledge(request, id_knowledge):
    knowledges = get_object_or_404(Knowledge, id=id_knowledge)
    if request.method=="POST":
        form = edit_knowledge_form (request.POST, instance = knowledges)
        if form.is_valid():
            knowledges = form.save(commit = False)
            knowledges.save()
            return redirect('detail_knowledge', id_knowledge=id_knowledge)
    else:
        form = edit_knowledge_form(instance = knowledges)
    return render(request, 'kelola/edit_knowledge.html', {'knowledges': knowledges, 'form': form})


def detail_event(request, id_event):
    events = get_object_or_404(Event, id=id_event)
    return render(request, 'kelola/detail_event.html', {'events': events})

@login_required(login_url='/admin/login/')
def edit_event(request, id_event):
    events = get_object_or_404(Event, id=id_event)
    if request.method=="POST":
        form = edit_event_form (request.POST, instance = events)
        if form.is_valid():
            events = form.save(commit = False)
            events.published_date = timezone.now()
            events.save()
            return redirect('detail_event', id_event=id_event)
    else:
        form = edit_event_form(instance = events)
    return render(request, 'kelola/edit_event.html', {'events': events, 'form': form})

@login_required(login_url='/admin/login/')
def delete_event(request, id_event):
    events = Event.objects.get(id=id_event)
    events.delete()
    return redirect('show_kegiatan')

@login_required(login_url='/admin/login/')
def delete_knowledge(request, id_knowledge):
    knowledges = Knowledge.objects.get(id=id_knowledge)
    knowledges.delete()
    return redirect('show_pengetahuan')

@login_required(login_url='/admin/login/')
def delete_member(request, id_bayi):
    member_baby = BabyBio.objects.get(id_baby=id_bayi)
    member_baby.delete()
    return redirect('show_anggota')
    #return HttpResponseRedirect(reverse('show_anggota'))

@login_required(login_url='/admin/login/')
def new_member(request):
    if request.method == "POST":
        form = BabyBioForm(request.POST)
        if form.is_valid():
            babybio = form.save(commit=False)
            babybio.created_date = timezone.now()
            babybio.save()
            return redirect('show_anggota')
            #return redirect('detail_member', id_bayi= babybio.id_baby)
    else:
        form = BabyBioForm()
    return render(request, 'kelola/new_member.html', {'form': form})

@login_required(login_url='/admin/login/')
def new_event(request):
    if request.method == "POST":
        form = new_event_form(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.published_date = timezone.now()
            event.save()
            return redirect('show_kegiatan')
             
    else:
        form = new_event_form()
    return render(request, 'kelola/new_event.html', {'form': form})

@login_required(login_url='/admin/login/')
def show_kegiatan(request):
    events = Event.objects.all()
    return render(request, 'kelola/kelola_kegiatan.html', {'events': events})
    
    
@login_required(login_url='/admin/login/')
def new_history(request):
    # history = get_object_or_404(History)
    if request.method == "POST":
        form = HistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.author = request.user
            history.published_date = timezone.now()
            history.save()
            history.update_status()
            history.save()
            return redirect('show_pemeriksaan')
            alert('aaa')
            #itung
    else:
        form = HistoryForm()


    return render(request, 'kelola/new_history.html', {'form': form})

