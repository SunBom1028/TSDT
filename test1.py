from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table=self.browser.find_element(By.ID,'id_list_table')
        rows=table.find_elements(By.TAG_NAME,'tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #张三听说有一个在线待办事项的应用
        #他去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        #他注意到网页里包含To-Do这个词
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element(By.TAG_NAME,'h1').text  #(1)
        self.assertIn('To-Do',header_text)

        #有一个输入待办事项的文本输入框
        inputbox=self.browser.find_element(By.ID,'id_new_item')  #(1)
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        #输入了Buy flowers
        inputbox.send_keys('Buy flowers')  #(2)

        #按了回车，页面更新了
        #待办事项列表中显示了1：Buy flowers
        inputbox.send_keys(Keys.ENTER)  #(3)
        time.sleep(1)  #(4)
        self.check_for_row_in_list_table('1: Buy flowers')

        #页面中又出现了一个文本输入框，可以输入其他待办事项
        #他输入了Give a gift to Lisi
        inputbox=self.browser.find_element(By.ID,'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        #页面再次更新，清单上显示两个待办事项
        self.check_for_row_in_list_table('1: Buy flowers')
        self.check_for_row_in_list_table('2: Give a gift to Lisi')

        #张三想知道网站是否记住清单
        #他看到网站为他生成了唯一的URL
        self.fail('Finish the test!')
        #他访问了那个URL，发现待办事项还在
        #满意离开


if __name__ == '__main__':
    unittest.main()

