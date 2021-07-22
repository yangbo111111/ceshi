import  requests
url='http://file.mukewang.com/apk/app/119/1592880622/imooc7.3.810102001android.apk?version=1592880624'
res=requests.get(url)
with open('C:/Users/74267/Downloads/1.apk',"wb") as f:
    f.write(res.content)
