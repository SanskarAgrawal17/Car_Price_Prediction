# Generated by Django 4.2.5 on 2023-10-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('carapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='groups',
            field=models.ManyToManyField(related_name='newuser_set', related_query_name='newuser', to='auth.group'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_permissions',
            field=models.ManyToManyField(related_name='newuser_set', related_query_name='newuser', to='auth.permission'),
        ),
    ]
