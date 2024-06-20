# Generated by Django 5.0.6 on 2024-06-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jjapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="profile_image",
        ),
        migrations.AddField(
            model_name="student",
            name="profile_photo",
            field=models.ImageField(blank=True, null=True, upload_to="profile_photos/"),
        ),
    ]