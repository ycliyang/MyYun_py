#-*-  coding:utf-8 -*-

from django.shortcuts import render,render_to_response
import hashlib,random,string,models.UCenter_members

def index(request):
    return render_to_response("uCenter/uCenterIndex.html");

def createUser(request):
    name = request.GET.get('name')
    # salt = GenPassword(6)
    salt="d5792f"
    md5Str = hashlib.md5(name).hexdigest()
    md5SaltStr = hashlib.md5(md5Str+salt).hexdigest();
    return render_to_response("uCenter/createUser.html",{'name':name,'salt': salt,'md5Str':md5Str,'md5SaltStr':md5SaltStr})

# def findAllUsers(request):
#     list = models.UCenter_members.objects.all()
#     return render_to_response("uCenter/UserList.html",{"list":list})



def GenPassword(length):
    #随机出数字的个数
    numOfNum = random.randint(1,length-1)
    numOfLetter = length - numOfNum
    #选中numOfNum个数字
    slcNum = [random.choice(string.digits) for i in range(numOfNum)]
    #选中numOfLetter个字母
    slcLetter = [random.choice(string.ascii_letters) for i in range(numOfLetter)]
    #打乱这个组合
    slcChar = slcNum + slcLetter
    random.shuffle(slcChar)
    #生成密码
    genPwd = ''.join([i for i in slcChar])
    return genPwd
