
import json
from .models import Creator, Presentation
import datetime
#mport presentations.settings.base

with open('data.json', 'r') as f:
    data=json.load(f)




for i in range(len(data)):
    au = Creator(name=data[i]["creator"]["name"], profileUrl=data[i]["creator"]["profileUrl"])
    au.save()


for i in range(len(data)):
    date_new=data[i]['createdAt']
    date_object = datetime.datetime.strptime(date_new, '%B %d, %Y').date()
    data[i]['createdAt']=date_object

for i in range(len(data)):
    b = Creator.objects.get(id=i+1)
    pre = Presentation(ident= data[i]['id'], title=data[i]['title'], thumbnail=data[i]['thumbnail'], author=b,createdAt=data[i]['createdAt'])
    pre.save()