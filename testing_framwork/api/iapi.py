#
#
#
import abc


class ICallable:
    @abc.abstractmethod
    def create(self):
        '''

        :return:
        '''

    @abc.abstractmethod
    def delete(self):
        '''

        :return:
        '''

    @abc.abstractmethod
    def update(self):
        '''

        :return:
        '''

    @abc.abstractmethod
    def search(self):
        '''

        :return:
        '''