# Generated by Django 5.0.4 on 2024-05-27 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sesion',
            old_name='fechadeinicio',
            new_name='fechaclase',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='enlacedesesion',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='fechadetermino',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='horadeinicio',
        ),
        migrations.RemoveField(
            model_name='sesion',
            name='horadetermino',
        ),
        migrations.AddField(
            model_name='sesion',
            name='contacto',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='sesion',
            name='mensaje',
            field=models.TextField(default=''),
        ),
    ]
