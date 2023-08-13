from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = [
        ('ADMIN', 'Yönetici'),
        ('AGENT', 'Acente'),
        ('SUBAGENT', 'Alt Acente'),
        ('USER', 'Kullanıcı'),
    ]
    role = models.CharField(choices=ROLES, max_length=10)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)  # Cinsiyet bilgisi için detaylandırma yapılabilir.
    marital_status = models.CharField(max_length=10)  # Medeni Durum için detaylandırma yapılabilir.
    education_status = models.CharField(max_length=30)  # Eğitim Durumu için detaylandırma yapılabilir.
    profession = models.CharField(max_length=100)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set",
        related_query_name="customuser",
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="customuser",
        verbose_name='user permissions'
    )