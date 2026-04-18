import requests

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