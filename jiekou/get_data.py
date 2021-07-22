from mitmproxy import  http
from Unit.handle_json import get_value
import json
class GetData:
    def request(self,flow):
        request_data = flow.request
        self.request_url = request_data.url
        request_pr = request_data.query
        request_form = request_data.urlencoded_form
        # print("url:------->",self.request_url)
        # print("pr:------->", request_pr)
        # print("form:------->", request_form)

    def response(self,flow):
        if '192.168.0.77' in self.request_url or '192.168.0.161' in self.request_url:
            response_data = flow.response
            host = self.request_url.split(".com")
            base_url = host[0]
            url = host[1]
            if "?" in host[1]:
                url = url.split("?")[0]
            print("====>", url)
            data = json.dumps(get_value(url))
            print("----->data:", data)
            response_data.set_text(data)
            # response_header = response_data.headers
            # content_type = response_header['content-type']
            # print("类型-------》",content_type)
            # if 'json' in content_type :
            #     print("code--------->", response_data.status_code)
            #     print("text--------->", response_data.text)
            # else:
            #     pass

addons = [
    GetData()
]