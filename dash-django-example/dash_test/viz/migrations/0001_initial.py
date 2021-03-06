# Generated by Django 2.2.1 on 2019-05-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('season', models.TextField(blank=True, null=True)),
                ('division', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('homeaway', models.TextField(blank=True, null=True)),
                ('team', models.TextField(blank=True, null=True)),
                ('opponent', models.TextField(blank=True, null=True)),
                ('goals', models.BigIntegerField(blank=True, null=True)),
                ('goals_opp', models.BigIntegerField(blank=True, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('points', models.BigIntegerField(blank=True, null=True)),
                ('h1_goals', models.TextField(blank=True, null=True)),
                ('h1_goals_opp', models.TextField(blank=True, null=True)),
                ('h1_result', models.TextField(blank=True, null=True)),
                ('h1_points', models.TextField(blank=True, null=True)),
                ('h2_goals', models.TextField(blank=True, null=True)),
                ('h2_goals_opp', models.TextField(blank=True, null=True)),
                ('h2_result', models.TextField(blank=True, null=True)),
                ('h2_points', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'results',
                'managed': False,
            },
        ),
    ]
