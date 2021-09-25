# Generated by Django 3.2.7 on 2021-09-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('idpost', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=100)),
                ('datepost', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
    ]
