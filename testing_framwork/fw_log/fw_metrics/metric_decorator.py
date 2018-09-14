#
#   This describe the decorator needed to invoke the metric capture when doing performance and load testing
#
from functools import wraps
import inspect
from testing_framwork.fw_log.fw_metrics import stopwatch_tracker



stopwatch = stopwatch_tracker.StopWatchTimeTracker("metric1")

def fw_metric(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        #
        # post-method operation
        start_time = stopwatch_tracker.current_time_millis()
        #
        #
        try:
            r = func(*args, **kwargs)
        except Exception as e:
            #TODO: Log calling exception and suspend test execution
            pass
        #
        # post-method operation
        run_time = stopwatch_tracker.current_time_millis() - start_time

        calframe = inspect.getouterframes(inspect.currentframe(), 2)
        calling_method = calframe[1][4][1]
        print('caller name:', calling_method)
        # TODO: Log the elapsed time with the
        #
        #
        return r
    return wrapped




