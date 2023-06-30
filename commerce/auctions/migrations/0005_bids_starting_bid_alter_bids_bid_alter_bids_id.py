# Generated by Django 4.1.7 on 2023-04-17 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_listing_createdby_alter_listing_id_bids"),
    ]

    operations = [
        migrations.AddField(
            model_name="bids",
            name="starting_bid",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="bids",
            name="bid",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="bids",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]