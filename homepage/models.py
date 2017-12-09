from django.db import models
from django.contrib import admin

# Create your models here.
class Champions(models.Model):
    id = models.CharField(primary_key=True, blank=True, unique=True, editable=False, max_length=4)
    name = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    partype = models.TextField(null=True, blank=True)
    tags_1 = models.TextField(null=True, blank=True)
    tags_2 = models.TextField(null=True, blank=True)
    info_difficulty = models.IntegerField(null=True, blank=True)
    info_attack = models.IntegerField(null=True, blank=True)
    info_defense = models.IntegerField(null=True, blank=True)
    info_magic = models.IntegerField(null=True, blank=True)
    stats_armorperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_attackdamage = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_mpperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_attackspeedoffset = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_mp = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_armor	= models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_hp = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_hpregenperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_attackspeedperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_attackrange = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_movespeed = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_attackdamageperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_mpregenperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_critperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_spellblockperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_crit = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_mpregen = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_spellblock = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_hpregen = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    stats_hpperlevel = models.DecimalField(null=True, blank=True,max_digits=7,decimal_places=4)
    img_url = models.TextField(null=True, blank=True)

admin.site.register(Champions)
