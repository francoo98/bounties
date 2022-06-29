# Generated by Django 4.0.5 on 2022-06-29 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bounties', '0008_alter_solution_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='awarded_solution',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='bounties.solution'),
        ),
    ]
