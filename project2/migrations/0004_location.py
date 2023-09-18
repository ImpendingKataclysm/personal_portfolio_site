# Generated by Django 4.2.4 on 2023-09-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project2', '0003_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('postal', models.CharField(max_length=6)),
                ('province', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project1')),
            ],
        ),
    ]