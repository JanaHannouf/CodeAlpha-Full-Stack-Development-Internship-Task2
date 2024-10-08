# Generated by Django 5.1.1 on 2024-09-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postimages',
            old_name='images',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='postimages',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ManyToManyField(to='social.postimages'),
        ),
    ]
