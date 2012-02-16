
from south.db import db
from django.db import models
from subscription.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'UserSubscription'
        db.create_table('subscription_usersubscription', (
            ('id', orm['subscription.UserSubscription:id']),
            ('user', orm['subscription.UserSubscription:user']),
            ('subscription', orm['subscription.UserSubscription:subscription']),
            ('expires', orm['subscription.UserSubscription:expires']),
            ('active', orm['subscription.UserSubscription:active']),
            ('cancelled', orm['subscription.UserSubscription:cancelled']),
        ))
        db.send_create_signal('subscription', ['UserSubscription'])
        
        # Adding model 'Transaction'
        db.create_table('subscription_transaction', (
            ('id', orm['subscription.Transaction:id']),
            ('timestamp', orm['subscription.Transaction:timestamp']),
            ('subscription', orm['subscription.Transaction:subscription']),
            ('user', orm['subscription.Transaction:user']),
            ('event', orm['subscription.Transaction:event']),
            ('amount', orm['subscription.Transaction:amount']),
            ('comment', orm['subscription.Transaction:comment']),
        ))
        db.send_create_signal('subscription', ['Transaction'])
        
        # Adding model 'Subscription'
        db.create_table('subscription_subscription', (
            ('id', orm['subscription.Subscription:id']),
            ('name', orm['subscription.Subscription:name']),
            ('description', orm['subscription.Subscription:description']),
            ('price', orm['subscription.Subscription:price']),
            ('recurrence_period', orm['subscription.Subscription:recurrence_period']),
            ('recurrence_unit', orm['subscription.Subscription:recurrence_unit']),
            ('group', orm['subscription.Subscription:group']),
        ))
        db.send_create_signal('subscription', ['Subscription'])
        
        # Creating unique_together for [user, subscription] on UserSubscription.
        db.create_unique('subscription_usersubscription', ['user_id', 'subscription_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'UserSubscription'
        db.delete_table('subscription_usersubscription')
        
        # Deleting model 'Transaction'
        db.delete_table('subscription_transaction')
        
        # Deleting model 'Subscription'
        db.delete_table('subscription_subscription')
        
        # Deleting unique_together for [user, subscription] on UserSubscription.
        db.delete_unique('subscription_usersubscription', ['user_id', 'subscription_id'])
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'subscription.subscription': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.Group']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '64', 'decimal_places': '2'}),
            'recurrence_period': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recurrence_unit': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'})
        },
        'subscription.transaction': {
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '64', 'decimal_places': '2', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subscription.Subscription']", 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'subscription.usersubscription': {
            'Meta': {'unique_together': "(('user', 'subscription'),)"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'cancelled': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'expires': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['subscription.Subscription']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }
    
    complete_apps = ['subscription']
