
import json
from .models import Creator, Presentation

#mport presentations.settings.base

with open('data.json', 'r') as f:
    data=json.load(f)




for i in range(len(data)):
    au = Creator(name=data[i]["creator"]["name"], profileUrl=data[i]["creator"]["profileUrl"])
    au.save()

for i in range(1,len(data)+1):
    b = Creator.objects.get(id=i)
    pre = Presentation(id= data[i]['id'], title=data[i]['title'], thumbnail=data[i]['thumbnail'], author=b,createdAt=data[i]['createdAt'])
    pre.save()
