# Generated by Django 3.0.7 on 2020-09-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Restaurant', 'Restaurant'), ('Public', 'Public'), ('Hotel', 'Hotel')], default=None, max_length=120)),
                ('place', models.CharField(max_length=120)),
                ('overal_tidiness', models.IntegerField(default=0)),
                ('overal_space', models.IntegerField(default=0)),
                ('overal_smell', models.IntegerField(default=0)),
                ('overal_design', models.IntegerField(default=0)),
                ('overal_rating', models.FloatField(default=0)),
            ],
        ),
    ]
