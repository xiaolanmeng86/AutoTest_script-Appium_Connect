# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppRegister13(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-用户名为空，注册验证'  # 用例名称
        self.zentao_id = 1825  # 禅道ID

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"])

            user_name = self.widget_click(self.page["register_page"]["username"],
                                          self.page["register_page"]["title"])

            # 发送数据
            data = ""
            user_name.clear()
            self.ac.send_keys(user_name, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["空白用户名"] input success')
            time.sleep(0.5)

            self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
            pwd = self.widget_click(self.page["register_page"]["password"],
                                    self.page["register_page"]["title"])

            data = "1234"
            pwd.clear()
            self.ac.send_keys(pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["注册密码"] input success')
            time.sleep(0.5)

            check_code = self.widget_click(self.page["register_page"]["check_code"],
                                           self.page["register_page"]["title"])

            data = "123456"
            check_code.clear()
            self.ac.send_keys(check_code, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            widget_px = self.ac.get_location(self.wait_widget(self.page["register_page"]["register_button"]))
            self.driver.tap([widget_px["centre"]])
            self.logger.info(u'[APP_CLICK] operate_widget success')

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)
