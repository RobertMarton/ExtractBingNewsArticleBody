#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time 
import urllib.request
import urllib 
import re
import scipy.misc
import io
import socket
import chardet   #需要导入这个模块，检测编码格式
import os, random
from random import randrange

socket.setdefaulttimeout(30)
opener = urllib.request.build_opener() 
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')] 
count = 1 
print('开始下载：') 
file1 = open('abstract', 'r',encoding="utf-8")
file2 = open('article', 'r',encoding="utf-8")

abstracts = file1.readlines() 
articles = file1.readlines() 

log = open('Abstract_Head.txt','w')
aa=[] 
for abstract in abstracts: 
	# print("line:"+str(abstract))
	source=abstract.split('.')
	tmp = abstract.replace('\n'," </s> </p> </d> ")
	# print("source:"+str(source))
	res = "abstract=<d> <p> <s> "+str(tmp)#+"\t"+"article=<d> <p>"
	# print("res:"+str(res))
	log.writelines(res)
	log.writelines('\n')
log.close()


# for line3 in file3 and article in articles:
# 	# print("lin3:"+str(line3))
# 	# for article in articles:

# 	print("arti:"+str(article))
# 	res = str(line3)+str(article)
# 	print("ress:"+str(res))
# 	log2.writelines(res)
# 	log2.writelines('\n')


	# article = str(line3)+str()
	# print("line:"+str(article))
	# source=articlearticle.split('.')
	# tmp = article.replace('\n'," </s> </p> </d> ")
	# print("source:"+str(source))
	# res = "abstract=<d> <p> <s> "+str(tmp)
	# print("res:"+str(res))
	# log.writelines(res)
	# log.writelines('\n')

	# ThumbnailID = source[1]
	# print("ThumbnailID:"+str(ThumbnailID))
	# tmp = source[0].split('.')
	# print("tmp:"+str(tmp))
	# name = tmp[9]
	# print("name:"+str(name))
	# 		# 	apd = ("\t"+str(count).zfill(5)+".jpg")
	# 		# # print (apd)
	# 		# res = line.replace('\n',apd)
	# pend = name.split('.')
	# print("pend:"+str(pend))
	# try:

	# 	if int(pend[0])>=1 and int(pend[0])<=1000 and str(pend[1])=="jpg":


	# 		res = str(name)+"\t"+str(ThumbnailID)
	# 		print("abstract=<d> <p> <s>"+str(res))
	# 		log.writelines(res)
	# except Exception as e:
	# 	print('=访问页面出错') 
	# 	pass
		# log.writelines('\n')
	# print (source)
# 	if count>2: break
# 	# tempUrl = source[0]
# 	tempUrl=line
# 	# print ("tempUrl",tempUrl)
# 	try : 
# 		opener.open(tempUrl,timeout=4)
# 		urllib.request.urlopen(tempUrl,timeout=4) 
# 		try :
# 			print("count:"+str(count))
# 			urllib.request.urlretrieve(tempUrl,str(count).zfill(5)+".jpg")###use f.write(timeout) if need
# 			print(tempUrl+'=下载成功')

# 			targ0=line.split('[')
# 			targ1=line.split(']')
# 			# print("targ1[0]",targ1[0])
# 			# res = line+"test"+"\t"+(str(count).zfill(5)+".jpg")
# 			apd = ("\t"+str(count).zfill(5)+".jpg")
# 			# print (apd)
# 			res = line.replace('\n',apd)
# 			# print(res)

# 			log.writelines(res)
# 			log.writelines('\n')
# 			print("rec:"+res)
# 			count+=1
			
# 		except socket.timeout:
# 			print(tempUrl+'=访问页面超时')
# 	except Exception as e:
# 		print(tempUrl+'=访问页面出错') 
# 		pass
# #print("NOw"+a)

