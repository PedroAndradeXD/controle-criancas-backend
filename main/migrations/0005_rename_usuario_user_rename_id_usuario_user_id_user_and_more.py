# Generated by Django 5.1.2 on 2024-11-14 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_usuario_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='id_usuario',
            new_name='id_user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='senha',
            new_name='password',
        ),
    ]
