# Generated by Django 3.0.6 on 2020-05-31 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_tweet_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tweets.Tweet'),
        ),
    ]
