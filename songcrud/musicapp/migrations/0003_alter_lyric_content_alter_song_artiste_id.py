# Generated by Django 4.1.2 on 2022-10-24 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_alter_song_artiste_id_alter_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artiste_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste'),
        ),
    ]