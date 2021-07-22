import requests
import json
from Unit.handle_ini import hanle_ini
from Unit.handle_json import get_value
from Unit.handle_cookie import get_cookie_value,write_cookie
class BaseRequest(object):
    def send_post(self,url,data,cookie=None,get_cookie=None,header=None):
        response = requests.post(url=url,data=data,cookies=cookie,headers=header)
        if get_cookie != None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(get_cookie['is_cookie'], cookie_value)
        res = response.text
        return res
    def send_get(self,url,data,cookie=None,get_cookie=None,header=None):
        response = requests.get(url=url,params=data,cookies=cookie,headers=header)
        if get_cookie != None:
            '''
            {"is_cookie":"app"}
            '''
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(get_cookie['is_cookie'], cookie_value)
        res = response.text
        return res
    def run_main(self,method,url,data,cookie=None,get_cookie=None,header=None):
        # return get_value(url)
        base_url = hanle_ini.get_value('host')
        if 'http' not in url:
            url = str(base_url) + url
        if method=='post':
            res=self.send_post(url,data,cookie,get_cookie,header)
        else:
            res=self.send_get(url,data,cookie,get_cookie,header)
        try:
            res=json.loads(res)
        except:
            print('这是txt')
        return res
if __name__ == '__main__':
    base=BaseRequest()
    data = {'username': 'yangbo','password': '123qwe!'}
    base.run_main("post","http://192.168.0.53:8001/flexbase/api/w/logon/login",
                  {"username": "yangbo","password": "123qwe!"})
