# Generated by Django 2.2.6 on 2019-10-28 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogapp.Post'),
        ),
    ]