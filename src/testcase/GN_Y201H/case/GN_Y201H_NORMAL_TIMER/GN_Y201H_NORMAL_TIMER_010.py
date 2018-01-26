# coding=utf-8
from src.testcase.GN_Y201H.WidgetOperation import *


class GNY201HNormalTimer10(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"普通定时(#246)"  # 用例所属模块
        self.case_title = u'在线状态，1组开与1组关定时执行状态检查'  # 用例名称
        self.zentao_id = "2056"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")
        delay_s = 120 + 2 * ((59 + 23) * 1)

        time_1, time_2 = 2, 4
        start_time_1, set_time_1, start_time_2, set_time_2, cycle1, cycle2 = self.create_normal_timer(
            now, time_1, time_2, delay_s=delay_s)

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.check_timer(start_time_1, set_time_1, u"电源已开启", cycle1)
        self.check_timer(start_time_2, set_time_2, u"电源已关闭", cycle2)
