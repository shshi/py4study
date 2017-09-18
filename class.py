#!/usr/bin/env python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: class.py
# Author：wangzhe
# E-mail: wangzhehyd@163.com
# Created Time: 2013-11-23
# Version: 1.0
# Description: 
# Copyright: Chemical Biology Research Center
#===========================================================
#类定义  
class people():  
    #定义基本属性  
    name = ''  
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问  
    __weight = 0 
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s is speaking: I am %d years old" %(self.name,self.age))

p = people('tom',10,30)
p.speak()
print p.name
print p.age
#私有属性无法外部访问报错
#print p.weight



#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d"%(self.name,self.age,self.grade))



s = student('ken',20,60,3)
s.speak()




#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("I am %s,I am a speaker!My topic is %s"%(self.name,self.topic))

#多重继承
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
#方法名同，默认调用的是在括号中排前地父类的方法
test.speak()





