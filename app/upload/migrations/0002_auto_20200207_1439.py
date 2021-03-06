# Generated by Django 3.0.3 on 2020-02-07 14:39

from django.db import migrations, models
import hello_django.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPrivate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(storage=hello_django.storage_backends.PrivateMediaStorage(), upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(storage=hello_django.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
