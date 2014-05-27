#Copyright 2014 Blackberry Limited
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Provisioner(models.Model):
    clientiqn = models.CharField(max_length=100)
    sizeinGB = models.FloatField()
    serviceName = models.CharField(max_length=100)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.clientiqn


class LV(models.Model):
    target = models.ForeignKey('Target')
    vg = models.ForeignKey('VG')
    lvname = models.CharField(max_length=200,default='Not found')
    lvsize = models.FloatField()
    lvuuid = models.CharField(max_length=200,primary_key=True)
    lvthinmapped = models.FloatField(default=-1)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.lvname

class VG (models.Model):
    vghost = models.ForeignKey('StorageHost')
    vgsize = models.FloatField()
    vguuid = models.CharField(max_length=200,primary_key=True)
    vgpesize = models.FloatField()
    vgtotalpe = models.FloatField()
    vgfreepe = models.FloatField(default=-1)
    thinusedpercent = models.FloatField(default=-1)
    thintotalGB = models.FloatField(default=-1)
    maxthinavlGB = models.FloatField(default=-1)
    opf = models.FloatField(default=0.7)
    thinusedmaxpercent = models.FloatField(default=70)
    enabled = models.BooleanField(default=True)
    CurrentAllocGB = models.FloatField(default=-100.0)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.vguuid

class StorageHost(models.Model):
    dnsname = models.CharField(max_length=200,primary_key=True)
    ipaddress = models.GenericIPAddressField(default='127.0.0.1')
    storageip1 = models.GenericIPAddressField(default='127.0.0.1')
    storageip2 = models.GenericIPAddressField(default='127.0.0.1')
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.dnsname




class Target(models.Model):
    owner = models.ForeignKey(User)
    targethost= models.ForeignKey('StorageHost')
    iqnini = models.CharField(max_length=200)
    iqntar = models.CharField(max_length=200,primary_key=True)
    sizeinGB = models.FloatField(max_length=200)
    sessionup = models.BooleanField(default=False)
    rkb = models.BigIntegerField(default=0)
    rkbpm = models.BigIntegerField(default=0)
    wkb = models.BigIntegerField(default=0)
    wkbpm = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.iqntar



class AAGroup(models.Model):
    name = models.CharField(max_length=200)
    hosts = models.ManyToManyField(StorageHost)
    target = models.ForeignKey(Target,null=True, blank=True)

    def __unicode__(self):
        return self.name 

from django.contrib.auth.models import User

#http://www.igorsobreira.com/2010/12/11/extending-user-model-in-django.html
class Profile(models.Model):
    user = models.OneToOneField(User,unique=True)
    max_target_sizeGB = models.FloatField(default=100.0)
    max_alloc_sizeGB = models.FloatField(default=400.0)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

from django.db.models import signals
signals.post_save.connect(create_user_profile, sender=User,dispatch_uid='autocreate_nuser')
