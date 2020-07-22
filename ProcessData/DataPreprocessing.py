#coding=utf-8
#data preprocessing 
import requests
import bs4
from bs4 import BeautifulSoup
import re
from collections import Counter,OrderedDict

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

import numpy as np
import time
import datetime
import json
import requests 
import collections
import random
import os
import jieba
from os import path   
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 
import codecs
import operator
from bottle import template
import webbrowser
_DEBUG=True
ANSPATH='C:/Users/Cathy/Desktop/通识课/'
def setpath(pathflag):
	global ANSPATH
	#ANSPATH='/root/web/static/'
	ANSPATH+=pathflag
	ANSPATH+='/'
	isExists=os.path.exists(ANSPATH+'Content')
	if not isExists:
		os.makedirs(ANSPATH+'Content')
#函数选择
def data(path,func):
	NameList=list()
	List=list()
	NameList=path.split('/',-1)
	len1=len(NameList)
	#for i in range(0,len1):
	#	print (NameList[i])
	#print (NameList[-2])
	#print(path)
	if (NameList[-2]=="moc_announcement"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="title"):
			List= DistillData(path,'4')
		elif(func=="content" ):
			List= DistillData(path,'5')
		elif(func=="term_id"):
			List= DistillData(path,'6')
		elif(func=="weight"):
			List= DistillData(path,'7')
		elif(func=="status"):
			List= DistillData(path,'8')
		elif(func=="send_mail"):
			List= DistillData(path,'9')
		elif(func=="publish_time"):
			List= DistillData(path,'10')
		elif(func=="type"):
			List= DistillData(path,'11')
		else :
			print ("请输入正确的关键字")
	#*************文件中是16个元素 
	elif (NameList[-2]=="moc_comment"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="commentor_id"):
			List= DistillData(path,'4')
		elif(func=="anonymous" ):
			List= DistillData(path,'5')
		elif(func=="post_id"):
			List= DistillData(path,'6')
		elif(func=="reply_id"):
			List= DistillData(path,'7')
		elif(func=="count_vote"):
			List= DistillData(path,'8')
		elif(func=="comment_time"):
			List= DistillData(path,'9')
		elif(func=="deleted"):
			List= DistillData(path,'10')
		elif(func=="tag_agree"):
			List= DistillData(path,'11')
		elif(func=="tag_top"):
			List= DistillData(path,'12')
		elif(func=="tag_top_time"):
			List= DistillData(path,'13')
		elif(func=="active_flag"):
			List= DistillData(path,'14')
		elif(func=="forum_id"):
			List= DistillData(path,'15')
		elif(func=="term_id"):
			List= DistillData(path,'16')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_course"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="name"):
			List= DistillData(path,'4')
		elif(func=="school_id" ):
			List= DistillData(path,'5')
		elif(func=="status"):
			List= DistillData(path,'6')
		elif(func=="current_term_id"):
			List= DistillData(path,'7')
		elif(func=="start_time"):
			List= DistillData(path,'8')
		elif(func=="duration"):
			List= DistillData(path,'9')
		elif(func=="end_time"):
			List= DistillData(path,'10')
		elif(func=="first_publish_time"):
			List= DistillData(path,'11')
		elif(func=="course_load"):
			List= DistillData(path,'12')
		elif(func=="big_photo"):
			List= DistillData(path,'13')
		elif(func=="short_name"):
			List= DistillData(path,'14')
		elif(func=="video_id"):
			List= DistillData(path,'15')
		elif(func=="train_id"):
			List= DistillData(path,'16')
		elif(func=="web_visible"):
			List= DistillData(path,'17')
		elif(func=="weight"):
			List= DistillData(path,'18')
		elif(func=="mode"):
			List= DistillData(path,'19')
		elif(func=="channel" ):
			List= DistillData(path,'20')
		elif(func=="from_course_id"):
			List= DistillData(path,'21')
		elif(func=="support_oj"):			
			List= DistillData(path,'22')
		elif(func=="previous_courses"):
			List= DistillData(path,'23')
		elif(func=="from_course_mode"):
			List= DistillData(path,'24')
		elif(func=="origin_copy_right_course_id"):
			List= DistillData(path,'25')
		elif(func=="apply_mooc_status"):
			List= DistillData(path,'26')
		elif(func=="current_term_chargeable"):
			List= DistillData(path,'27')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_exam"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="release_time"):
			List= DistillData(path,'4')
		elif(func=="name" ):
			List= DistillData(path,'5')
		elif(func=="description"):
			List= DistillData(path,'6')
		elif(func=="term_id"):
			List= DistillData(path,'7')
		elif(func=="deadline"):
			List= DistillData(path,'8')
		elif(func=="score_pub_status"):
			List= DistillData(path,'9')
		elif(func=="avg_score"):
			List= DistillData(path,'10')
		elif(func=="total_score"):
			List= DistillData(path,'11')
		elif(func=="score_release_time"):
			List= DistillData(path,'12')
		elif(func=="submit_count"):
			List= DistillData(path,'13')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_forum"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="name" ):
			List= DistillData(path,'4')
		elif(func=="description"):
			List= DistillData(path,'5')
		elif(func=="term_id"):
			List= DistillData(path,'6')
		elif(func=="parent_id"):
			List= DistillData(path,'7')
		elif(func=="release_time"):
			List= DistillData(path,'8')
		elif(func=="type"):
			List= DistillData(path,'9')
		elif(func=="allow_leaner_post"):
			List= DistillData(path,'10')
		elif(func=="deleted"):
			List= DistillData(path,'11')
		elif(func=="shown"):
			List= DistillData(path,'12')
		elif(func=="newest_post_id"):
			List= DistillData(path,'13')
		elif(func=="forced_closed_status"):
			List= DistillData(path,'14')
		elif(func=="forum_closed_checked"):
			List= DistillData(path,'15')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_lesson"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="name"):
			List= DistillData(path,'4')
		elif(func=="position" ):
			List= DistillData(path,'5')
		elif(func=="release_time"):
			List= DistillData(path,'6')
		elif(func=="term_id"):
			List= DistillData(path,'7')
		elif(func=="chapter_id"):
			List= DistillData(path,'8')
		elif(func=="content_type"):
			List= DistillData(path,'9')
		elif(func=="content_id"):
			List= DistillData(path,'10')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_lesson_unit"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="name"):
			List= DistillData(path,'4')
		elif(func=="position" ):
			List= DistillData(path,'5')
		elif(func=="lesson_id"):
			List= DistillData(path,'6')
		elif(func=="chapter_id"):
			List= DistillData(path,'7')
		elif(func=="term_id"):
			List= DistillData(path,'8')
		elif(func=="content_type"):
			List= DistillData(path,'9')
		elif(func=="content_id"):
			List= DistillData(path,'10')
		elif(func=="json_content"):
			List= DistillData(path,'11')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_mutual_evaluate"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="evaluator_id"):
			List= DistillData(path,'4')
		elif(func=="test_answerer_id" ):
			List= DistillData(path,'5')
		elif(func=="test_id"):
			List= DistillData(path,'6')
		elif(func=="answerform_id"):
			List= DistillData(path,'7')
		elif(func=="status"):
			List= DistillData(path,'8')
		elif(func=="orig_score"):
			List= DistillData(path,'9')
		elif(func=="evaluate_judge_type"):
			List= DistillData(path,'10')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_mutual_evaluate_detail"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="test_id"):
			List= DistillData(path,'4')
		elif(func=="evaluate" ):
			List= DistillData(path,'5')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_post"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="type"):
			List= DistillData(path,'4')
		elif(func=="lesson_unit_id" ):
			List= DistillData(path,'5')
		elif(func=="forum_id"):
			List= DistillData(path,'6')
		elif(func=="root_forum_id"):
			List= DistillData(path,'7')
		elif(func=="term_id"):
			List= DistillData(path,'8')
		elif(func=="poster_id"):
			List= DistillData(path,'9')
		elif(func=="post_time"):
			List= DistillData(path,'10')
		elif(func=="title"):
			List= DistillData(path,'11')
		elif(func=="last_replyer"):
			List= DistillData(path,'12')
		elif(func=="last_reply_time"):
			List= DistillData(path,'13')
		elif(func=="anonymous" ):
			List= DistillData(path,'14')
		elif(func=="tag_agree"):
			List= DistillData(path,'15')
		elif(func=="tag_top"):
			List= DistillData(path,'16')
		elif(func=="tag_top_time"):
			List= DistillData(path,'17')
		elif(func=="tag_solve"):
			List= DistillData(path,'18')
		elif(func=="tag_lector"):
			List= DistillData(path,'19')
		elif(func=="count_browse"):
			List= DistillData(path,'20')
		elif(func=="count_reply"):
			List= DistillData(path,'21')
		elif(func=="count_vote"):
			List= DistillData(path,'22')
		elif(func=="deleted" ):
			List= DistillData(path,'23')
		elif(func=="active_flag"):
			List= DistillData(path,'24')
		elif(func=="lock_flag"):
			List= DistillData(path,'25')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_post_detail"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="content"):
			List= DistillData(path,'4')	
		else :
			print ("请输入正确的关键字")
	#*************文件中是16个元素
	elif (NameList[-2]=="moc_reply"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="replyer_id"):
			List= DistillData(path,'4')
		elif(func=="anonymous" ):
			List= DistillData(path,'5')
		elif(func=="post_id"):
			List= DistillData(path,'6')
		elif(func=="content"):
			List= DistillData(path,'7')
		elif(func=="count_vote"):
			List= DistillData(path,'8')
		elif(func=="reply_time"):
			List= DistillData(path,'9')
		elif(func=="deleted"):
			List= DistillData(path,'10')
		elif(func=="tag_agree"):
			List= DistillData(path,'11')
		elif(func=="tag_top"):
			List= DistillData(path,'12')
		elif(func=="tag_top_time" ):
			List= DistillData(path,'13')
		elif(func=="active_flag"):
			List= DistillData(path,'14')
		elif(func=="forum_id"):
			List= DistillData(path,'15')
		elif(func=="term_id"):
			List= DistillData(path,'16')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_term"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="course_id"):
			List= DistillData(path,'4')
		elif(func=="start_time" ):
			List= DistillData(path,'5')
		elif(func=="duration"):
			List= DistillData(path,'6')
		elif(func=="end_time"):
			List= DistillData(path,'7')
		elif(func=="publish_status"):
			List= DistillData(path,'8')
		elif(func=="small_photo"):
			List= DistillData(path,'9')
		elif(func=="big_photo"):
			List= DistillData(path,'10')
		elif(func=="course_load"):
			List= DistillData(path,'11')
		elif(func=="first_publish_time"):
			List= DistillData(path,'12')
		elif(func=="close_visable_status"):
			List= DistillData(path,'13')
		elif(func=="web_visible" ):
			List= DistillData(path,'14')
		elif(func=="achievement_status"):
			List= DistillData(path,'15')
		elif(func=="term_no"):
			List= DistillData(path,'16')
		elif(func=="chargeable_cert"):
			List= DistillData(path,'17')
		elif(func=="achievement_confirmed_time"):
			List= DistillData(path,'18')
		elif(func=="time_to_freeze"):
			List= DistillData(path,'19')
		elif(func=="mode"):
			List= DistillData(path,'20')
		elif(func=="from_term_id"):
			List= DistillData(path,'21')
		elif(func=="school_id"):
			List= DistillData(path,'22')
		elif(func=="password" ):
			List= DistillData(path,'23')
		elif(func=="qualified_count"):
			List= DistillData(path,'24')
		elif(func=="excellent_count"):
			List= DistillData(path,'25')
		elif(func=="enroll_count"):
			List= DistillData(path,'26')
		elif(func=="delta_start"):
			List= DistillData(path,'27')
		elif(func=="delta_end"):
			List= DistillData(path,'28')
		elif(func=="weight_total"):
			List= DistillData(path,'29')
		elif(func=="weight_starting"):
			List= DistillData(path,'30')
		elif(func=="weight_started"):
			List= DistillData(path,'31')
		elif(func=="weight_finished" ):
			List= DistillData(path,'32')
		elif(func=="origin_copy_right_term_id"):
			List= DistillData(path,'33')
		elif(func=="apply_mooc_status"):
			List= DistillData(path,'34')
		elif(func=="from_term_mode"):
			List= DistillData(path,'35')
		elif(func=="uniform_combo_score"):
			List= DistillData(path,'36')
		elif(func=="mob_uniform_combo_score"):
			List= DistillData(path,'37')
		elif(func=="copied"):
			List= DistillData(path,'38')
		elif(func=="copy_time" ):
			List= DistillData(path,'39')
		elif(func=="price"):
			List= DistillData(path,'40')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="moc_test"):
		if(func=="id"):	
			List= DistillData(path,'1')	
		elif(func=="gmt_create"):
			List= DistillData(path,'2')
		elif(func=="gmt_modified"):
			List= DistillData(path,'3')
		elif(func=="release_time"):
			List= DistillData(path,'4')
		elif(func=="name" ):
			List= DistillData(path,'5')
		elif(func=="description"):
			List= DistillData(path,'6')
		elif(func=="test_time"):
			List= DistillData(path,'7')
		elif(func=="trytime"):
			List= DistillData(path,'8')
		elif(func=="analyse_setting"):
			List= DistillData(path,'9')
		elif(func=="test_random_setting"):
			List= DistillData(path,'10')
		elif(func=="type"):
			List= DistillData(path,'11')
		elif(func=="term_id"):
			List= DistillData(path,'12')
		elif(func=="chapter_id"):
			List= DistillData(path,'13')
		elif(func=="deadline" ):
			List= DistillData(path,'14')
		elif(func=="subjective_total_score"):
			List= DistillData(path,'15')
		elif(func=="objective_total_score"):
			List= DistillData(path,'16')
		elif(func=="submit_test_count"):
			List= DistillData(path,'17')
		elif(func=="score_pub_status"):
			List= DistillData(path,'18')
		elif(func=="avg_score"):
			List= DistillData(path,'19')
		elif(func=="exam_id"):
			List= DistillData(path,'20')
		elif(func=="position_in_exam"):
			List= DistillData(path,'21')
		elif(func=="oj_question_trytime"):
			List= DistillData(path,'22')
		elif(func=="is_random" ):
			List= DistillData(path,'23')
		else :
			print ("请输入正确的关键字")
	elif (NameList[-2]=="user_tag_value"):
		if(func=="用户id"):	
			List= DistillData(path,'1')	
		elif(func=="用户昵称"):
			List= DistillData(path,'2')
		elif(func=="生日"):
			List= DistillData(path,'3')
		elif(func=="性别"):
			List= DistillData(path,'4')
		elif(func=="地域" ):
			List= DistillData(path,'5')
		elif(func=="最后一次登陆中M时间"):
			List= DistillData(path,'6')
		elif(func=="term_id"):
			List= DistillData(path,'7')
		elif(func=="course_id"):
			List= DistillData(path,'8')
		elif(func=="选课时间"):
			List= DistillData(path,'9')
		else :
			print ("请输入正确的关键字")
	#elif (NameList[-2]=="wda_mooc"):
	else:
		if(func=="logtime"):	
			List= DistillData2(path,'1')	
		elif(func=="login_type"):
			List= DistillData2(path,'2')
		elif(func=="filter"):
			List= DistillData2(path,'3')
		elif(func=="version"):
			List= DistillData2(path,'4')
		elif(func=="session_seq" ):
			List= DistillData2(path,'5')
		elif(func=="hostname"):
			List= DistillData2(path,'6')
		elif(func=="character_set"):
			List= DistillData2(path,'7')
		elif(func=="screen_resolution"):
			List= DistillData2(path,'8')
		elif(func=="screen_color"):
			List= DistillData2(path,'9')
		elif(func=="screen_color"):
			List= DistillData2(path,'10')
		elif(func=="flash_version"):
			List= DistillData2(path,'11')
		elif(func=="refer"):
			List= DistillData2(path,'12')
		elif(func=="url"):
			List= DistillData2(path,'13')
		elif(func=="os" ):
			List= DistillData2(path,'14')
		elif(func=="browser"):
			List= DistillData2(path,'15')
		elif(func=="browser_version"):
			List= DistillData2(path,'16')
		elif(func=="uid"):
			List= DistillData2(path,'17')
		elif(func=="sid"):
			List= DistillData2(path,'18')
		elif(func=="first_session"):
			List= DistillData2(path,'19')
		elif(func=="last_session"):
			List= DistillData2(path,'20')
		elif(func=="current_session"):
			List= DistillData2(path,'21')
		elif(func=="ip"):
			List= DistillData2(path,'22')
		elif(func=="region" ):
			List= DistillData2(path,'23')
		elif(func=="event_category"):
			List= DistillData2(path,'24')
		elif(func=="event_operation"):
			List= DistillData2(path,'25')
		elif(func=="event_label"):
			List= DistillData2(path,'26')
		elif(func=="daily_newuser"):
			List= DistillData2(path,'27')
		elif(func=="hourly_newuser"):
			List= DistillData2(path,'28')
		elif(func=="search_keyword"):
			List= DistillData2(path,'29')
		elif(func=="search_engine"):
			List= DistillData2(path,'30')
		elif(func=="referral"):
			List= DistillData2(path,'31')
		elif(func=="source" ):
			List= DistillData2(path,'32')
		elif(func=="medium"):
			List= DistillData2(path,'33')
		elif(func=="utm_source"):
			List= DistillData2(path,'34')
		elif(func=="utm_medium"):
			List= DistillData2(path,'35')
		elif(func=="utm_campaign"):
			List= DistillData2(path,'36')
		elif(func=="custom_data"):
			List= DistillData2(path,'37')
		elif(func=="dt"):
			List= DistillData2(path,'38')
		elif(func=="type" ):
			List= DistillData2(path,'39')
		elif(func=="url"):
			List= DistillData2(path,'40')	
		elif(func=="refer"):
			List= DistillData2(path,'41')
		else :
			print ("请输入正确的关键字")
	

	return List
	
