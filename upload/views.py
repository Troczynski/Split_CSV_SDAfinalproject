from django.shortcuts import render, HttpResponseRedirect, Http404,HttpResponse
from .forms import UploadFileForm
from .verified_file import verify_file
from .models import GeneratedFileLog
import os
import zipfile
from datetime import datetime
import mimetypes




def handle_uploaded_file(f):
    file_path = 'uploaded_file.csv'
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return file_path


def get_turbine_name_from_csv(csv_file):
    with open(csv_file, 'r') as f:
        first_line = f.readline().strip()
        second_line = f.readline().strip()
        file_type = second_line.split(',')[0]
        return file_type

def create_zip_file(files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))

def delete_previous_files():
    # Usunięcie plików CSV i plik ZIP z katalogu roboczego
    for file in os.listdir('.'):
        if file.endswith('.csv') or file.endswith('.zip'):
            os.remove(file)

def upload_file(request):
    success = '/success/'
    invalid_file = '/invalid_file/'
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Usunięcie starych plików
            delete_previous_files()

            file_path = handle_uploaded_file(request.FILES['file'])
            if verify_file(file_path):
                processed_files = [f for f in os.listdir('.') if f.endswith('.csv') and f != 'uploaded_file.csv']
                zip_file_path = 'processed_files.zip'
                create_zip_file(processed_files, zip_file_path)

                # Zapis logów do bazy danych
                for file in processed_files:
                    turbine_name = get_turbine_name_from_csv(file)
                    log_entry = GeneratedFileLog.objects.create(
                        file_type=turbine_name,
                        file_name=file,
                        generated_at=datetime.now()
                    )
                    log_entry.save()

                return HttpResponseRedirect(success)
            else:
                return HttpResponseRedirect(invalid_file)
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
