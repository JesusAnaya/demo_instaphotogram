# Generated by Django 2.1.3 on 2018-11-28 03:12

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
