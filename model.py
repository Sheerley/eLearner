import random
import os
from config import config
from log import Logger

class Configuration():
    pass #TODO: implement

class DictionaryReader():
    word_list = None
    logger = None
    filename = None

    def __init__(self): #TODO: implement config
        self.logger = Logger() # TODO: refractor
        try:
            filepath = os.path.expanduser(config.get('dictionary location'))
            self.read_file(filepath)
        except FileNotFoundError as err:
            self.logger.error(err) # TODO: refractor

    def reload_dictionary(self):
        self.logger.info("Reloading dictionary")
        self.read_file(self.filename)

    def read_file(self, filename):
        self.filename = filename
        try:
            with open(filename, 'r') as f:
                content = f.read()
                splitted = content.split('\n')
                only_unique = (list(set(splitted)))
                sorted_data = sorted(only_unique)
                self.word_list = sorted_data
        except FileNotFoundError as err:
            self.logger.error(err) #TODO: refractor
            try:
                with open(filename, 'w') as f:
                    f.write('Sample\ndata\nin the\ndictionary')
            except IOError as err:
                self.logger.error(err)
        except PermissionError as err:
            self.logger.error(err) #TODO: refractor
        except OSError as err:
            self.logger.error(err) #TODO: refractor
    
    def get_random_word(self):
        if len(self.word_list) > 0:
            random_entry = random.randrange(0, len(self.word_list), 1)
            word = self.word_list[random_entry]
            if config.get('remove words from pool'):
                self.word_list.remove(word)
            return word
        else:
            self.logger.info('Dictionary emptied')
            return 'Greetings! You emptied the pool!'