# Generated by Django 4.2.6 on 2023-10-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='logo',
            field=models.ImageField(default='', storage='media', upload_to=''),
            preserve_default=False,
        ),
    ]
