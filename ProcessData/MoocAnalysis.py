import DataPreprocessing
#from multiprocessing import Pool
if __name__ == '__main__':
	path='/root/web/Mooc_File/Subject1'
	dirname=path.split('/')[-1]
	DataPreprocessing.setpath(dirname)
	#爬虫
	
	DataListA=[]
	DataListA=DataPreprocessing.data(path+'/wda_mooc/wda_mooc_24001.txt',"uid")
	DataListB=[]
	DataListB=DataPreprocessing.data(path+'/wda_mooc/wda_mooc_24001.txt',"ip")
	anslist=[]
	anslist=DataPreprocessing.user_ip_dictmap(DataListA,DataListB)
	print("user-ip对应结束！")
	DataPreprocessing.ipip_net_data(anslist)
	#print("successful!")
	
	
	
	
	'''
	#anslist=['1.206.162.63','125.39.68.37','124.207.139.5','36.63.156.70']
	pool = Pool(processes=20)    # 最大进程数为40
	result= pool.apply_async(DataPreprocessing.ipip_net_data,(anslist,))
	pool.close()
	pool.join()
	if(result.successful()):
		print("successful!")
	'''
	#图表展示
	DataPreprocessing.country_province_city_districtlist('/root/web/static/'+dirname+'/ipip_net_position.txt')
	DataPreprocessing.province_city_in_indexhtml()
	#DataPreprocessing.writelist('/root/web/static/'+dirname)
	