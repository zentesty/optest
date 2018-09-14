import os
import sys
import yaml


class MyLoader:

    color: str = "DARK BLUE"
    temperature = 119

    def __init__(self):
        pass

    def load_file(self):
        self.color = self.__load_entry_from_config_file("general", "version", self.color)


    '''
        Loader from file
    '''
    def __load_entry_from_config_file(self, section, entry, existing_value):
        path_config_file = os.path.join(os.path.split(os.environ['VIRTUAL_ENV'])[0], "config.yaml")
        try:
            open_file = open(path_config_file, 'r')
        except FileNotFoundError:
            print("FileNotFoundError: Configuration file not found at " + path_config_file)
            return existing_value

        # if the file exists it get loaded for data extraction
        with open_file as stream:
            data_loaded = yaml.load(stream)
        try:
            val = data_loaded[section][entry]
            if val is not None:
                return val
            else:
                return existing_value
        except KeyError as e:
            print("KeyError: was unable to find key [" + section + "] or [" + entry + "] in file " + path_config_file +
                  " with KeyError: " + str(e))
            return existing_value
        except Exception as e:
            print("Exception: while accessing key [" + section + "] or [" + entry + "] in file " + path_config_file +
                  " with exception: " + str(e))
            # todo: Add logging of the exception
            return existing_value


# print(os.path.split(os.environ['VIRTUAL_ENV'])[0])

print('---- STARTED ----')
loader = MyLoader()
loader.load_file()
print(loader.color)
print('----- ENDED -----')
