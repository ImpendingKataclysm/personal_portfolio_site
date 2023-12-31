# Generated by Django 4.2.6 on 2023-11-10 20:52

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0017_remove_portfolioproject_images_image_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('caption', models.TextField(blank=True, max_length=200, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='main_site.image')),
            ],
            options={
                'verbose_name': 'image Translation',
                'db_table': 'main_site_image_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
