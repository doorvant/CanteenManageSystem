from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Adding(models.Model):
    goodid = models.OneToOneField('Good', models.DO_NOTHING, db_column='goodId', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Orderlist', models.DO_NOTHING, db_column='orderId')  # Field name made lowercase.
    goodnum = models.IntegerField(db_column='goodNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = True
        db_table = 'adding'
        unique_together = (('goodid', 'orderid'),)


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class Canteen(models.Model):
    cname = models.TextField(db_column='cName')  # Field name made lowercase.
    cinfo = models.TextField(db_column='cInfo', blank=True, null=True)  # Field name made lowercase.
    caddr = models.TextField(db_column='cAddr', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(db_column='cId', primary_key=True)  # Field name made lowercase.
    rootid = models.ForeignKey('Root', models.DO_NOTHING, db_column='rootId')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'canteen'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         # managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         # managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         # managed = False
#         db_table = 'django_session'


class Food(models.Model):
    foodname = models.TextField(db_column='foodName')  # Field name made lowercase.
    foodprice = models.IntegerField(db_column='foodPrice')  # Field name made lowercase.
    foodsold = models.IntegerField(db_column='foodSold', blank=True, null=True)  # Field name made lowercase.
    foodinfo = models.TextField(db_column='foodInfo', blank=True, null=True)  # Field name made lowercase.
    foodcate = models.TextField(db_column='foodCate')  # Field name made lowercase.
    foodid = models.IntegerField(db_column='foodId', primary_key=True)  # Field name made lowercase.
    wid = models.ForeignKey('Windows', models.DO_NOTHING, db_column='wId')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'food'


class Good(models.Model):
    goodname = models.TextField(db_column='goodName')  # Field name made lowercase.
    goodprice = models.FloatField(db_column='goodPrice', blank=True, null=True)  # Field name made lowercase.
    goodinfo = models.TextField(db_column='goodInfo', blank=True, null=True)  # Field name made lowercase.
    goodsold = models.IntegerField(db_column='goodSold', blank=True, null=True)  # Field name made lowercase.
    goodid = models.IntegerField(db_column='goodId', primary_key=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'good'


class Including(models.Model):
    foodid = models.OneToOneField(Food, models.DO_NOTHING, db_column='foodId', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Orderlist', models.DO_NOTHING, db_column='orderId')  # Field name made lowercase.
    foodnum = models.IntegerField(db_column='foodNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'including'
        unique_together = (('foodid', 'orderid'),)


class Orderlist(models.Model):
    orderid = models.IntegerField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    userphone = models.ForeignKey('Userinfo', models.DO_NOTHING, db_column='userPhone')  # Field name made lowercase.
    ordernum = models.IntegerField(db_column='orderNum')  # Field name made lowercase.
    ordersum = models.FloatField(db_column='orderSum')  # Field name made lowercase.
    ordertext = models.TextField(db_column='orderText', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'orderlist'


class Root(models.Model):
    rootid = models.DecimalField(db_column='rootId', primary_key=True, max_digits=5, decimal_places=0)  # Field name made lowercase.
    rootpw = models.CharField(db_column='rootPw', max_length=20)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'root'


class Scoring(models.Model):
    userphone = models.OneToOneField('Userinfo', models.DO_NOTHING, db_column='userPhone', primary_key=True)  # Field name made lowercase.
    wid = models.ForeignKey('Windows', models.DO_NOTHING, db_column='wId')  # Field name made lowercase.
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'scoring'
        unique_together = (('userphone', 'wid'),)


class Userinfo(models.Model):
    username = models.CharField(db_column='userName', max_length=10)  # Field name made lowercase.
    userpw = models.CharField(db_column='userPw', max_length=20)  # Field name made lowercase.
    userphone = models.DecimalField(db_column='userPhone', primary_key=True, max_digits=11, decimal_places=0)  # Field name made lowercase.
    viplv = models.ForeignKey('Vip', models.DO_NOTHING, db_column='vipLv')  # Field name made lowercase.
    userdate = models.DateField(db_column='userDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'userinfo'


class Vip(models.Model):
    viplv = models.DecimalField(db_column='vipLv', primary_key=True, max_digits=1, decimal_places=0)  # Field name made lowercase.
    rootid = models.ForeignKey(Root, models.DO_NOTHING, db_column='rootId')  # Field name made lowercase.
    vipdiscount = models.FloatField(db_column='vipDiscount')  # Field name made lowercase.
    vipscore = models.IntegerField(db_column='vipScore', blank=True, null=True)  # Field name made lowercase.
    vipcount = models.IntegerField(db_column='vipCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'vip'


class Windows(models.Model):
    wname = models.TextField(db_column='wName')  # Field name made lowercase.
    wscore = models.IntegerField(db_column='wScore')  # Field name made lowercase.
    winfo = models.TextField(db_column='wInfo', blank=True, null=True)  # Field name made lowercase.
    wscorenum = models.IntegerField(db_column='wScoreNum')  # Field name made lowercase.
    wtotalscore = models.IntegerField(db_column='wTotalScore', blank=True, null=True)  # Field name made lowercase.
    wid = models.IntegerField(db_column='wId', primary_key=True)  # Field name made lowercase.
    cid = models.ForeignKey(Canteen, models.DO_NOTHING, db_column='cId')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'windows'


class Vieworderfood(models.Model):
    foodid = models.OneToOneField(Food, models.DO_NOTHING, db_column='foodId',
                                  primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Orderlist', models.DO_NOTHING, db_column='orderId')  # Field name made lowercase.
    foodnum = models.IntegerField(db_column='foodNum', blank=True, null=True)  # Field name made lowercase.
    foodname = models.TextField(db_column='foodName')  # Field name made lowercase.
    foodprice = models.IntegerField(db_column='foodPrice')  # Field name made lowercase.
    foodcate = models.TextField(db_column='foodCate')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'vieworderfood'


class Viewordergood(models.Model):
    goodid = models.OneToOneField(Good, models.DO_NOTHING, db_column='goodId',
                                  primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey('Orderlist', models.DO_NOTHING, db_column='orderId')  # Field name made lowercase.
    goodnum = models.IntegerField(db_column='goodNum', blank=True, null=True)  # Field name made lowercase.
    goodname = models.TextField(db_column='goodName')  # Field name made lowercase.
    goodprice = models.IntegerField(db_column='goodPrice')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'viewordergood'


class Viewfoodsold(models.Model):
    foodid = models.IntegerField(db_column='foodId', primary_key=True)  # Field name made lowercase.
    foodname = models.TextField(db_column='foodName')  # Field name made lowercase.
    foodmoney = models.IntegerField(db_column='foodMoney')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'viewfoodsold'


class Viewgoodsold(models.Model):
    goodid = models.IntegerField(db_column='goodId', primary_key=True)  # Field name made lowercase.
    goodname = models.TextField(db_column='goodName')  # Field name made lowercase.
    goodmoney = models.IntegerField(db_column='goodMoney')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'viewgoodsold'


class Viewscore(models.Model):
    wid = models.IntegerField(db_column='wId', primary_key=True)  # Field name made lowercase.
    wname = models.TextField(db_column='wName')  # Field name made lowercase.
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'viewscore'