import  requests
import  json
url='http://61.190.4.70:65410/defaultroot/public/upload/uploadify/uploader.jsp?currentModule=oa_systemmanager&dir=peopleinfo&makeYMdir=no&thumbnail=50x50_small;100x100_middle&domainId=0&portletSettingId=null'
file={
    "file":("图片.jpg",open('C:/Users/74267/Pictures/Saved Pictures/图片.jpg','rb'),'image/jpg'),
    "name":"图片.jpg"
}
cookies={
    "JSESSIONID":"475058E7AB9861B93A588FC6A01162D1",
    "ezofficePortal1722850":"3623940",
    "OASESSIONID":"475058E7AB9861B93A588FC6A01162D1",
    #"JSESSIONID":"B79B40F9A33FC32B3BE0E633E091ED16"
}
res=requests.post(url,files=file,cookies=cookies)
print(res)

