# Generated by Django 5.1.3 on 2024-12-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
