from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField("Nama Kursus", max_length=255)
    description = models.TextField("Deskripsi")
    price = models.DecimalField("Harga", max_digits=10, decimal_places=2)
    image = models.ImageField("Gambar", upload_to="course", blank=True, null=True)
    teacher = models.ForeignKey(User, verbose_name="Pengajar", on_delete=models.RESTRICT)
    created_at = models.DateTimeField("Dibuat pada", auto_now_add=True)
    updated_at = models.DateTimeField("Diubah pada", auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kursus"
        verbose_name_plural = "Data Kursus"
        ordering = ["-created_at"]