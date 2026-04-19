import requests
import pytest

def test_get(test_data, base_url):
    url = base_url + test_data["endpoints"]["get"]
    response = requests.get(url)
    assert response.status_code == test_data["expected_status"], "状态码不对"
    print("GET测试通过")

def test_post(test_data, base_url):
    url = base_url + test_data["endpoints"]["post"]
    response = requests.post(url)
    assert response.status_code == test_data["expected_status"], "状态码不对"
    print("POST测试通过")


@pytest.mark.parametrize("method,status_code,url",[                     #参数化可以让一个函数跑多组数据
                             ('get',200,'http://httpbin.org/get'),
                             ('post',200,'http://httpbin.org/post'),
                         ])
def test_parametrize(method,status_code,url):
    if method == 'get':
        response = requests.get(url)
    else:
        response = requests.post(url)
    assert response.status_code == status_code,f'状态码不对，实际是{response.status_code}'
    print(f'测试通过:{url}')