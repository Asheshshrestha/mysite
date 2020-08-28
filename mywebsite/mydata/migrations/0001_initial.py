# Generated by Django 2.2.2 on 2020-08-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('carrer_status', models.CharField(max_length=30, null=True)),
                ('short_desc', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField(null=True)),
                ('phone', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('fb_link', models.URLField(null=True)),
                ('tw_link', models.URLField(null=True)),
                ('lin_link', models.URLField(null=True)),
            ],
        ),
    ]
