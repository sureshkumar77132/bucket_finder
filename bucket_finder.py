import pandas 
import requests as r
list=[]
data=pandas.read_csv('b.csv', usecols=['content'])
df=data['content'].values.tolist()
mylist=list(dict.fromkeys(df))
for i in mylist:

  url="http://"+i+".s3.amazonaws.com"
  response=r.get(url)
  status=response.status_code
  if(status==200):
    list.append(i)

for j in list:

    print("The opened buckets are:")
	print(j)
