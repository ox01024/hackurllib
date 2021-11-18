import hackurllib
# import requests
#
# proxy={
#     "http":"http://127.0.0.1:8080",
#     "https":"https://127.0.0.1:8080"
# }
# #
# #
# r=requests.get('https://qq.com',proxies=proxy)
# print(r.text)


if __name__ == '__main__':
    requests_Meeseg='''
POST /post HTTP/1.1
Host: httpbin.org
Content-Length: 0
accept: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Origin: http://httpbin.org
Referer: http://httpbin.org/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
    '''
    r=hackurllib.raw_requests(requests_Meeseg)
    print(r.request.method)