#数据提取1
def DistillData(path,num):	
	#print(path)
	DataList=list()
	NO_DATA = eval(num)
	#print(NO_DATA)
	with open(path,encoding='utf-8') as data:
		for line in data:
			count=0
			s = ''
			global flag
			#flag='1'
			line = line[:-1] + '\1' + line[-1:]
			for c in line:
				#print(flag)
				#if _DEBUG == True: 
				#	pdb.set_trace() 
				if (c == '\1'):
					count += 1
					continue
				if (count == NO_DATA-1):
					s += c
					
					continue
				
				if (count == NO_DATA ):
					DataList.append(s)
					break
	return DataList
	
#数据提取2 wda_mooc
def DistillData2(path,num):	
	#print (path)
	DataList=list()
	HangList=list()
	NO_DATA = eval(num)
	#print(NO_DATA)
	with open(path,'r',encoding='utf-8') as data:
		for line in data:
			if not line.strip():continue
			HangList=line.split('\t')
			#print (HangList[NO_DATA-1])
			DataList.append(HangList[NO_DATA-1])
	return DataList
		
#数据预处理时间转化	
def ChangeTime1( timelist):
	TIMELIST=[]
	for i in range(0,len(timelist)):
		TIMELIST.append(str(time.strftime("%Y-%m-%d",  (time.localtime(eval(timelist[i])//1000)))))
	return TIMELIST

'''	
#爬http://ipinfo.io，将ip转化为经纬度
#filelaglng=open('C:/Users/Cathy/Desktop/毕设/file/data/ipinfo.io经纬度.txt','w')
#fileUser_Id_Place=open('C:/Users/Cathy/Desktop/毕设/file/data/User_Id_Place.txt','w')
filelaglng=open('./Ans/ipinfoLagLng.txt','w')
fileId_Place=open('./Ans/ipinfoPlace.txt','w')
def getHTMLText(url): 
	try:
		r =requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
	
def write_data(html,num):
	try:
		tplt="{0:^20}\t{1:^10}\t{2:^10}\t{3:^10}\n"
		pos=re.findall(r'\"loc\"\: \"[\d\.]*\,[\d\.]*\"',html)
		pos1=eval(pos[0].split(':')[1])
		x=pos1.split(',')[0]
		y=pos1.split(',')[1]
		c=str(eval(x)+random.uniform(-0.005, 0.005))
		d=str(eval(y)+random.uniform(-0.005, 0.005))
		if(num==0):
			filelaglng.write("["+c+","+d+",1]]}")
		else:
			filelaglng.write("["+c+","+d+",1],")
		pos5=re.findall(r'\"ip\"\: \"[\d\.]*\"',html)
		nowip=pos5[0].split(':')[1]
		pos2=re.findall(r'\"country\"\: \"[A-Za-z]*\"',html)
		country=pos2[0].split(':')[1]
		pos3=re.findall(r'\"region\"\: \"[A-Za-z]*\"',html)
		region=pos3[0].split(':')[1]
		pos4=re.findall(r'\"city\"\: \"[A-Za-z]*\"',html)
		city=pos4[0].split(':')[1]
		
		fileId_Place.write(tplt.format(nowip,country,region,city,chr(12288)))
		
	except:
		print("")

def IpToLngLat(list):
	filelaglng.write("var data = { "+"\"data\":[")
	tplt="{0:^20}\t{1:^10}\t{2:^10}\t{3:^10}\n"
	fileId_Place.write(tplt.format("用户ip","国家","省份","市",chr(12288)))
	for i in range(0,len(list)):
		url = 'http://ipinfo.io/'
		url += list[i]
		html=getHTMLText(url)
		#print(html)
		if i==len(list)-1:
			write_data(html,0)
		else:
			write_data(html,1)
		print("已经进行到第%d个"%i)

'''
#用户-ip对应
def user_ip_dictmap(User,Ippp):
	global ANSPATH
	user_ip_data=open(ANSPATH+'user_ip_data.txt','w')
	list3=[]
	list3 = list(set(User))
	#print("结果user长度")
	#print(len(list3))
	ans=[]
	user_ip_dict={}
	user_ip_dict[User[0]]=Ippp[0]
	len1=len(User)
	for i in range (1,len1):#拼接
		if(User[i] in user_ip_dict.keys()):
			flag=user_ip_dict[User[i]]+','+Ippp[i]
			user_ip_dict[User[i]]=flag
			continue
		user_ip_dict[User[i]]=Ippp[i]
	for j in range(0,len(list3)):#截取
		pos1=user_ip_dict[list3[j]]
		x=pos1.split(',')
		d = collections.Counter(x).most_common(1)
		ans.append(d[0][0])#选择数量最多的ip作为用户ip
	for t in range(0,len(ans)):
		user_ip_data.write(ans[t]+'\n')
	#print("结果ip长度：")
	#print(len(ans))
	
	return ans
#爬取ipip.net
def getHTMLText2(url,ip): 
	try:
		
		header = {'Referer':'http://www.ipip.net/ip.html','Host':'www.ipip.net','User-Agent':'Mozilla/5.0'} 
		payload = {'ip':ip}
		r = requests.post(url,headers=header, data=payload)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def write_data2(html,num):
	FLAG_ERROR=1
	global ANSPATH
	ipip_net_lnglat=open(ANSPATH+'ipip_net_latlong.txt','a+')
	ipip_net_Place=open(ANSPATH+'ipip_net_position.txt','a+')
	try:
		tplt="{0:^40}\t{1:^10}\t{2:^10}\t{3:^10}\n"
		soup =BeautifulSoup(html,"html.parser")
		position=soup.find(style='text-align: center;color:red;font-size: 20px;font-weight: 600;')
		if position is None:
			flag1=soup.find_all( class_='table table-striped table-bordered')
			pos2=flag1[1]
			flag2=soup.find_all('td',pos2)
			flag3=flag2[-4]
			pos3=flag3.text
			pos3.split()
			str1=["*","*","*","*"]
			for q in range(0,len(pos3.split())):
				str1[q]=pos3.split()[q]
			ipip_net_Place.write(tplt.format(str1[0],str1[1],str1[2],str1[3],chr(12288)))
		else:
			pos=position.text
			#print("pos"+pos)
			country=pos.split()[0]
			province=pos.split()[1]
			city=pos.split()[2]
			district=pos.split()[3]
			if city=="杭州":
				FLAG_ERROR=0
			else :
				ipip_net_Place.write(tplt.format(country,province,city,district,chr(12288)))
			
		res = (soup.find_all('script'))[5].text
		lat=re.search(r'\"latitude\"\:\"-?[\d\.]*\"',res)
		x=lat.group(0).split(':')[1].split('"')[1]
		c=str(eval(x)+random.uniform(-0.15, 0.15))#latitude
		long=re.search(r'\"longitude\"\:\"-?[\d\.]*\"',res)
		y=long.group(0).split(':')[1].split('"')[1]
		d=str(eval(y)+random.uniform(-0.15, 0.15))#longitude
		if(num==0):
			ipip_net_lnglat.write("["+c+","+d+",1]]}")
			ipip_net_lnglat.close()
			ipip_net_Place.close()
			
		else:
			ipip_net_lnglat.write("["+c+","+d+",1],")
		return FLAG_ERROR
	except:
		print("failure！！！")
		return FLAG_ERROR
		
		#time.sleep(5)
def ipip_net_data(list):
	global ANSPATH
	ipip_net_lnglat=open(ANSPATH+'ipip_net_latlong.txt','w+')
	ipip_net_Place=open(ANSPATH+'ipip_net_position.txt','w+')
	ipip_net_lnglat.write("var data = { "+"\"data\":[")
	tplt="{0:^40}\t{1:^10}\t{2:^10}\t{3:^10}\n"
	ipip_net_Place.write(tplt.format("国家","省份","市","区/县",chr(12288)))
	ipip_net_lnglat.close()
	ipip_net_Place.close()
	Delete_Duplicate(list)
def Delete_Duplicate(list):
	if len(list)==0:
		return 0
	List_Flag=[]
	for i in range(0,len(list)):
		url = 'http://www.ipip.net/ip.html'
		html=getHTMLText2(url,list[i])
		if(html==""):
			List_Flag.append(list[i])
			continue
		else:
			if i==len(list)-1:
				Delete_Duplicate(List_Flag)
				url = 'http://www.ipip.net/ip.html'
				html=getHTMLText2(url,list[i])
				FailFlag=write_data2(html,0)
			else:
				FailFlag=write_data2(html,1)
				if FailFlag==0 or FailFlag=='0':
					print("0000000000000000\n")
					List_Flag.append(list[i])
		#print("已经进行到第%d个"%i)
'''
		
#数据利用百度地图ip转化为经纬度
def IpChangeLngLat (list1,start ,end):
	file=open('C:/Users/Cathy/Desktop/毕设/file/data/Ip_LngLat_data.txt','w')
	for i in range(0,len(list1)):
		
		if i%100==0:
			time.sleep(10)
		
		url = 'http://api.map.baidu.com/location/ip?ip='
		url +=list1[i]
		url +='&ak=02MgQiAUQkSnfEFb14V1Zt7a3BMH8py3&coor=bd09ll'
		header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Sougou/6.0.5.18249'}  
		r = requests.get(url, headers = header,timeout = 300)
		js = json.loads(r.text)
		if js['status']!=0:
			num+=1
			continue
		#print(js)
		file.write((str(js['content']['point']['x']))+'\n')
		file.write((str(js['content']['point']['y']))+'\n')
		#print (i)
	print("跳过的次数为:")
	print(num)
'''
'''
	print(len(list1))
	LngLat=[]
	url = 'http://api.map.baidu.com/location/ip?ip='
	url +=list1[0]
	url +='&ak=ZQWG0l95n518LhAeHROA1wplIdlAZQcf&coor=bd09ll'
	header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Sougou/6.0.5.18249'}  
	r = requests.get(url, headers = header, timeout = 30)
	#print(r.headers)
	js = json.loads(r.text)
	#print(js)
	LngLat.append(str(js['content']['point']['x']))
	for i in range (1,len(list1)):
		#s = requests.session()  
		if(list1[i]==list1[i-1]):
			continue
		url = 'http://api.map.baidu.com/location/ip?ip='
		url +=list1[i]
		url +='&ak=ZQWG0l95n518LhAeHROA1wplIdlAZQcf&coor=bd09ll'
		header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Sougou/6.0.5.18249'}  
		r = requests.get(url, headers = header, timeout = 30)
		js = json.loads(r.text)
		#print(js)
		LngLat.append(str(js['content']['point']['x']))
		LngLat.append(str(js['content']['point']['y']))
		print(i)
	print("ip转化中心点经纬度完成"+'\n')
	return LngLat
'''
word_time = []
#列表转化为字典统计元素个数对应
def list_To_dir(list,start_time):
	#print(list)
	delete_word=['也','有','是','了',')','（','）','(','；','：',' ','?',',',':',';','.','，','。','？','“','"','/','、','”','&','*','%','? ',', ', ': ', '; ', '. ', '，', '。 ','？ ','“ ','" ','/ ','、 ','” ','& ','* ','% ','.:','=:','[',']','quot','_','self','的','gt','/','-','1','line']
	count = {}
	for item in list:
		if item in delete_word or len(item)==1:
			list.remove(item)
		else:
			count[item] = count.get(item, 0) + 1
	sorted_x = sorted(count.items(), key=lambda count : count[1], reverse=True)
	'''
	for item in sorted_x:
		flag = item[0]
		if flag in delete_word or len(flag)==1:
			sorted_x.remove(item)
	'''			
	flagdir={}
	flagdir['time'] = start_time[0:-3]
	flagdir['words'] = sorted_x
	word_time.append(flagdir)
	

def write_Word_Cloud():
	word_timedir=open(ANSPATH+'Content/'+'word_time1.txt', 'w+')
	word_timedir.write(str(word_time))
#词云模块
def content_To_txt(path,startime,endtime):
	global ANSPATH
	exclude=["老师","谢谢","请问"]
	content_file=open(ANSPATH+'Content/'+startime+'-'+endtime+'.txt','w')
	FileList=os.listdir(path)
	AnsTimeList=[]
	AnsContentList=[]
	Content_Time=[]
	Content_detail=[]
	for i in range(0,len(FileList)):
		Content_Time1=ChangeTime1(data(path+'/'+FileList[i],"gmt_create"))
		Content_detail=data(path+'/'+FileList[i],"content")
		#print(len(Content_detail))
		AnsTimeList+=Content_Time1
		AnsContentList+=Content_detail
	#print(len(AnsTimeList))
	for j in range(0,len(AnsTimeList)):
		if AnsTimeList[j]>=startime and AnsTimeList[j]<=endtime:
			sum=re.sub(r'<([^>]*)>', '', AnsContentList[j])#将评论中的<……></……>替换为空
			sum=re.sub(r'老师', '', sum)
			sum=re.sub(r'谢谢', '', sum)
			sum=re.sub(r'请问', '', sum)
			sum=re.sub(r'没有', '', sum)
			sum=re.sub(r'可以', '', sum)
			sum=re.sub(r'您', '', sum)
			sum=re.sub(r'你', '', sum)
			sum=re.sub(r'我', '', sum)
			sum=re.sub(r'他', '', sum)
			sum=re.sub(r'它', '', sum)
			sum=re.sub(r'&nbsp', '', sum)
			sum=re.sub(r'什么', '', sum)
			sum=re.sub(r'为什么', '', sum)
			sum=re.sub(r'怎么', '', sum)
			sum=re.sub(r'但是', '', sum)
			sum=re.sub(r'还是', '', sum)
			sum=re.sub(r'虽然', '', sum)
			sum=re.sub(r'所以', '', sum)
			sum=re.sub(r'因为', '', sum)
			#data[sum] = data[sum].decode('latin-1')
			content_file.write(sum)
	return ANSPATH+'Content/'+startime+'-'+endtime+'.txt'
	
def jieba_cut_word (txt1,start_time):
	text = open(txt1,'r').read()  #,encoding = 'utf-8'
	list_To_dir(jieba.lcut(text),start_time)
def Word_Cloud(txt1):
	global ANSPATH
	isExists=os.path.exists(ANSPATH+'PIC')
	if not isExists:
		os.makedirs(ANSPATH+'PIC')
	sstr=ANSPATH+'PIC/'
	matplotlib.rcParams['font.family']='SimHei'
	matplotlib.rcParams['font.sans-serif']=['SimHei']
	matplotlib.rcParams['font.size'] = 20
	text = open(txt1,'r').read()  #,encoding = 'utf-8'
	word_jieba = jieba.cut(text,cut_all=True)  #利用jieba分割中文文本
	word_split = " ".join(word_jieba)  
	my_wordclud = WordCloud(font_path='/root/web/msyh.ttc',max_words=100,width = 1600,height=800)
	my_wordclud=my_wordclud.generate(word_split)#用wordcloud形成词云
	word_split.split()
	flag1=txt1.split('/')
	flag2=flag1[-1]
	plt.figure(figsize=(18, 10)) 
	plt.title(flag2.split('.')[0]+"评论区词云") 
	plt.imshow(my_wordclud)  
	plt.axis("off")  
	#plt.show() 
	#d = path.dirname(__file__)	
	str=sstr+flag2.split('.')[0]+'.png'
	my_wordclud.to_file(str) 
	
	
#图形显示模块	
	
#处理国省市区+计数
country_list=[]
province_list=[]
city_list=[]
district_list=[]
#数据预处理时间转化 年-月
def ChangeTime2(timelist):
	TIMELIST=[]
	for i in range(0,len(timelist)):
		TIMELIST.append(str(time.strftime("%Y-%m",  (time.localtime(eval(timelist[i])//1000)))))
	return TIMELIST
#日期和用户数量对应
def date_usernum(time_list,uid_list):
	day_user_count=[]
	date_count_dirt={}
	num_list=[]
	TIME_LIST2=list(set(time_list))
	for i in range(0,len(TIME_LIST2)):
		for j in range(0,(len(time_list))):
			if time_list[j]==TIME_LIST2[i]:
				day_user_count.append(uid_list[j])
		num_list=list(set(day_user_count))
		#print(len(num_list))
		date_count_dirt[TIME_LIST2[i]]=len(num_list)
		day_user_count=[]
		num_list=[]			
	new_list=sorted(date_count_dirt.keys() )
	new_dirt={}
	#按照时间将字典排序
	for m in range(0,len(date_count_dirt)):
		new_dirt[new_list[m]]=date_count_dirt[new_list[m]]
	return new_dirt
def country_province_city_districtlist(path):
	with open(path) as data2:#,encoding='utf-8'
		data2.readline()
		flag=0
		for line in data2:
			if(line=='\n'):
				continue
			a=line.split('\t')[0].strip()
			if a=='*':
				continue
			b=line.split('\t')[1].strip()
			c=line.split('\t')[2].strip()
			d=line.split('\t')[3].strip()
			if a[-1]=='省' or a[-1]=='市' :
				a=a[0:-1]
			if b[-1]=='省' or b[-1]=='市' :
				b=b[0:-1]
			if c[-1]=='省' or c[-1]=='市' :
				c=c[0:-1]
			if d[-1]=='省' or d[-1]=='市' :
				d=d[0:-1]
			if(a=="香港" or a=="澳门"or a=="台湾"):
				flag+=1
				d=c
				c=b
				b=a
				a='中国'
			if b=='闽':
				b='福建'
			if b=='内蒙古自治区':
				b='内蒙古'
			if b=='广西壮族自治区':
				b='广西'
			if b=='西藏自治区':
				b='西藏'
			if b=='宁夏回族自治区':
				b='宁夏'
			if b=='新疆维吾尔自治区':
				b='新疆'
			country_list.append(a)
			province_list.append(b)
			city_list.append(c)
			district_list.append(d)
	'''
	print("country")
	print(country_list)
	print(province_list)
	print(city_list)
	print(district_list)
	'''

#统计不同国家用户数，返回字典
def country_num():
	list=country_list[:]
	count = Counter(list)
	#print(count)
	#print(type(count))
	#print(len(count))
	#print(len(country_list))
	#print(count["中国"])
	
	return count
#查询特定国家的用户在该国家内的分布，返回字典
def country_province(country):
	FLAG=0
	country_povince_dict={}#国家和省的对应字典
	len1=len(country_list)
	for i in range (1,len1):
		if country==country_list[i]:
			if(country!='中国'):
				if province_list[i]=='*':
					province_list[i]=='其他'
					if('其他' in country_povince_dict.keys()):
						country_povince_dict['其他']+=1
					else:
						country_povince_dict['其他']=1
				else:
					if(province_list[i] in country_povince_dict.keys()):
						country_povince_dict[province_list[i]]+=1
					else:
						country_povince_dict[province_list[i]]=1
			else:
				if province_list[i]=='*':
					continue
				else:
					if(province_list[i] in country_povince_dict.keys()):
						country_povince_dict[province_list[i]]+=1
					else:
						country_povince_dict[province_list[i]]=1
		else:
			continue
	#print(country_povince_dict)
	return country_povince_dict

#查询特定省份的用户在该省份内的分布，返回字典(不包括4个直辖市)
def province_city(province):
	province_city_dict={}#省和市的对应字典
	len1=len(province_list)
	for i in range (1,len1):
		if province==province_list[i]:
			if province=='吉林':
				if city_list[i]=='Guangdong'or city_list[i]=='Yushu'or city_list[i]=='Chaoyang'or city_list[i]=='*':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				else:
					if(city_list[i] in province_city_dict.keys()):
						province_city_dict[city_list[i]]+=1
					else:
						province_city_dict[city_list[i]]=1
				continue
			elif province=='安徽':
				if city_list[i]=='Xuanzhou':
					city_list[i]='安徽'
					if('宣州' in province_city_dict.keys()):
						province_city_dict['宣州']+=1
					else:
						province_city_dict['宣州']=1
				elif city_list[i]=='Huainan':
					city_list[i]='淮南'
					if('淮南' in province_city_dict.keys()):
						province_city_dict['淮南']+=1
					else:
						province_city_dict['淮南']=1
			elif province=='福建':
				if city_list[i]=='Putian':
					city_list[i]='莆田'
					if('莆田' in province_city_dict.keys()):
						province_city_dict['莆田']+=1
					else:
						province_city_dict['莆田']=1
			elif province=='辽宁':
				if city_list[i]=='Panjin':
					city_list[i]='盘锦'
					if('盘锦' in province_city_dict.keys()):
						province_city_dict['盘锦']+=1
					else:
						province_city_dict['盘锦']=1
				elif city_list[i]=='Chaoyang':
					city_list[i]='朝阳'
					if('朝阳' in province_city_dict.keys()):
						province_city_dict['朝阳']+=1
					else:
						province_city_dict['朝阳']=1
				elif city_list[i]=='Beipiao':
					city_list[i]='北票'
					if('北票' in province_city_dict.keys()):
						province_city_dict['北票']+=1
					else:
						province_city_dict['北票']=1
				elif city_list[i]=='Daqing':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
			elif province=='河北':
				if city_list[i]=='Shijiazhuang':
					city_list[i]='石家庄'
					if('石家庄' in province_city_dict.keys()):
						province_city_dict['石家庄']+=1
					else:
						province_city_dict['石家庄']=1
				elif city_list[i]=='Shenzhou':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
			elif province=='湖北':
				if city_list[i]=='Xiantao':
					city_list[i]='仙桃'
					if('仙桃' in province_city_dict.keys()):
						province_city_dict['仙桃']+=1
					else:
						province_city_dict['仙桃']=1
			elif province=='山西':
				if city_list[i]=='Changzhi':
					city_list[i]='长治'
					if('长治' in province_city_dict.keys()):
						province_city_dict['长治']+=1
					else:
						province_city_dict['长治']=1
			elif province=='台湾':
				if city_list[i]=='Taoyuan':
					city_list[i]='桃园'
					if('桃园' in province_city_dict.keys()):
						province_city_dict['桃园']+=1
					else:
						province_city_dict['桃园']=1
			elif province=='江苏':
				if city_list[i]=="Huai'an":
					city_list[i]='淮安'
					if('淮安' in province_city_dict.keys()):
						province_city_dict['淮安']+=1
					else:
						province_city_dict['淮安']=1
				elif city_list[i]=='Chengxiang':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				elif city_list[i]=='Dongtai':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				elif city_list[i]=='Changshu':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				elif city_list[i]=='Chengjiang':
					city_list[i]='澄江'
					if('澄江' in province_city_dict.keys()):
						province_city_dict['澄江']+=1
					else:
						province_city_dict['澄江']=1
			elif province=='浙江':
				if city_list[i]=='Huzhou':
					city_list[i]='湖州'
					if('湖州' in province_city_dict.keys()):
						province_city_dict['湖州']+=1
					else:
						province_city_dict['湖州']=1
				elif city_list[i]=='Kunyang':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				elif city_list[i]=='Deqing':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				elif city_list[i]=='Weitang':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
			elif province=='江西':
				if city_list[i]=='Yichun':
					city_list[i]='宜春'
					if('宜春' in province_city_dict.keys()):
						province_city_dict['宜春']+=1
					else:
						province_city_dict['宜春']=1
				elif city_list[i]=='Guixi':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
			elif province=='广西':
				if city_list[i]=='Yichun':
					city_list[i]='福建'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
				elif city_list[i]=='Hechi':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
			elif province=='山东':
				if city_list[i]=="Tai'an":
					city_list[i]='泰安'
					if('泰安' in province_city_dict.keys()):
						province_city_dict['泰安']+=1
					else:
						province_city_dict['泰安']=1
			elif province=='广东':
				if city_list[i]=='Shantou':
					city_list[i]='汕头'
					if('汕头' in province_city_dict.keys()):
						province_city_dict['汕头']+=1
					else:
						province_city_dict['汕头']=1
			elif province=='贵州':
				if city_list[i]=='Qinghai':
					city_list[i]='其他'
					if('其他' in province_city_dict.keys()):
						province_city_dict['其他']+=1
					else:
						province_city_dict['其他']=1
			elif province=='海南':
				if city_list[i]=='Sanya':
					city_list[i]='三亚'
					if('三亚' in province_city_dict.keys()):
						province_city_dict['三亚']+=1
					else:
						province_city_dict['三亚']=1
			if city_list[i]=='*'or city_list[i]==province_list[i]:
				if('其他' in province_city_dict.keys()):
					province_city_dict['其他']+=1
				else:
					province_city_dict['其他']=1
			else:
				if(city_list[i] in province_city_dict.keys()):
					province_city_dict[city_list[i]]+=1
				else:
					province_city_dict[city_list[i]]=1
		else:
			continue
	#print(province_city_dict)
	return province_city_dict

#查询国家和市的对应
def country_city(country):	
	country_city_dict={}#国家和市的对应字典
	len1=len(country_list)
	print(len1)
	for i in range (1,len1):
		if country==country_list[i]:
			if city_list[i]=='*':
				continue
			else:
				if(city_list[i] in country_city_dict.keys()):
					country_city_dict[city_list[i]]+=1
				else:
					country_city_dict[city_list[i]]=1
		else:
			continue
	print(len(country_city_dict))
	return country_city_dict

#查询特定市的用户在该市内的分布，返回字典(包括4个直辖市)
def city_district(city):
	city_district_dict={}#省和市的对应字典
	len1=len(city_list)
	for i in range (1,len1):
		if city==city_list[i]:
			if district_list[i]=='*'or district_list[i]==city_list[i]:
				if '其他'in city_district_dict.keys():
					city_district_dict['其他']+=1
				else:
					city_district_dict['其他']=1
			else:
				if(district_list[i] in city_district_dict.keys()):
					city_district_dict[district_list[i]]+=1
				else:
					city_district_dict[district_list[i]]=1
		else:
			continue
	#print(city_district_dict)
	return city_district_dict	

	
def province_city_in_indexhtml():
	global ANSPATH
	pro_city_index=open(ANSPATH+'pro_city_list.txt','w')
	pro_list=["河北","山西","辽宁","吉林","黑龙江","江苏","浙江","安徽","福建","江西","山东","河南","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","台湾","内蒙古","广西","西藏","宁夏","新疆","香港","澳门"]
	pro_city_index.write("var city_name=[")
	for i in range(0,(len(pro_list)-1)):
		flag_dirt=province_city(pro_list[i])
		flag_list=list(flag_dirt.keys())
		if '其他' in flag_list:
			flag_list.remove('其他')
		if (len(flag_list)!=0):
			pro_city_index.write("[")
			for j in range(0,(len(flag_list)-1)):
				pro_city_index.write("\""+flag_list[j]+'\",')
			pro_city_index.write("\""+flag_list[len(flag_list)-1]+'\"],')
		else:
			continue
	flag_dirt=province_city(pro_list[len(pro_list)-1])
	flag_list=list(flag_dirt.keys())
	if '其他' in flag_list:
		flag_list.remove('其他')
	if len(flag_list)!=0:
		pro_city_index.write("[")
		for j in range(0,(len(flag_list)-1)):
			pro_city_index.write("\""+flag_list[j]+'\",')
		pro_city_index.write("\""+flag_list[len(flag_list)-1]+'\"]')
		
	pro_city_index.write("]")
#可视化柱状图
def bar_chart(flag_dirt,num,str):
	#print(type(flag_dirt))
	#print(len(flag_dirt))
	#print(flag_dirt["中国"])
	global ANSPATH
	if not flag_dirt:
		return 0
	if str=='*':
		return 0
	labeln=[]
	data=[]
	i=0
	for key in flag_dirt.keys():
		labeln.append(key)
		data.append(flag_dirt[key])
		i+=1
		
	matplotlib.rcParams['font.family']='SimHei'
	matplotlib.rcParams['font.sans-serif']=['SimHei']
	matplotlib.rcParams['font.size'] = 15
	plt.figure(figsize=(18, 10))
	ax=plt.subplot(111)
	plt.subplots_adjust(0.1, 0.2, 0.95, 0.95)
	n_groups = i 
	bar_width = 0.9
	index = np.arange(n_groups) 
	ticks = ax.set_xticks(index)
	labels = ax.set_xticklabels(labeln, rotation=90, fontsize='small')
	plt.bar(index,data,bar_width,color='b')#,label=labels
	isExists=os.path.exists(ANSPATH+'PIC')
	if not isExists:
		os.makedirs(ANSPATH+'PIC')
	sstr=ANSPATH+'PIC/'
	if num==0:	
		plt.xlabel('国家')  
		plt.title('用户在'+str+'各国的分布')
	elif num==1:
		plt.xlabel('省份')  
		plt.title('用户在'+str+'各省的分布')
	elif num==2:
		plt.xlabel('市')  
		plt.title('用户在'+str+'各市的分布')
	elif num==3:
		plt.xlabel('区、县')  
		plt.title('用户在'+str+'各区、县的分布')
	plt.ylabel('个数/人')  
	 
	x1=np.arange(i)
	y1=np.array(data)
	for a,b in zip(x1,y1):
		plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=7)
	plt.ylim(0,(max(data)+200)) 
	plt.savefig(sstr+str+'.png')
	#plt.show()  
#可视化饼图 前num名的比例
def pie_chart(dirt1,num):
	global ANSPATH
	isExists=os.path.exists(ANSPATH+'PIC')
	if not isExists:
		os.makedirs(ANSPATH+'PIC')
	#value_list=sorted(dirt1.iteritems(), key=lambda d:d[1], reverse = False )
	#value_list=sorted(dirt1.keys())
	labels=[]
	values=[]
	if num>len(dirt1):
		num=len(dirt1)
	for i in range(0,num):
		labels.append(max(dirt1.items(), key=lambda x: x[1]))
		values.append(max(dirt1.items(), key=lambda x: x[1])[1])
		dirt1.pop(max(dirt1.items(), key=lambda x: x[1])[0])
	matplotlib.rcParams['font.family']='SimHei'
	matplotlib.rcParams['font.sans-serif']=['SimHei']
	#调节图形大小，宽，高
	#labels=values
	plt.figure(figsize=(15,12))
	plt.pie(values,explode=None,labels=labels,autopct='%1.2f%%')
	plt.title('前'+str(num)+'名的用户分布') 
	# 设置x，y轴刻度一致，这样饼图才能是圆的
	plt.axis('equal')    
	plt.savefig(ANSPATH+'PIC/first'+str(num)+'.png') 
	#plt.show()
#可视化折线图
def plot_chart(dirt2):
	global ANSPATH
	isExists=os.path.exists(ANSPATH+'PIC')
	if not isExists:
		os.makedirs(ANSPATH+'PIC')
	new_list=sorted(dirt2.keys() )
	print(new_list)
	new_dirt={}
	i=0
	labeln=[]
	data=[]
	#按照时间将字典排序
	for m in range(0,len(dirt2)):
		labeln.append(new_list[m])
		data.append(dirt2[new_list[m]])
		i+=1
	matplotlib.rcParams['font.family']='SimHei'
	matplotlib.rcParams['font.sans-serif']=['SimHei']
	matplotlib.rcParams['font.size'] = 15
	plt.figure(figsize=(18, 10))
	ax=plt.subplot(111)
	index = np.arange(i)  
	ticks = ax.set_xticks(index)
	labels = ax.set_xticklabels(labeln, rotation=30, fontsize='small')
	plt.plot(index,data,linewidth=3,label='用户数量',color='r',marker='o', markerfacecolor='blue',markersize=10)
	plt.xlabel('时间') 
	plt.ylabel('用户量/人') 
	plt.title('用户量随时间的变化') 
	x1=np.arange(i)
	y1=np.array(data)
	for a,b in zip(x1,y1):
		plt.text(a+0.4, b+1, '%.0f' % b, ha='center', va= 'bottom',fontsize=15)
	plt.legend() 
	#plt.show() document.getElementById("start_time").value
	plt.savefig(ANSPATH+'PIC/User_Time.png') 

	
#将列表写入文件
def writelist(path):
	country=open(path+'/country.txt','w')
	province=open(path+'/province.txt','w')
	city=open(path+'/city.txt','w')
	district=open(path+'/district.txt','w')
	for i in range (0,len(country_list)):
		country.write(country_list[i]+'\n')
	for i in range (0,len(province_list)):
		province.write(province_list[i]+'\n')
	for i in range (0,len(city_list)):
		city.write(city_list[i]+'\n')
	for i in range (0,len(district_list)):
		district.write(district_list[i]+'\n')
	if(len(country_list)==len(province_list)):
		if(len(country_list)==len(city_list)):
			if(len(country_list)==len(district_list)):
				print(len(district_list))
				print("All Lists have same length!!!!!!!")
country_list2=[]
province_list2=[]
city_list2=[]
district_list2=[]
#从文件读入列表
def readlist(path):
	with open(path+'/country.txt','r') as data1:
		for line1 in data1:
			country_list.append(line1.strip('\n'))
	with open(path+'/province.txt','r') as data2:
		for line2 in data2:
			province_list.append(line2.strip('\n'))
	with open(path+'/city.txt','r') as data3:
		for line3 in data3:
			city_list.append(line3.strip('\n'))
	with open(path+'/district.txt','r') as data4:
		for line4 in data4:
			district_list.append(line4.strip('\n'))
	#print(len(country_list))
	#print(len(province_list))
	#print(city_list)
	#print(district_list)
	
#在浏览器上展示	
def ShowHtml(flaglist):
	articles=flaglist
	#定义想要生成的Html的基本格式
	#使用%来插入python代码
	template_demo="""
	<html>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>MOOC数据分析</title>
	<style type = “text/css”>
	a {font-size:16px}
	a:link {color: blue; text-decoration:none;} 
	a:active:{color: red; } 
	a:visited {color:purple;text-decoration:none;} 
	a:hover {color: red; text-decoration:underline;} 
	</style>
	<body>
	<div style="background:'green';color:'black'">
	<a href="http://www.icourse163.org/" style="color:blue;">中国大学Mooc</a>
	<br/>
	<br/>
	<br/>
	<a href="http://123.57.35.110:8080/static/Masspoint.html" align="center" style="color:blue;">用户归属地地图显示--请点击</a>
	<br/>
	<br/>
	<br/>
	<h2 align="center" style="color:red;">您可以参考以下两幅图，对您感兴趣的进行再次查询</h2>
	% for title,detail in items:
	<div align="center">
	<h2>{{title.strip()}}</h2>
	<img src={{detail}} width="90%" height="90%" " />
	</div>
	%end


	</body>
	</html>
	"""

	html = template(template_demo,items=articles)
	with open("/root/web/templates/test.html",'wb') as f:
		f.write(html.encode('utf-8'))
	#使用浏览器打开html
	return "/root/web/templates/test.html"
