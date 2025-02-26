# Generated by Django 4.2.6 on 2024-04-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_afecteduser_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cyberattack',
            name='attackType',
            field=models.TextField(blank=True, null=True, verbose_name='Tipo de Ataque'),
        ),
        migrations.AddField(
            model_name='cyberattack',
            name='idsIpsAlerts',
            field=models.BooleanField(blank=True, null=True, verbose_name='Alertas IDS/IPS'),
        ),
    ]
