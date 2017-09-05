# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppLogin10(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—位数错误的数字账号，登录提示信息检查'  # 用例名称
        self.zentao_id = 1895  # 禅道ID

    # 用例动作
    def case(self):
        try:
            user_name = self.widget_click(self.page["login_page"]["username"],
                                          self.page["login_page"]["title"])

            # 发送数据
            data = "1"
            user_name.clear()
            self.ac.send_keys(user_name, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["位数错误用户名"] input success')
            time.sleep(0.5)

            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            login_pwd = self.widget_click(self.page["login_page"]["password"],
                                          self.page["login_page"]["title"])

            data = self.user["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            login_pwd.clear()
            self.ac.send_keys(login_pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["登录密码"] input success')
            time.sleep(0.5)

            widget_px = self.ac.get_location(self.wait_widget(self.page["login_page"]["login_button"]))
            self.driver.tap([widget_px["centre"]])
            self.logger.info(u'[APP_CLICK] operate_widget success')

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            try:
                user_name = self.widget_click(self.page["login_page"]["username"],
                                              self.page["login_page"]["title"])

                # 发送数据
                data = self.user["user_name"]
                data = str(data).decode('hex').replace(" ", "")
                user_name.clear()
                self.ac.send_keys(user_name, data, self.driver)
                self.logger.info(u'[APP_INPUT] ["正确用户名"] input success')
                time.sleep(0.5)

                self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
                login_pwd = self.widget_click(self.page["login_page"]["password"],
                                              self.page["login_page"]["title"])

                data = self.user["login_pwd"]
                data = str(data).decode('hex').replace(" ", "")
                login_pwd.clear()
                self.ac.send_keys(login_pwd, data, self.driver)
                self.logger.info(u'[APP_INPUT] ["正确密码"] input success')
                self.widget_click(self.page["login_page"]["login_button"],
                                  self.page["device_page"]["title"])
            except TimeoutException:
                self.wait_pwd_timeout()
                try:
                    self.wait_widget(self.page["device_page"]["title"])
                except TimeoutException:
                    self.widget_click(self.page["login_page"]["login_button"],
                                      self.page["device_page"]["title"])

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)
