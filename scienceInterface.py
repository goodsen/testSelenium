import requests
import unittest

#定义接口测试类
class scienceInterface(unittest.TestCase):
    #定义启动方法
    def setUp(self):
        print("开始测试")
        self.url = ""
    def test_get_event_null(self):
        r = requests.get(self.url,params={'key':'value'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")
    def test_get_event_success(self):
        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message',"success"])
        self.assertEqual(result['data']['name'],"xx产品发布会")
        self.assertEqual(result['data']['address'],"北京奥林匹克公园水立方")
        #self.assertEqual(result['data'])['start_time',"2016-10-15T18:00:00"]
    def tearDown(self):
        print("结束测试")
if __name__ == '__main__':
    unittest.main()