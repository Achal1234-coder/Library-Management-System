# Generated by Django 2.1.4 on 2021-06-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='published_year',
        ),
        migrations.AddField(
            model_name='books',
            name='book_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]