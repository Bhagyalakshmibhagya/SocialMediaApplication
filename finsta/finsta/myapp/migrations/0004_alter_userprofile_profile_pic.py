# Generated by Django 4.1.7 on 2023-04-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_userprofile_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='/profilepics/female.jpg', upload_to='profie_pic'),
        ),
    ]
