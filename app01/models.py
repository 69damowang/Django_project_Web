from django.db import models

class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name="标题",max_length=32)

class UserInfo(models.Model):
    '''员工表'''
    name = models.CharField(verbose_name="姓名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")


    #1. django自动写入
    # 生成数据列 depart_id
    #2. 部门表删除，员工信息自动删除
    depart= models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)

    # django的约束，只能选1或2
    gender_choices = (
        (1,"男"),
        (2,"女")
    )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)

