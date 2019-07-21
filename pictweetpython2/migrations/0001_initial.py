# Generated by Django 2.2.3 on 2019-07-20 05:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)])),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=140)),
                ('image', models.ImageField(upload_to='documents/')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tweet',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictweetpython2.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to='pictweetpython2.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=140)),
                ('created_at', models.DateTimeField()),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictweetpython2.Tweet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pictweetpython2.User')),
            ],
        ),
    ]
