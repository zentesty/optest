#
#   This file defines the interface an orchestrator must implement
#
import abc


class IOrchestrator:

    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self):
        '''
            This method will invoke the execution of the creation
        :return: a boolean indicating the success or failure of the test 
        ''''''
        '''

    @abc.abstractmethod
    def pause(self):
        '''
            put the execution on a stand by mode that can or cannot be resumed
        :return: a long indicating the number of milliseconds elapse since the code started excuting

        '''