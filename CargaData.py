import xml.etree.ElementTree as ET
import csv
import os

os.chdir("C:/Users/Taro/Documents/LEN22/LFP_PR_201602404")
os.getcwd()

f= open("Arch.data")
reader = csv.reader(f)
for row in reader:
   print (row) 
