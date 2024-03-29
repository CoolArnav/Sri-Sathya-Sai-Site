# Generated by Django 4.2 on 2023-05-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_song_raga_alter_song_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='deity_image',
            field=models.ImageField(default='default.png', upload_to='media/deity_images'),
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(max_length=10000, upload_to='media/songs'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sortfilter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
