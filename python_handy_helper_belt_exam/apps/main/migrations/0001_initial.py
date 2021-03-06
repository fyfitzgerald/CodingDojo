# Generated by Django 2.1.1 on 2018-09-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_created', models.ForeignKey(on_delete='models.CASCADE', related_name='job_created', to='loginreg.User')),
                ('user_taking', models.ManyToManyField(related_name='job_user_taking', to='loginreg.User')),
            ],
        ),
    ]
