# Generated by Django 4.1.7 on 2023-04-14 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_delete_bids_delete_comments_listing_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="createdby",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name="Bids",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bid", models.DecimalField(decimal_places=2, max_digits=5)),
                ("biduser", models.IntegerField()),
                ("status", models.BooleanField(default=False)),
                (
                    "bid_listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="auctions.listing",
                    ),
                ),
            ],
        ),
    ]
