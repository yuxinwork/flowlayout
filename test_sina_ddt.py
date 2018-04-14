#!/usr/bin/env python 
#-*-coding:utf-8-*-

from selenium import  webdriver


import  unittest
import  os
from ddt import  ddt,data,unpack


def getData():
	return [['', '', u'请输入邮箱名'],['', 'asd', u'请输入邮箱名'],['asd', 'asd', u'您输入的邮箱名格式不正确']
	]

@ddt
class SingTest(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get('http://mail.sina.com.cn/#')
		self.driver.implicitly_wait(30)

	def tearDown(self):
		self.driver.quit()

	@data(*getData())
	@unpack
	def test_username_password_null(self,username,password,result):
		'''验证：sina邮箱登录的测试'''
		self.driver.find_element_by_id('freename').send_keys(username)
		self.driver.find_element_by_id('freepassword').send_keys(password)
		self.driver.find_element_by_link_text(u'登录').click()
		error_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
		self.assertEqual(error_text,result)

	# def test_username_null(self):
	# 	'''验证：用户名权为空，密码不为空的错误提示信息'''
	# 	self.driver.find_element_by_id('freename').send_keys('')
	# 	self.driver.find_element_by_id('freepassword').send_keys('asd')
	# 	self.driver.find_element_by_link_text(u'登录').click()
	# 	error_text = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
	# 	self.assertEqual(error_text,u'请输入邮箱名')

if __name__ == '__main__':
    unittest.main(verbosity=2)
