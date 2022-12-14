# Generated by Django 4.1 on 2022-08-29 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('mobile', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.TextField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
