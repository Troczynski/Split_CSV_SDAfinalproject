import os
import mimetypes
import zipfile
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from .forms import UploadFileForm
from .verified_file import verify_file


def handle_uploaded_file(f):
    file_path = 'uploaded_file.csv'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


def create_zip_file(files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))


def clear_previous_files():
    # Usunięcie wcześniejszych plików CSV i archiwum ZIP
    for file in os.listdir('.'):
        if file.endswith('.csv') and file != 'uploaded_file.csv':
            os.remove(file)
    zip_file_path = 'processed_files.zip'
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            clear_previous_files()

            file_path = handle_uploaded_file(request.FILES['file'])
            if verify_file(file_path):

                processed_files = [f for f in os.listdir('.') if f.endswith('.csv') and f != 'uploaded_file.csv']
                zip_file_path = 'processed_files.zip'
                create_zip_file(processed_files, zip_file_path)
                return HttpResponseRedirect('/success/')
            else:
                return HttpResponseRedirect('/invalid_file/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def success_view(request):
    processed_files = [f for f in os.listdir('.') if f.endswith('.csv') and f != 'uploaded_file.csv']
    return render(request, 'success.html', {'processed_files': processed_files})


def invalid_file_view(request):
    return render(request, 'invalid_file.html')


def download_file(request):
    file_path = 'processed_files.zip'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def download_single_file(request, filename):
    zip_file_path = 'processed_files.zip'
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            if filename in zipf.namelist():
                content_type, _ = mimetypes.guess_type(filename)
                response = HttpResponse(zipf.read(filename), content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                return response
    raise Http404
