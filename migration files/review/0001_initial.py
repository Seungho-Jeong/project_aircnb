# Generated by Django 3.1.2 on 2020-11-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField(auto_now=True)),
                ('body', models.CharField(max_length=2000)),
                ('cleanliness_star', models.IntegerField()),
                ('communication_star', models.IntegerField()),
                ('checkin_star', models.IntegerField()),
                ('accuracy_star', models.IntegerField()),
                ('location_star', models.IntegerField()),
                ('value_star', models.IntegerField()),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
    ]
