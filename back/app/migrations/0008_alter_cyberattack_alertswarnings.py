# Generated by Django 4.2.6 on 2024-04-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_cyberattack_device_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cyberattack',
            name='alertsWarnings',
            field=models.BooleanField(default=False, null=True, verbose_name='Alertas/Advertencias'),
        ),
    ]