# Generated by Django 5.0.3 on 2024-03-21 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_general'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='general',
            options={'verbose_name_plural': 'Información General'},
        ),
        migrations.AlterField(
            model_name='general',
            name='actualizacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]