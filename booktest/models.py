from django.db import models

# Create your models here.

#在模型管理器中添加自定义方法：
class BookInfoManager(models.Manager):

    def insertBook(self, btitle, bdate):
        #book = BookInfo()
        book = self.model()
        book.btitle = btitle
        book.bput_date = bdate
        book.save()
        return book

#一对多模型类：
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bput_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcommit = models.IntegerField(default=0)
    bdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    class Mate:
        db_table = 'BookInfo'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hmajor = models.CharField(max_length=40)
    hbook = models.ForeignKey('BookInfo')

    def __str__(self):
        return self.hname

#多对多模型类：
# class NewsInfo(models.Model):
#     newsplace = models.DateField()

# class NewsType(models.Model):
#     newsname = models.CharField(max_length=20)
#     newsplace = models.CharField(max_length=30)
#     newsfund = models.ManyToManyField('NewsInfo')
    
# #一对一模型类：
# class EmployeeBasicInfo(models.Model):
#     employeeinfo = models.CharField(max_length=30)

# class EmployeeDetailInfo(models.Model):
#     employeedetail = models.CharField(max_length=50)
#     employeefund = models.OneToOneField('EmployeeBasicInfo')

#自关联：
class AreaInfo(models.Model):
    areaName = models.CharField(max_length=20)
    areaParent = models.ForeignKey('self', null=True, blank=True)
