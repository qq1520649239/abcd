# from vv import HTMLTestRunnerCN
import HTMLTestRunnerCN
import unittest
#文件路径    
Testcase_dir = 'C:\\Users\\15206\\PycharmProjects\\pythonProject\\vv'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'ces.py')
# 定义报告存放路径
filename = "C:\\Users\\15206\\PycharmProjects\\pythonProject\\baogao\\ces.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="描述：")
    # 运行测试用例
runner.run(dis)
#关闭报告文件
fp.close()