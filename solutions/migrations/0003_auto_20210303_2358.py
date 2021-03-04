# Generated by Django 3.1.6 on 2021-03-03 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_auto_20210219_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='file_one',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='file_three',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='file_two',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='image_one',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='image_three',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='image_two',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a name to identify this image', max_length=255)),
                ('image', models.ImageField(upload_to='solutions/images')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='solutions.solution')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a name to identify this file', max_length=255)),
                ('file', models.FileField(upload_to='solutions/files/')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='solutions.solution')),
            ],
        ),
    ]
