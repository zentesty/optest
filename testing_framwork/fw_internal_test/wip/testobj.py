from testing_framwork.fw_log.fw_metrics import metric_decorator


class TestObj:
    def __init__(self):
        self.name = "bob"

    @metric_decorator.fw_metric
    def call_get_my_new_name(self):
        print("In my method")
        return self.name


test = TestObj()
test.call_get_my_new_name()

