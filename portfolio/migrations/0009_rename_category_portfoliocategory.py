# Generated by Django 5.0.6 on 2024-07-12 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_team_alter_portfolio_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='PortfolioCategory',
        ),
    ]
