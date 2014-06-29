from django.db import models

# # Create your models here.
# class UCenter_members(models.Model):
#     uid = models.IntegerField(max_length=8)
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=32)
#     email = models.CharField(max_length=32)
#     myid = models.CharField(max_length=30)
#     myidkey = models.CharField(max_length=16)
#     regip = models.CharField(max_length=15)
#     regdate = models.IntegerField(max_length=10)
#     lastloginip = models.IntegerField(max_length=10)
#     lastlogintime = models.IntegerField(max_length=10)
#     salt = models.CharField(max_length=6)
#     secques = models.CharField(max_length=8)
#
#     def __init__(self,username,password,email,myid,myidkey,regip,regdate,lastloginip,lastlogintime,salt,secques):
#         self.username = username
#         self.password = password
#         self.salt = salt
#         self.email = email
#         self.myid = myid
#         self.myidkey = myidkey
#         self.regip = regip
#         self.regdate = regdate
#         self.lastloginip = lastloginip
#         self.lastlogintime = lastlogintime
#         self.secques = secques