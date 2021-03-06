# Generated by Django 3.0 on 2019-12-08 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=80)),
                ('type', models.CharField(max_length=30)),
                ('beds', models.CharField(max_length=100)),
                ('price', models.PositiveSmallIntegerField(blank=True, default=None, null=True)),
                ('destription', models.TextField(blank=True, null=True)),
                ('booker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_booker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
