# Generated by Django 2.1.4 on 2021-06-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=20)),
                ('writter', models.CharField(max_length=30)),
                ('published_year', models.DateField()),
                ('no_of_book', models.IntegerField()),
                ('image_of_book', models.ImageField(blank=True, upload_to='book/image')),
            ],
        ),
    ]
