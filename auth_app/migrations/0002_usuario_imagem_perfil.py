# Generated by Django 5.1.3 on 2024-12-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagem_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_perfil/'),
        ),
    ]
