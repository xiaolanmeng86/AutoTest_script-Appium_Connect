# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppThemeStyle1(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"主题风格"  # 用例所属模块
        self.case_title = u'返回按钮功能检查'  # 用例名称
        self.zentao_id = 1986  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["theme_style"],
                              self.page["theme_style_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["theme_style_page"]["title"],
                              self.page["theme_style_page"]["to_return"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

