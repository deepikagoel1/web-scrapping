from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaGyIAQGYATG4AQfIAQzYAQHoAQH4AQKIAgGoAgO4AvTIm_IFwAIB;sid=7101b3fb6caa095b7b974488df1521d2;city=-2109472;from_idr=1&;dr_ps=IDR;ilp=1;d_dcp=1'
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'lxml')
