# Generated by Django 2.2.10 on 2020-02-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200213_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/categories'),
        ),
    ]
