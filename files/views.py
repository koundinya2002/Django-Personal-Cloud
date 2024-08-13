from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Folder, File
from .forms import FileUploadForm, FolderCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
@login_required
def home(request):
    folders = Folder.objects.filter(owner = request.user.id)
    return render(request, 'home.html', {
        "things":folders,
    })


@login_required
def files(request, pk):
    files = File.objects.filter(folder = pk)
    return render(request, 'files.html',{
        "files": files,
        "pk": pk
    })


@login_required
def upload_files(request, pk):
    if request.method == "POST":
        files = File.objects.filter(folder = pk)
        name = request.POST["file_name"]
        file2 = request.FILES["file"]
        document = File.objects.create(folder_id=pk,file_name=name, file=file2)
        document.save()
        return render(request, 'files.html',{
            "files":files,
            "pk": pk,
        })
    return render(request,'upload_file.html')


# @login_required
class CreateFolderView(CreateView):
    model = Folder
    form_class = FolderCreationForm
    template_name = 'created.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    success_url = reverse_lazy("home")