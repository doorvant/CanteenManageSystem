# Generated by Django 3.2.8 on 2021-10-28 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('cname', models.TextField(db_column='cName')),
                ('cinfo', models.TextField(blank=True, db_column='cInfo', null=True)),
                ('caddr', models.TextField(blank=True, db_column='cAddr', null=True)),
                ('cid', models.IntegerField(db_column='cId', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'canteen',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('goodname', models.TextField(db_column='goodName')),
                ('goodprice', models.FloatField(blank=True, db_column='goodPrice', null=True)),
                ('goodinfo', models.TextField(blank=True, db_column='goodInfo', null=True)),
                ('goodsold', models.IntegerField(blank=True, db_column='goodSold', null=True)),
                ('goodid', models.IntegerField(db_column='goodId', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'good',
            },
        ),
        migrations.CreateModel(
            name='Root',
            fields=[
                ('rootid', models.DecimalField(db_column='rootId', decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('rootpw', models.CharField(db_column='rootPw', max_length=20)),
            ],
            options={
                'db_table': 'root',
            },
        ),
        migrations.CreateModel(
            name='Windows',
            fields=[
                ('wname', models.TextField(db_column='wName')),
                ('wscore', models.IntegerField(db_column='wScore')),
                ('winfo', models.TextField(blank=True, db_column='wInfo', null=True)),
                ('wscorenum', models.IntegerField(db_column='wScoreNum')),
                ('wtotalscore', models.IntegerField(blank=True, db_column='wTotalScore', null=True)),
                ('wid', models.IntegerField(db_column='wId', primary_key=True, serialize=False)),
                ('cid', models.ForeignKey(db_column='cId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.canteen')),
            ],
            options={
                'db_table': 'windows',
            },
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('viplv', models.DecimalField(db_column='vipLv', decimal_places=0, max_digits=1, primary_key=True, serialize=False)),
                ('vipdiscount', models.FloatField(db_column='vipDiscount')),
                ('vipscore', models.IntegerField(blank=True, db_column='vipScore', null=True)),
                ('vipcount', models.IntegerField(blank=True, db_column='vipCount', null=True)),
                ('rootid', models.ForeignKey(db_column='rootId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.root')),
            ],
            options={
                'db_table': 'vip',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('username', models.CharField(db_column='userName', max_length=10)),
                ('userpw', models.CharField(db_column='userPw', max_length=20)),
                ('userphone', models.DecimalField(db_column='userPhone', decimal_places=0, max_digits=11, primary_key=True, serialize=False)),
                ('userdate', models.DateField(blank=True, db_column='userDate', null=True)),
                ('viplv', models.ForeignKey(db_column='vipLv', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.vip')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.CreateModel(
            name='Orderlist',
            fields=[
                ('orderid', models.IntegerField(db_column='orderId', primary_key=True, serialize=False)),
                ('ordernum', models.IntegerField(db_column='orderNum')),
                ('ordersum', models.FloatField(db_column='orderSum')),
                ('ordertext', models.TextField(blank=True, db_column='orderText', null=True)),
                ('userphone', models.ForeignKey(db_column='userPhone', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.userinfo')),
            ],
            options={
                'db_table': 'orderlist',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('foodname', models.TextField(db_column='foodName')),
                ('foodprice', models.IntegerField(db_column='foodPrice')),
                ('foodsold', models.IntegerField(blank=True, db_column='foodSold', null=True)),
                ('foodinfo', models.TextField(blank=True, db_column='foodInfo', null=True)),
                ('foodcate', models.TextField(db_column='foodCate')),
                ('foodid', models.IntegerField(db_column='foodId', primary_key=True, serialize=False)),
                ('wid', models.ForeignKey(db_column='wId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.windows')),
            ],
            options={
                'db_table': 'food',
            },
        ),
        migrations.AddField(
            model_name='canteen',
            name='rootid',
            field=models.ForeignKey(db_column='rootId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.root'),
        ),
        migrations.CreateModel(
            name='Scoring',
            fields=[
                ('userphone', models.OneToOneField(db_column='userPhone', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='canteenApp.userinfo')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('wid', models.ForeignKey(db_column='wId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.windows')),
            ],
            options={
                'db_table': 'scoring',
                'unique_together': {('userphone', 'wid')},
            },
        ),
        migrations.CreateModel(
            name='Including',
            fields=[
                ('foodid', models.OneToOneField(db_column='foodId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='canteenApp.food')),
                ('orderid', models.ForeignKey(db_column='orderId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.orderlist')),
            ],
            options={
                'db_table': 'including',
                'unique_together': {('foodid', 'orderid')},
            },
        ),
        migrations.CreateModel(
            name='Adding',
            fields=[
                ('goodid', models.OneToOneField(db_column='goodId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='canteenApp.good')),
                ('orderid', models.ForeignKey(db_column='orderId', on_delete=django.db.models.deletion.DO_NOTHING, to='canteenApp.orderlist')),
            ],
            options={
                'db_table': 'adding',
                'unique_together': {('goodid', 'orderid')},
            },
        ),
    ]