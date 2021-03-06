# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champions',
            fields=[
                ('id', models.CharField(blank=True, editable=False, max_length=4, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('partype', models.TextField(blank=True, null=True)),
                ('tags_1', models.TextField(blank=True, null=True)),
                ('tags_2', models.TextField(blank=True, null=True)),
                ('info_difficulty', models.IntegerField(blank=True, null=True)),
                ('info_attack', models.IntegerField(blank=True, null=True)),
                ('info_defense', models.IntegerField(blank=True, null=True)),
                ('info_magic', models.IntegerField(blank=True, null=True)),
                ('stats_armorperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_attackdamage', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_mpperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_attackspeedoffset', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_mp', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_armor', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_hp', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_hpregenperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_attackspeedperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_attackrange', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_movespeed', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_attackdamageperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_mpregenperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_critperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_spellblockperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_crit', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_mpregen', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_spellblock', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_hpregen', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('stats_hpperlevel', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('img_url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
