# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FTPUser'
        db.create_table(u'core_ftpuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('homedir', self.gf('filebrowser.fields.FileBrowseField')(max_length=256)),
            ('quota', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('upload_limit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('download_limit', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(default='*', max_length=15)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('ftppass', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ftpuid', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ftpgid', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'core', ['FTPUser'])

        # Adding M2M table for field groups on 'FTPUser'
        m2m_table_name = db.shorten_name(u'core_ftpuser_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ftpuser', models.ForeignKey(orm[u'core.ftpuser'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ftpuser_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'FTPUser'
        m2m_table_name = db.shorten_name(u'core_ftpuser_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ftpuser', models.ForeignKey(orm[u'core.ftpuser'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ftpuser_id', 'permission_id'])

        # Adding model 'FTPClient'
        db.create_table(u'core_ftpclient', (
            (u'ftpuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.FTPUser'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['FTPClient'])

        # Adding model 'FTPStaff'
        db.create_table(u'core_ftpstaff', (
            (u'ftpuser_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.FTPUser'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['FTPStaff'])


    def backwards(self, orm):
        # Deleting model 'FTPUser'
        db.delete_table(u'core_ftpuser')

        # Removing M2M table for field groups on 'FTPUser'
        db.delete_table(db.shorten_name(u'core_ftpuser_groups'))

        # Removing M2M table for field user_permissions on 'FTPUser'
        db.delete_table(db.shorten_name(u'core_ftpuser_user_permissions'))

        # Deleting model 'FTPClient'
        db.delete_table(u'core_ftpclient')

        # Deleting model 'FTPStaff'
        db.delete_table(u'core_ftpstaff')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.ftpclient': {
            'Meta': {'object_name': 'FTPClient', '_ormbases': [u'core.FTPUser']},
            u'ftpuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.FTPUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.ftpstaff': {
            'Meta': {'object_name': 'FTPStaff', '_ormbases': [u'core.FTPUser']},
            u'ftpuser_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.FTPUser']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.ftpuser': {
            'Meta': {'object_name': 'FTPUser'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'download_limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ftpgid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ftppass': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ftpuid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'homedir': ('filebrowser.fields.FileBrowseField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '15'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'quota': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upload_limit': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['core']