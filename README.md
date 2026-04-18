# Finance Test

基于pytest + requests的接口自动化测试项目

## 项目结构
- `conftest.py` - 全局fixture配置
- `test_data.json` - 测试数据
- `test_api.py` - 测试用例

## 运行方式
pip install requests pytest
pytest test_api.py -v