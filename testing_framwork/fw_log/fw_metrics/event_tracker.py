#
#
#
from testing_framwork.fw_log.fw_metrics import basemetric
import time


class EventCountTracker(basemetric.BaseMetric):
    __instances = {}

    @staticmethod
    def get_instance(name):
        """ Static access method. """
        try:
            EventCountTracker.__instances[name]
        except KeyError:
            EventCountTracker(name)
        # if StopWatchTimeTracker.__instances[name] == None:
        #     StopWatchTimeTracker(name)
        return EventCountTracker.__instances[name]

    def __init__(self, name):
        self.array_action = None
        """ Virtually private constructor. """
        try:
            EventCountTracker.__instances[name]
            raise Exception("This class is a singleton, obtain instance via the get_instance static method")
        except KeyError:
            pass
        EventCountTracker.__instances[name] = self

    __array_events = []

    def add_event_occurrence(self, description, count=1):
        self.__array_events.append(EventCountTracker.EventCountOccurrence(description, count))
        return len(self.__array_events)

    def reset_event_occurrences(self):
        self.__array_events = []
        return len(self.__array_events)

    def get_count_event_entries(self):
        return len(self.__array_events)

    def get_sum_event_entries(self):
        e: EventCountTracker.EventCountOccurrence
        count = 0
        for e in self.__array_events:
            count += e.event_count
        return count

    def get_average_event_entries(self):
        if len(self.__array_events) > 0:
            return self.get_sum_event_entries() / len(self.__array_events)
        else:
            return 0

    def get_min_event_entries(self):
        e: EventCountTracker.EventCountOccurrence
        if len(self.__array_events) > 0:
            min_val = self.__array_events.index(0).event_count
            for e in self.__array_events:
                if e.event_count < min_val:
                    min_val = e.event_count
            return min_val
        else:
            return 0

    def get_max_event_entries(self):
        e: EventCountTracker.EventCountOccurrence
        if len(self.__array_events) > 0:
            max_val = 0
            for e in self.__array_events:
                if e.event_count > max_val:
                    max_val = e.event_count
            return max_val
        else:
            return 0

    def get_standard_dev_event_entries(self):
        pass

    def debug_dump_array(self):
        e: EventCountTracker.EventCountOccurrence
        for e in self.__array_events:
            print(e)


    # This inner class contains the occurrences of event allowing
    # for
    class EventCountOccurrence:
        event_time = 0
        event_count = 0
        description = ""

        def __init__(self, description, count=1):
            self.event_time = basemetric.current_time_millis()
            self.description = description
            self.event_count = count

        def __str__(self):
            return self.description + " with " + str(self.event_count) + " occurrences at " + str(self.event_time)


test = EventCountTracker("MPR")
test.add_event_occurrence("RunX", 12)
test2 = EventCountTracker.get_instance("MPR")
time.sleep(0.001)
test.add_event_occurrence("RunY", 33)
time.sleep(0.009)
test.add_event_occurrence("RunZ", 19)
test.debug_dump_array()