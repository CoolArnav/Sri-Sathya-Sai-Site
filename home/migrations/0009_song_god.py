# Generated by Django 4.2 on 2023-05-18 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_god_remove_song_deity_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='god',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.god'),
        ),
    ]
