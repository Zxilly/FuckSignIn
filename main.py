# Fuck Sign in
import json
from urllib.parse import quote

import requests
import urllib3

from pri import *

proxies = {
    "http": None,
}

cookie = {'loginName': loginname, 'yzxx': yzxx}
http = urllib3.PoolManager()
data_get = requests.get('http://yqjk.jgsu.edu.cn:8090/parameter/xxmc', proxies=proxies)
data_get_cookie = json.loads(data_get.content)
cookie['xxmc'] = quote(quote(data_get_cookie['xxmc']))
cookie['xxms'] = quote(quote(data_get_cookie['xmms']))
cookie['loginType'] = data_get_cookie['xsjs']
cookie['versinStr'] = quote(quote(data_get_cookie['version']))
loginparam = {}
loginparam['loginName'] = loginname
loginparam['yzxx'] = yzxx
loginparam['loginType'] = cookie['loginType']
session = requests.session()
login_info = session.post('http://yqjk.jgsu.edu.cn:8090/public/getLoginInfoByLoginName', data=loginparam,
                          proxies=proxies)
login_info_dict = json.loads(login_info.content)
sessionid = login_info.headers['Set-Cookie'].split(';')[0].split('=')[1]
cookie['JSESSIONID'] = sessionid
url = 'http://yqjk.jgsu.edu.cn:8090/public/homeQd?loginName=' + loginname + '&loginType=0'
login_main = session.get(url, proxies=proxies)
studentQdQj = {'qjlx': '0', 'qjjzrq': ''}
signin_param = {'studentQdQj': json.dumps(studentQdQj), 'studentQd': json.dumps(studentQd)}


def signin_function():
    signin_post = session.post('http://yqjk.jgsu.edu.cn:8090/studentQd/qdStudentByXh', data=signin_param,
                               proxies=proxies)
    print(signin_post.content.decode('utf-8'))
    form_post = session.post('http://yqjk.jgsu.edu.cn:8090/dcwjEditNew/dcwjSubmit2',
                             data={'dcwj': json.dumps(form_param)}, proxies=proxies)
    print(form_post.content.decode('utf-8'))


if __name__ == '__main__':
    signin_function()

# print(url)
# print(quote(data_get_cookie['xxms']))
# print(data_get.headers)
# logininfo = http.request('POST', 'http://yqjk.jgsu.edu.cn:8090/public/getLoginInfoByLoginName', fields=loginparam)
# session = re.match(regrx,login_info.headers['Set-Cookie'])
# print(session.group(0))
# cookiedata = ''
# signin_param_data = ''
'''
for key in cookie.keys():
    cookiedata += key
    cookiedata += '='
    cookiedata += cookie[key]
    cookiedata += ';'
for data in signin_param.keys():
    signin_param_data += data
    signin_param_data += '='
    signin_param_data += signin_param[data]
    signin_param_data += ';'
'''
# signin_post = requests.post('http://yqjk.jgsu.edu.cn:8090/studentQd/qdStudentByXh',data=signin_param,cookies=cookie)
# print(signin_param_data)
# print(signin_post.content.decode('utf-8'))

# print(headers)
# signin_post = http.request('POST','http://yqjk.jgsu.edu.cn:8090/studentQd/qdStudentByXh',fields=quote(signin_param_data),headers=headers)
# print(signin_post.status)

# loginrequest_url = 'http://yqjk.jgsu.edu.cn:8090/public/homeQd?loginName=' + loginname + '&loginType=' + cookie['loginType']
# loginrequest = http.request('GET', loginrequest_url)
# print(loginrequest.data)
# print(loginrequest.headers[''])
# print('http://yqjk.jgsu.edu.cn:8090/public/homeQd?loginName='+loginname+'&loginType='+cookie['loginType'])
# for key in logininfo_dict.keys():
#    print(logininfo_dict[key])
# for key in data_get_cookie.keys():
#    print(key + ':' + data_get_cookie[key])
