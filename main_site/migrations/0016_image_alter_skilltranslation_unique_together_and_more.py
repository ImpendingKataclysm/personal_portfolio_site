# Generated by Django 4.2.6 on 2023-10-18 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0015_siteowner_siteownertranslation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='skilltranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='skilltranslation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='portfolioprojecttranslation',
            name='image',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='SkillTranslation',
        ),
        migrations.AddField(
            model_name='portfolioproject',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='portfolio_projects', to='main_site.image'),
        ),
    ]
