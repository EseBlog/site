# Generated by Django 5.0.3 on 2024-03-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_general_options_alter_general_actualizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='etiqueta',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
    ]
