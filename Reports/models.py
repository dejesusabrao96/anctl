from django.db import models

class TipuRelatoriu(models.Model):
    naran = models.CharField(max_length=100)
    deskrisaun = models.TextField(blank=True)
    def __str__(self):
        return self.naran
    class Meta:
        verbose_name_plural = "Tipu Relatorius"

class Relatoriu(models.Model):
    titulu = models.CharField(max_length=200)
    deskrisaun = models.TextField(blank=True)
    tipu_relatoriu = models.ForeignKey(TipuRelatoriu, on_delete=models.SET_NULL, null=True, blank=True)
    arquivu_pdf = models.FileField(upload_to='relatorius/pdfs/')
    data= models.DateTimeField(null=True, blank=True)
    hashed = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.titulu
    class Meta:
        verbose_name_plural = "Relatorius"
