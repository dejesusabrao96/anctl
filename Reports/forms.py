from django import forms
from django.utils import timezone
from .models import Relatoriu, TipuRelatoriu
import os

class RelatoriuForm(forms.ModelForm):
    class Meta:
        model = Relatoriu
        fields = ['titulu', 'deskrisaun', 'tipu_relatoriu', 'arquivu_pdf', 'data']
        widgets = {
            'titulu': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Foti naran relatóriu nian...',
            }),
            'deskrisaun': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Deskrisaun kona-ba konteúdu relatóriu nian...',
                'rows': 4
            }),
            'tipu_relatoriu': forms.Select(attrs={
                'class': 'form-select',
            }),
            'arquivu_pdf': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf'
            }),
            'data': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipu_relatoriu'].queryset = TipuRelatoriu.objects.all().order_by('naran')
        self.fields['tipu_relatoriu'].empty_label = "Hili tipu relatóriu..."

    def clean_titulu(self):
        titulu = self.cleaned_data.get('titulu')
        if len(titulu) < 5:
            raise forms.ValidationError("Títulu tenke iha liu karakter 5.")
        return titulu

    def clean_arquivu_pdf(self):
        arquivu_pdf = self.cleaned_data.get('arquivu_pdf')
        if arquivu_pdf:
            if arquivu_pdf.size > 90 * 1024 * 1024:
                raise forms.ValidationError("Tamanha arquivu la bele liu 90MB.")
            
            extension = os.path.splitext(arquivu_pdf.name)[1].lower()
            if extension != '.pdf':
                raise forms.ValidationError("Deit bele upload arquivu PDF.")
        return arquivu_pdf

    def clean_data(self):
        data = self.cleaned_data.get('data')
        if data:
            try:
                # Konverte data input ba timezone aware
                from django.utils import timezone
                data_aware = timezone.make_aware(data) if timezone.is_naive(data) else data
                agora = timezone.now()
                
                if data_aware > agora:
                    raise forms.ValidationError("Data la bele iha futuru.")
            except Exception:
                # Se error, skip validasaun
                pass
        return data