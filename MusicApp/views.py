from django.views import generic
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album, Song
from .forms import UserForm, LoginForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('MusicApp:login')
    else:
        all_albums = Album.objects.filter(user=request.user)
        return render(request, 'music/index.html',{'all_albums': all_albums})



class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name = 'music/album_form.html'

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    template_name = 'music/album_form.html'

class AlbumDelete(DeleteView):
    model = Album
    success_url =reverse_lazy('MusicApp:index')

class SongCreate(CreateView):
    model = Song
    fields = ['album','song_title', 'audio_file']
    template_name = 'music/song_form.html'


class UserFormView(View):

    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                            login(request,user)
                            return redirect('MusicApp:index')
        return render(request,self.template_name, {'form': form})


class LoginFormView(View):

    form_class = LoginForm
    template_name = 'music/login_form.html'

    def get(self,request):
        form = self.form_class(None)
        return  render(request,self.template_name,{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('MusicApp:index')
        return render(request,self.template_name,{'form':form})

def logout_user(request):
    logout(request)
    return redirect('MusicApp:login')



















