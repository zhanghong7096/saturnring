# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Provisioner'
        db.create_table(u'ssdfrontend_provisioner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clientiqn', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sizeinGB', self.gf('django.db.models.fields.FloatField')()),
            ('serviceName', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ssdfrontend', ['Provisioner'])

        # Adding model 'LV'
        db.create_table(u'ssdfrontend_lv', (
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.Target'])),
            ('vg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.VG'])),
            ('lvname', self.gf('django.db.models.fields.CharField')(default='Not found', max_length=200)),
            ('lvsize', self.gf('django.db.models.fields.FloatField')()),
            ('lvuuid', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('lvthinmapped', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'ssdfrontend', ['LV'])

        # Adding model 'Lock'
        db.create_table(u'ssdfrontend_lock', (
            ('lockname', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('locked', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ssdfrontend', ['Lock'])

        # Adding model 'VG'
        db.create_table(u'ssdfrontend_vg', (
            ('vghost', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.StorageHost'])),
            ('vgsize', self.gf('django.db.models.fields.FloatField')()),
            ('vguuid', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('vgpesize', self.gf('django.db.models.fields.FloatField')()),
            ('vgtotalpe', self.gf('django.db.models.fields.FloatField')()),
            ('vgfreepe', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('thinusedpercent', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('thintotalGB', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('maxthinavlGB', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('opf', self.gf('django.db.models.fields.FloatField')(default=0.99)),
            ('thinusedmaxpercent', self.gf('django.db.models.fields.FloatField')(default=99)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('CurrentAllocGB', self.gf('django.db.models.fields.FloatField')(default=-100.0, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('is_locked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_error', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ssdfrontend', ['VG'])

        # Adding model 'StorageHost'
        db.create_table(u'ssdfrontend_storagehost', (
            ('dnsname', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('ipaddress', self.gf('django.db.models.fields.GenericIPAddressField')(default='127.0.0.1', max_length=39)),
            ('storageip1', self.gf('django.db.models.fields.GenericIPAddressField')(default='127.0.0.1', max_length=39)),
            ('storageip2', self.gf('django.db.models.fields.GenericIPAddressField')(default='127.0.0.1', max_length=39)),
            ('enabled', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'ssdfrontend', ['StorageHost'])

        # Adding model 'Target'
        db.create_table(u'ssdfrontend_target', (
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('targethost', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.StorageHost'])),
            ('iqnini', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('iqntar', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('sizeinGB', self.gf('django.db.models.fields.FloatField')(max_length=200)),
            ('sessionup', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rkb', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('rkbpm', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('wkb', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('wkbpm', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('storageip1', self.gf('django.db.models.fields.GenericIPAddressField')(default='127.0.0.1', max_length=39)),
            ('storageip2', self.gf('django.db.models.fields.GenericIPAddressField')(default='127.0.0.1', max_length=39)),
        ))
        db.send_create_signal(u'ssdfrontend', ['Target'])

        # Adding model 'TargetHistory'
        db.create_table(u'ssdfrontend_targethistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('iqntar', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('iqnini', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deleted_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('sizeinGB', self.gf('django.db.models.fields.FloatField')(max_length=200)),
            ('rkb', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('wkb', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
        ))
        db.send_create_signal(u'ssdfrontend', ['TargetHistory'])

        # Adding model 'AAGroup'
        db.create_table(u'ssdfrontend_aagroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.Target'], null=True, blank=True)),
        ))
        db.send_create_signal(u'ssdfrontend', ['AAGroup'])

        # Adding M2M table for field hosts on 'AAGroup'
        m2m_table_name = db.shorten_name(u'ssdfrontend_aagroup_hosts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('aagroup', models.ForeignKey(orm[u'ssdfrontend.aagroup'], null=False)),
            ('storagehost', models.ForeignKey(orm[u'ssdfrontend.storagehost'], null=False))
        ))
        db.create_unique(m2m_table_name, ['aagroup_id', 'storagehost_id'])

        # Adding model 'ClumpGroup'
        db.create_table(u'ssdfrontend_clumpgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.Target'], null=True, blank=True)),
        ))
        db.send_create_signal(u'ssdfrontend', ['ClumpGroup'])

        # Adding M2M table for field hosts on 'ClumpGroup'
        m2m_table_name = db.shorten_name(u'ssdfrontend_clumpgroup_hosts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clumpgroup', models.ForeignKey(orm[u'ssdfrontend.clumpgroup'], null=False)),
            ('storagehost', models.ForeignKey(orm[u'ssdfrontend.storagehost'], null=False))
        ))
        db.create_unique(m2m_table_name, ['clumpgroup_id', 'storagehost_id'])

        # Adding model 'IPRange'
        db.create_table(u'ssdfrontend_iprange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('iprange', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'ssdfrontend', ['IPRange'])

        # Adding M2M table for field hosts on 'IPRange'
        m2m_table_name = db.shorten_name(u'ssdfrontend_iprange_hosts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('iprange', models.ForeignKey(orm[u'ssdfrontend.iprange'], null=False)),
            ('storagehost', models.ForeignKey(orm[u'ssdfrontend.storagehost'], null=False))
        ))
        db.create_unique(m2m_table_name, ['iprange_id', 'storagehost_id'])

        # Adding model 'Interface'
        db.create_table(u'ssdfrontend_interface', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storagehost', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ssdfrontend.StorageHost'])),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
        ))
        db.send_create_signal(u'ssdfrontend', ['Interface'])

        # Adding M2M table for field iprange on 'Interface'
        m2m_table_name = db.shorten_name(u'ssdfrontend_interface_iprange')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('interface', models.ForeignKey(orm[u'ssdfrontend.interface'], null=False)),
            ('iprange', models.ForeignKey(orm[u'ssdfrontend.iprange'], null=False))
        ))
        db.create_unique(m2m_table_name, ['interface_id', 'iprange_id'])

        # Adding model 'Profile'
        db.create_table(u'ssdfrontend_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('max_target_sizeGB', self.gf('django.db.models.fields.FloatField')(default=5)),
            ('max_alloc_sizeGB', self.gf('django.db.models.fields.FloatField')(default=10)),
        ))
        db.send_create_signal(u'ssdfrontend', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Provisioner'
        db.delete_table(u'ssdfrontend_provisioner')

        # Deleting model 'LV'
        db.delete_table(u'ssdfrontend_lv')

        # Deleting model 'Lock'
        db.delete_table(u'ssdfrontend_lock')

        # Deleting model 'VG'
        db.delete_table(u'ssdfrontend_vg')

        # Deleting model 'StorageHost'
        db.delete_table(u'ssdfrontend_storagehost')

        # Deleting model 'Target'
        db.delete_table(u'ssdfrontend_target')

        # Deleting model 'TargetHistory'
        db.delete_table(u'ssdfrontend_targethistory')

        # Deleting model 'AAGroup'
        db.delete_table(u'ssdfrontend_aagroup')

        # Removing M2M table for field hosts on 'AAGroup'
        db.delete_table(db.shorten_name(u'ssdfrontend_aagroup_hosts'))

        # Deleting model 'ClumpGroup'
        db.delete_table(u'ssdfrontend_clumpgroup')

        # Removing M2M table for field hosts on 'ClumpGroup'
        db.delete_table(db.shorten_name(u'ssdfrontend_clumpgroup_hosts'))

        # Deleting model 'IPRange'
        db.delete_table(u'ssdfrontend_iprange')

        # Removing M2M table for field hosts on 'IPRange'
        db.delete_table(db.shorten_name(u'ssdfrontend_iprange_hosts'))

        # Deleting model 'Interface'
        db.delete_table(u'ssdfrontend_interface')

        # Removing M2M table for field iprange on 'Interface'
        db.delete_table(db.shorten_name(u'ssdfrontend_interface_iprange'))

        # Deleting model 'Profile'
        db.delete_table(u'ssdfrontend_profile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ssdfrontend.aagroup': {
            'Meta': {'object_name': 'AAGroup'},
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ssdfrontend.StorageHost']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.Target']", 'null': 'True', 'blank': 'True'})
        },
        u'ssdfrontend.clumpgroup': {
            'Meta': {'object_name': 'ClumpGroup'},
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ssdfrontend.StorageHost']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.Target']", 'null': 'True', 'blank': 'True'})
        },
        u'ssdfrontend.interface': {
            'Meta': {'object_name': 'Interface'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'iprange': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ssdfrontend.IPRange']", 'symmetrical': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'storagehost': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.StorageHost']"})
        },
        u'ssdfrontend.iprange': {
            'Meta': {'object_name': 'IPRange'},
            'hosts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ssdfrontend.StorageHost']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iprange': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ssdfrontend.lock': {
            'Meta': {'object_name': 'Lock'},
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lockname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        u'ssdfrontend.lv': {
            'Meta': {'object_name': 'LV'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'lvname': ('django.db.models.fields.CharField', [], {'default': "'Not found'", 'max_length': '200'}),
            'lvsize': ('django.db.models.fields.FloatField', [], {}),
            'lvthinmapped': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'lvuuid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.Target']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'vg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.VG']"})
        },
        u'ssdfrontend.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_alloc_sizeGB': ('django.db.models.fields.FloatField', [], {'default': '10'}),
            'max_target_sizeGB': ('django.db.models.fields.FloatField', [], {'default': '5'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'ssdfrontend.provisioner': {
            'Meta': {'object_name': 'Provisioner'},
            'clientiqn': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serviceName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sizeinGB': ('django.db.models.fields.FloatField', [], {})
        },
        u'ssdfrontend.storagehost': {
            'Meta': {'object_name': 'StorageHost'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'dnsname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ipaddress': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'storageip1': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'storageip2': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'ssdfrontend.target': {
            'Meta': {'object_name': 'Target'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'iqnini': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'iqntar': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'rkb': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'rkbpm': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'sessionup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sizeinGB': ('django.db.models.fields.FloatField', [], {'max_length': '200'}),
            'storageip1': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'storageip2': ('django.db.models.fields.GenericIPAddressField', [], {'default': "'127.0.0.1'", 'max_length': '39'}),
            'targethost': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.StorageHost']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'wkb': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'wkbpm': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        u'ssdfrontend.targethistory': {
            'Meta': {'object_name': 'TargetHistory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deleted_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iqnini': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'iqntar': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'rkb': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'sizeinGB': ('django.db.models.fields.FloatField', [], {'max_length': '200'}),
            'wkb': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        u'ssdfrontend.vg': {
            'CurrentAllocGB': ('django.db.models.fields.FloatField', [], {'default': '-100.0', 'null': 'True'}),
            'Meta': {'object_name': 'VG'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'in_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'maxthinavlGB': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'opf': ('django.db.models.fields.FloatField', [], {'default': '0.99'}),
            'thintotalGB': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'thinusedmaxpercent': ('django.db.models.fields.FloatField', [], {'default': '99'}),
            'thinusedpercent': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'vgfreepe': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'vghost': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ssdfrontend.StorageHost']"}),
            'vgpesize': ('django.db.models.fields.FloatField', [], {}),
            'vgsize': ('django.db.models.fields.FloatField', [], {}),
            'vgtotalpe': ('django.db.models.fields.FloatField', [], {}),
            'vguuid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'})
        }
    }

    complete_apps = ['ssdfrontend']