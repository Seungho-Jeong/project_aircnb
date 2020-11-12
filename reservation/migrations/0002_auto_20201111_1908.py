# Generated by Django 3.1.2 on 2020-11-11 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('reservation', '0001_initial'),
        ('stay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancellation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='booking',
            name='stay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stay.stay'),
        ),
    ]