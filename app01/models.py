from django.db import models

# Create your models here.

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        db_table = 'test'
        verbose_name = '测试'
        verbose_name_plural = '测试'




# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False   # 这个属性是通知django，不需要进行从模型到数据库的迁移管理
#         db_table = 'django_session'  # 对应的数据库中的表名