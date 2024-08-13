from django import forms
from .models import Folder, File

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file_name', 'file')

        widgets = {
            'file_name':forms.TextInput(attrs={'placeholder':'enter file name here'})
        }


class FolderCreationForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('folder_title',)

        widgets = {
            'folder_title':forms.TextInput(attrs={'placeholder':'enter folder name'})
        }