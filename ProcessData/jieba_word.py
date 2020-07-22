import DataPreprocessing
'''
path='/root/web/Mooc_File/Subject4'
flagpath=[]
flagpath.append('/root/web/Mooc_File/Subject5/wda_mooc_18001.txt')
flagpath.append('/root/web/Mooc_File/Subject6')
flagpath.append('/root/web/Mooc_File/Subject7')
flagpath.append('/root/web/Mooc_File/Subject8')
flagpath.append('/root/web/Mooc_File/Subject9')
flagpath.append('/root/web/Mooc_File/Subject10')
flagpath.append('/root/web/Mooc_File/Subject11')
flagpath.append('/root/web/Mooc_File/Subject12')
flagpath.append('/root/web/Mooc_File/Subject13')
flagpath.append('/root/web/Mooc_File/Subject14')
timelist=[]
timelist.append('2017-09','2017-10','2017-11')
dirname=path.split('/')[-1]
DataPreprocessing.setpath(dirname)

list = ['2015-09-01','2015-10-01','2015-11-01','2015-12-01','2016-01-01','2016-02-01','2016-03-01','2016-04-01','2016-05-01','2016-06-01','2016-07-01','2016-08-01','2016-09-01','2016-10-01','2016-11-01','2016-12-01','2017-01-01','2017-02-01','2017-03-01','2017-04-01','2017-05-01','2017-06-01','2017-07-01','2017-08-01','2017-09-01']
path='C:/Users/Cathy/Desktop/通识课/18001-唐诗经典'
first_end_date =DataPreprocessing.get_course_time(path+'/moc_post_detail')
first_end_date.split('*')
start_time=first_end_date.split('*')[0]
end_time=start_time
print(start_time)
print(end_time)

'''
list = ['2017-09','2017-10','2017-11']

#path='C:/Users/Cathy/Desktop/通识课/18001-唐诗经典'
#path='C:/Users/Cathy/Desktop/通识课/20005-现代礼仪'
#path='C:/Users/Cathy/Desktop/通识课/20012'
#path='C:/Users/Cathy/Desktop/通识课/85001-急救常识'
path='C:/Users/Cathy/Desktop/通识课/153003-国际交流英语'
dirname=path.split('/')[-1]
DataPreprocessing.setpath(dirname)
'''
DataListC=[]
DataListC=DataListC=DataPreprocessing.data(path+'/wda_mooc_153003.txt',"logtime")
#print(DataListC)
DataListD=[]
DataListD=DataPreprocessing.ChangeTime1(DataListC)
print(min(DataListD))
print(max(DataListD))
'''
for i in range(0,len(list)-1):
	start_time = list[i]
	end_time = list[i+1]
	txt1 =DataPreprocessing.content_To_txt(path+'/moc_post_detail',start_time,end_time)
	DataPreprocessing.jieba_cut_word(txt1,start_time)
DataPreprocessing.write_Word_Cloud()
