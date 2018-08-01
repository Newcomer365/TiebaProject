# Generated by Django 2.0.7 on 2018-08-01 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tieba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('tid', models.IntegerField()),
                ('isSign', models.BooleanField(default=False)),
                ('isLike', models.BooleanField(default=False)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bduss', models.CharField(max_length=192)),
                ('username', models.CharField(max_length=30, verbose_name='用户名')),
                ('openid', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('idDel', models.BooleanField(default=False)),
                ('tb', models.ManyToManyField(to='Sign.Tieba')),
            ],
        ),
    ]
