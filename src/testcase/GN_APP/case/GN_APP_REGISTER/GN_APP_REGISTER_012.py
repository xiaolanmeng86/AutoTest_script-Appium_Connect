# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPRegister12(WidgetOperation):
    @case_run(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-用户名长度大于11位，提示信息检查'  # 用例名称
        self.zentao_id = "1826"  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_register"],
                          self.page["register_page"]["title"])

        self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
        user_name = self.widget_click(self.page["register_page"]["username"],
                                      self.page["register_page"]["title"])

        # 发送数据
        data = "138123412341"
        user_name.clear()
        self.ac.send_keys(user_name, data, self.driver)
        self.debug.info(u'[APP_INPUT] ["用户名"] input success')
        time.sleep(0.5)

        element = self.page["register_page"]["username"]
        user_name = self.ac.get_attribute(self.wait_widget(element), "name")
        self.debug.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (user_name, len(user_name)))
        user_name = user_name.replace(element[3]["default_text"], "")
        if len(user_name) != 11:
            raise TimeoutException("user name len is not 11, current is %s" % len(user_name))
