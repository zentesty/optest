#
# StopWatch class used to
#
from testing_framwork.fw_log.fw_metrics import basemetric


class StopWatchTimeTracker(basemetric.BaseMetric):
    __instances = {}

    @staticmethod
    def get_instance(name):
        """ Static access method. """
        try:
            StopWatchTimeTracker.__instances[name]
        except KeyError:
            StopWatchTimeTracker(name)
        # if StopWatchTimeTracker.__instances[name] == None:
        #     StopWatchTimeTracker(name)
        return StopWatchTimeTracker.__instances[name]

    start_time = 0
    end_time = 0
    elapsed_time = 0
    pause_start = 0
    total_paused_time = 0
    array_events = []

    def __init__(self, name):
        self.array_action = None
        """ Virtually private constructor. """
        try:
            StopWatchTimeTracker.__instances[name]
            raise Exception("This class is a singleton, obtain instance via the get_instance static method")
        except KeyError:
            pass
        StopWatchTimeTracker.__instances[name] = self

    def start_timer(self):
        self.unpause_timer()
        print(str(len(self.array_events)))
        if len(self.array_events) > 0:
            self.array_events.append(StopWatchTimeTracker.TimeTrackerLaps())
            self.start_time = self.array_events.index(StopWatchTimeTracker.TimeTrackerLaps)

    def pause_timer(self):
        if self.start_time != 0 and self.pause_start == 0:
            self.pause_start = basemetric.current_time_millis()
            return True
        else:
            return False

    def unpause_timer(self):
        if self.pause_start != 0:
            pause_time = current_time_millis() - self.pause_start
            self.total_paused_time += pause_time;
            self.array_event[len(self.array_event) - 1].offset_start_for_pause(pause_time)
            return True;
        else:
            return False;

    def stop_timer(self):
        if self.start_time != 0:
            self.unpause_timer()
            self.array_events[len(self.array_event) - 1].end_lap()
            self.end_time = basemetric.current_time_millis()
            self.elapsed_time = self.end_time - (self.start_time + self.total_paused_time)
            return self.elapsed_time
        else:
            return 0;

    def lap(self, info):
        if len(self.array_events) > 0 and self.pause_start == 0:
            self.array_events[len(self.array_event) - 1].end_lap()
            self.array_events.append(StopWatchTimeTracker.TimeTrackerLaps(info))
        return len(self.array_events)

    def reset_timer(self):
        self.array_events = []

    def getDuration(self):
        return self.end_time - (self.start_time + self.total_paused_time)

    def get_number_laps(self):
        return len(self.array_events)

    '''
            Inner class 
            Class that holds every timed tracked laps information
        '''

    class TimeTrackerLaps:
        time_stamp = 0
        lap_start = 0
        elapsed_time = 0
        description = ""

        def __init__(self, info=""):
            self.description = info

        def end_laps(self):
            self.elapsed_time = basemetric.current_time_millis() - self.time_stamp

        @property
        def time_stamp(self):
            return self.__time_stamp

        @time_stamp.setter
        def time_stamp(self, val):
            self.__time_stamp = val

        def offset_start_for_pause(self, offset):
            self.lap_start += offset





