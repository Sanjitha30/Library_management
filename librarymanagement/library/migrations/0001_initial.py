# Generated by Django 4.2.7 on 2024-01-04 07:39

import datetime
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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150)),
                ('author_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=1)),
                ('subject', models.CharField(max_length=2000)),
                ('book_add_time', models.TimeField(default=datetime.datetime(2024, 1, 4, 7, 39, 41, 248912, tzinfo=datetime.timezone.utc))),
                ('book_add_date', models.DateField(default=datetime.date(2024, 1, 4))),
            ],
            options={
                'unique_together': {('book_name', 'author_name')},
            },
        ),
        migrations.CreateModel(
            name='IssuedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(default=datetime.date(2024, 1, 4))),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
