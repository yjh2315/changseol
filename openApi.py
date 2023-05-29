import crawl
import requests
import pandas as pd


#API 설명서
#http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do

#일간 박스오피스

key = 'a92558cb64a5f10d00486d83d58dcb84'
movieNm = '명량'

url = 'http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={}&movieNm={}'.format(key,movieNm)

response = requests.get(url)
r_data =	 response.json()
fMovieList = pd.DataFrame(r_data['movieListResult']['movieList'])  

data = fMovieList[fMovieList['movieNm']==movieNm]
outCd = data.iloc[0,0]
# data.to_csv('test.csv',header=False,index =False)
# # ,encoding='cp949'

# with open('test.csv',mode = 'r') as f:
#   # ,encoding='cp949'
#   inner = f.readline()
#   in1 = inner.split(",")
#   outCd = in1[0]

url2 = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'.format(key,outCd)
response = requests.get(url2)
r_data =	 response.json()
outMovieList = pd.DataFrame(r_data['movieInfoResult'])
outMovieList_Actors = pd.DataFrame(outMovieList['movieInfo']['actors'])

# 아래 변수만큼의 배우만 정보 수집
numberOf_cmp_Actor = 7

if len(outMovieList_Actors)>numberOf_cmp_Actor:
  rep = numberOf_cmp_Actor
else:
  rep = len(outMovieList_Actors)

movieTotalPeople_Num = 0

for i in range(rep):
  url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={}&peopleNm={}&filmoNames={}'.format(key,outMovieList_Actors.iloc[i,0],movieNm)
  response = requests.get(url)
  r_data =	 response.json()
  fMovieList = pd.DataFrame(r_data['peopleListResult']['peopleList'])
  data = fMovieList[fMovieList['repRoleNm']=='배우']
  movieList = data.iloc[0,4].split("|")
  
  totalView = 0
  for i in movieList:
    try:
      print('{}:{}'.format(i,crawl.findMovieView(i)))
      totalView += crawl.findMovieView(i)
    except Exception:
      continue

# print(crawl.findMovieView('한산'))