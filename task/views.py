from django.views.generic.edit import FormView
from django.shortcuts import render
from .forms import UploadFileForm
from django.conf import settings
from .tfidf import get_words, get_tfidf


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            main_file = _main_file_handler(request.FILES['file'])
            other_files = _handle_uploaded_file(request.FILES.getlist('files'))

            other_files_words = get_words(other_files, many=True)
            tfidf = get_tfidf(main_file, other_files_words)

            return render(request, 'task/success.html', {'data': tfidf})

    form = UploadFileForm()
    return render(request, 'task/index.html', {'form': form})


def _main_file_handler(file) -> dict:
    """ Для главного файла. Возвращает словарь, где ключ само словоб а значение частота появления в тексте """

    data = b''
    to_clear = ',.!?:;*()"'

    for chunk in file.chunks():
        data += chunk

    data = data.decode()
    data_map = {}
    data_split = data.split()

    for word in data_split:
        cleaned_word = word.strip(to_clear).lower()
        if cleaned_word not in data_map:
            data_map[cleaned_word] = [0, ]

        data_map[cleaned_word][0] += 1

    for key, value in data_map.items():
        value.append(value[0] / float(len(data_split)))

    return data_map


def _handle_uploaded_file(file):
    """ Для остальных файлов. Возвращает содержимое файла в строке, или файлов в списке строк """

    if isinstance(file, list):
        data = []
        data_tmp = b''
        for f in file:
            for chunk in f.chunks():
                data_tmp += chunk
            data.append(data_tmp.decode())
        return data

    data = b''
    for chunk in file.chunks():
        data += chunk
    return data.decode()
