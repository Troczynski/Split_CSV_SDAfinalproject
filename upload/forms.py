from django import forms
from django.core.exceptions import ValidationError

class UploadFileForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': '.csv'}),
        label='Select CSV File'
    )

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.csv'):
            raise ValidationError('Invalid file format. Please upload a CSV file.')
        return file
