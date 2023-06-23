# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:42:32 2023

@author: DEV_KVCS
"""
print("\n\nFeladat - Megoldás merge script\n")
print("Ami kell: ")
print("1. fel.txt ,ebben vannak a feladatok szövegei, ß-el elválasztva, UTF-8!")
print("2. meg.txt ,ebben vannak a megoldások, ß-el elválasztva, UTF-8!")
print("3. egy sör nekem\n")
print("Have fun, KVCS\n\n")
input("Nyomj entert az indításhoz...")
f1 = open('fel.txt', encoding='UTF-8', errors='ignore')
f2 = open('meg.txt', encoding='UTF-8', errors='ignore')
f3 = open('result.txt', 'w', encoding='UTF-8', errors='ignore')
s1 = f1.read()
s2 = f2.read()
l1 = s1.split('ß')
l2 = s2.split('ß')
f1.close()
f2.close()
if len(l1) != len(l2):
    print("Elbasztad!")
    if len(l1) > len(l2):
        print("Több feladat van mint megoldás!")
        input("Nyomj entert hogy beismerd a hibádat...")
        raise SystemExit
    else:
        print("Több megoldás van mint feladat!")
        input("Nyomj entert ha leesett ezt miért hülye...")
        raise SystemExit
for i in range(len(l1)):
    f3.write(l1[i])
    f3.write(l2[i])
f3.close
print("\n\nKész!")
input("Nyomj entert ha nagyon gyorsan lefutott!")
raise SystemExit