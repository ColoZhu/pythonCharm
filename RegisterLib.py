from selenium import webdriver
from pprint import pprint

class RegisterLib:
    def __init__(self):
        driver = webdriver.Chrome("D:\Automation\cdriver\chromedriver.exe")
        self.driver=driver

    def teacher_register(self,username,password):
        driver=self.driver
        driver.get("http://ci.ytesting.com/portal/home.html")
        driver.implicitly_wait(3)
        #点击【老师登陆】按钮
        driver.find_element_by_css_selector("[class='teacher'] a").click()
        #输入账号跟密码进行登录
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit").click()

        #driver.close()
    def teacher_check_classStudentIsNone(self):
        #老师角色点击班级学生菜单
        div=self.driver.find_element_by_css_selector("[class='main-menu']")
        div.find_element_by_css_selector("[class='menu-title']").click()
        #核对班级学生，班级学生为空
        list=self.driver.find_element_by_css_selector("[class*='col-lg-7']")
        if list==[]:
            pprint("为空")

    def teacher_check_classStudentIsnotNone(self):
        #老师角色点击班级学生菜单
        div=self.driver.find_element_by_css_selector("[class='main-menu']")
        div.find_element_by_css_selector("[class='menu-title']").click()
        #核对班级学生，班级学生为空
        list=self.driver.find_element_by_css_selector("[class*='col-lg-7']")
        if list !=[]:
            pprint("bu为空")
    def homepage_message_IsTrue(self):
        table=self.driver.find_element_by_css_selector("[class*='table-hover']")
        tb=table.find_elements_by_css_selector("[class*='ng-binding']")
        pprint(tb)
        index = 0
        for one in tb:
            pprint(one.text)
            for num in range(0,4):
                if num==0 and one.text=="松勤学院0196":
                    pprint("学校pass")
                if num==1 and one.text=="zhuzhuz":
                    pprint("姓名pass")
                if index==2 and one.text=="初中英语":
                    pprint("学科pass")
                if index==3 and one.text=="0":
                    pprint("金币pass")
    def student_register(self):
        pass

if __name__ == '__main__':
    tc=RegisterLib()
    tc.teacher_register("zhuzhuz",888888)
    tc.homepage_message_IsTrue()