#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import random
from random import randint
os.system('clear')
b=0
list=[]
sist=[]
bist=[]
t=0
x=0
print os.getcwd()

print "Adam Asmaca oyununa hoşgeldiniz!"
a=raw_input("Kelime otomatik mi oluşturulsun?")
if a == "evet" or a == "Evet" or a == "yes" or a == "Yes" or a == "y" or a == "Y" or a == "e" or a == "E" or a == "ev" or a == "Ev":
    b=1
if a == "hayır" or a == "Hayır" or a == "no" or a == "No" or a == "n" or a == "N" or a == "h" or a == "H" or a == "ha" or a == "Ha":
    b=2

if b == 2:
    k=raw_input("Kelime: ")
if b == 1:
    f = open('turkish.txt' , 'r')
    r=[]
    for line in f:
        r.append(line)
    y=randint(0,26123)
    k=r[y]
    k=k.replace("\n" ,"")
l=len(k)
for i in range (0,l):
    list.append(k[i])
for i in range (0,l):
    sist.append("*")
os.system('clear')

def oyun():
    os.system('clear')
    global t
    global x
    print "Kelime %s harfli" %(l) ,sist
    print "Hak:",6-t
    print "Kullanılan kelimeler:",bist
    z=raw_input("Tahmin:")
    if z == k:
        print "Doğru tahmin"
        print "Kelime %s idi" %(k)
        exit()
    if z != k:
        if z == "":
            pass
        else:
            print "Yanlış tahmin"
            t=t+1
            print "Hak:",6-t
    s=raw_input("Harf:")
    for i in range (0,l):
        if list[i] == s:
            sist[i] = s
            x=x+1
    if s == "":
        x=x+1
    if x == 0:
        print "Yanlış harf"
        t=t+1
        bist.append(s)
        print "Hak:",6-t
    x=0
while t != 6:
    oyun()
print "Adam asıldı"
print "Kelime %s idi" %(k)
exit()
