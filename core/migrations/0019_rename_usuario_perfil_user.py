# Generated by Django 4.2.2 on 2023-07-11 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_rename_user_perfil_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuario',
            new_name='user',
        ),
    ]
