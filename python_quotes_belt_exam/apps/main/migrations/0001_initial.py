# Generated by Django 2.1.1 on 2018-09-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_created', models.ForeignKey(on_delete='models.CASCADE', related_name='quote_created', to='loginreg.User')),
                ('user_liking', models.ManyToManyField(related_name='quote_user_liking', to='loginreg.User')),
            ],
        ),
    ]
