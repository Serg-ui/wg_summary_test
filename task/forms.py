from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Основной файл',
                           widget=forms.ClearableFileInput(attrs={
                               'class': 'form-control',
                               'id': 'inputGroupFile01'
                           })
                           )
    files = forms.FileField(label='Файлы для сравнения с основным',
                            widget=forms.ClearableFileInput(attrs={
                                'multiple': True,
                                'class': 'form-control',
                                'id': 'inputGroupFile02'
                            }))
