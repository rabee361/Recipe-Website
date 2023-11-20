# Generated by Django 4.2.5 on 2023-09-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_author_alter_ingredient_name_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=1500),
        ),
    ]