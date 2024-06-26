


from django.db import models
import datetime

class JobTitle(models.Model):
    name = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=50)
    head = models.ForeignKey('User', on_delete=models.PROTECT)


class Task(models.Model):
    MADE = 'Готово'
    PROGRESS = 'В процессе'
    INTALK = 'В обсуждении'
    STAGES = [
        (MADE,"Готово"),
        (PROGRESS,"В процессе"),
        (INTALK,"В обсуждении"),
    ]

    project_id = models.ForeignKey('Project', on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    hoursToAccomplish = models.IntegerField(default=0)
    stageAt = models.CharField(max_length=20,choices=STAGES,default=INTALK)
    priority = models.IntegerField(default=0)
    workers = models.ManyToManyField('User')
    created_at = models.DateTimeField(default=datetime.datetime.now())
    finished_at = models.DateTimeField(null=True)

class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    members = models.ManyToManyField('User')
    created_at = models.DateTimeField(default=datetime.datetime.now())

class Issue(models.Model):

    FIXED = 'Закрыто'
    NOT_FIXED = 'Открыто'
    STAGES = [
        (FIXED, "Closed"),
        (NOT_FIXED, "Open")
    ]

    project_id = models.ForeignKey('Project', on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=800)
    status = models.CharField(max_length=30, choices=STAGES, default=NOT_FIXED,null=True)
    author = models.ForeignKey("User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    finished_at = models.DateTimeField(null=True)

class User(models.Model):
    WORKER = 'W'
    BOSS = 'B'
    STAGES = [
        (WORKER,"Работник"),
        (BOSS,"Руководитель"),
    ]
    job_title_id = models.ForeignKey(JobTitle, on_delete=models.PROTECT)
    avatar = models.CharField(max_length=800,default="https://www.svgrepo.com/show/192244/man-user.svg")
    age = models.IntegerField(default=0)
    first_name = models.CharField(max_length=800)
    last_name = models.CharField(max_length=800)
    father_name = models.CharField(max_length=800)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 
    position = models.CharField(max_length=80 , choices=STAGES,default=WORKER)
    department_id = models.ForeignKey(Department, on_delete=models.PROTECT,null=True)
    
class UserWIthTask(models.Model):
    TASK = "T"
    ISSUE = "I"
    WORK_TYPES = [
        (TASK,"task"),
        (ISSUE,"issue"),
    ]
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    work_type = models.CharField(max_length=80 , choices=WORK_TYPES,default="T")
    work_id = models.ForeignKey(Task, on_delete=models.PROTECT)
    work_time = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now())