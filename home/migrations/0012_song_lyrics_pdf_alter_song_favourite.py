# Generated by Django 4.1.7 on 2023-08-12 17:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_song_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics_pdf',
            field=models.FileField(max_length=1000000000, null=True, upload_to='lyrics'),
        ),
        migrations.AlterField(
            model_name='song',
            name='favourite',
            field=models.ManyToManyField(blank=True, editable=False, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
