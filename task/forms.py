from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Основной файл')
    files = forms.FileField(label='Файлы для сравнения с основным',
                            widget=forms.ClearableFileInput(attrs={'multiple': True}))
