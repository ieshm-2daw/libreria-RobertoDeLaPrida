# Generated by Django 4.2.7 on 2023-12-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
