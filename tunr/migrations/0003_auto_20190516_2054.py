# Generated by Django 2.2.1 on 2019-05-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_song'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='spotify',
            new_name='preview_url',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.TextField(null=True),
        ),
    ]
