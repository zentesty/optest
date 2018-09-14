#
#  Base class for the metric gatherer
#
import time

class BaseMetric:
    class TYPE:
        TYPE_OTHER = 0
        TYPE_PERFORMANCE = 100
        TYPE_PERTINENCE = 200  # Coverage, density, ..
        TYPE_UX_FACTOR = 300
        TYPE_UNDEFINED = 10000

    name = None
    type = type

    def __init__(self, name, type=TYPE.TYPE_UNDEFINED):
        self.name = name
        self.type = type

    def serialize(self):
        # TODO: implement the serialization of the metric
        return self.serialized_stream

    def commit_metric(self):
        # TODO: implement db commit of the metric
        return self.name

#
#   Functions declaration
#
'''
    Function that return the current time in milliseconds. Useful to track events independantly 
    of a baseline simply relative to each others
'''


def current_time_millis():
    return int(round(time.time() * 1000))