import hackurllib

# proxy={
#     "http://":"127.0.0.1:8080)",
#     "https://":"127.0.0.1:8080"
# }
#
#
# r=hackurllib.get('https://qq.com')
# print(r.text)

if __name__ == '__main__':
    requests_Meeseg='''
    
    
    
GET / HTTP/1.1
Host: www.baidu.com
Cookie: uc_login_unique=93747f5be3f986cd3bd5b33d0da7be0b; uc_recom_mark=cmVjb21tYXJrXzM2MTc1MDky; __yjs_duid=1_47ffbeaa0c8c53bf5f8aedc47f97901a1635656056359; jsdk-uuid=628935b3-0048-4149-9c62-9150b68d7141; BAIDUID=E083A89D50F9039D2C76C06A694219DF:FG=1; BAIDUID_BFESS=E083A89D50F9039D2C76C06A694219DF:FG=1; BIDUPSID=E083A89D50F9039D2C76C06A694219DF; PSTM=1636771036; BD_UPN=123253; BA_HECTOR=0c2100a10l2120a1tc1gp6n930q
Sec-Ch-Ua: "Chromium";v="95", ";Not A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close'''
    r=hackurllib.raw_requests(requests_Meeseg)
    print(r)