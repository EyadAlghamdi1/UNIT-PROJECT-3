# Generated by Django 5.1.2 on 2024-11-26 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(choices=[('Jeddah', 'Jeddah'), ('Riyadh', 'Riyadh'), ('Dammam', 'Dammam'), ('Abha', 'Abha')], default='Jeddah', max_length=255),
        ),
    ]
