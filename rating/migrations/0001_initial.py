# Generated by Django 3.0.7 on 2020-09-18 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toilet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tidiness', models.IntegerField(default=0)),
                ('space', models.IntegerField(default=0)),
                ('smell', models.IntegerField(default=0)),
                ('design', models.IntegerField(default=0)),
                ('toilet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toilet.Toilet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
