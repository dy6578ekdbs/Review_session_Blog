# Generated by Django 3.2 on 2021-07-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_title', models.CharField(max_length=50)),
                ('time', models.DateTimeField(verbose_name='date published')),
                ('long_text', models.TextField()),
            ],
        ),
    ]
