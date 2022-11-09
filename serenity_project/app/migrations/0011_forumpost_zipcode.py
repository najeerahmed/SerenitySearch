# Generated by Django 3.2.16 on 2022-11-01 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("app", "0010_rename_discussion_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="forumpost",
            name="zipcode",
            field=models.ForeignKey(
                blank=True,
                default=11201,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.scoretable",
            ),
            preserve_default=False,
        ),
    ]