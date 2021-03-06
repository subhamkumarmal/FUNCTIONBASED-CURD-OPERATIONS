# Generated by Django 3.2.5 on 2021-07-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('city', models.CharField(max_length=30)),
                ('castVote', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'votervotes',
            },
        ),
    ]
