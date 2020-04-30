import enum
import os
import sys
import time 

class LogLevel(enum.IntEnum):
    DEBUG = 0
    WARNING = 1
    ERROR = 2
    NONE = 3

    def __str__(self):
        return self.name

#TODO: refractor
class Logger():
    class __Logger():
        level = None
        log_file = None
        run_time = None

        def __init__(self, level):
            self.level = level
            self.run_time = time.time()
            try:
                os.mkdir(os.path.expanduser('~/log'));
            except FileExistsError as err:
                pass
            except IOError as err:
                print(err, file=sys.stderr)
            self.log_file = os.path.expanduser('~') + '/log/' + str(self.run_time) + '.txt'

            for f in os.listdir(os.path.expanduser('~/log/')):
                if os.stat(os.path.expanduser('~/log/') + f).st_mtime < self.run_time - 7 * 24 * 60 * 60:
                    if os.path.isfile(os.path.expanduser('~/log/') + f):
                        os.remove(os.path.expanduser('~/log/') + f)

        def set_level(self, level):
            self.level = level

        def write(self, string):
            try:
                with open(self.log_file, 'a') as f:
                    f.write(string + '\n')
            except FileNotFoundError as e:
                print(e, file=sys.stderr)

        def __del__(self):
            pass #TODO: implement sending log file on destroy

    instance = None

    def __init__(self):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(LogLevel.DEBUG)

    def set_level(self, level):
        self.instance.set_level(level)

    def get_current_time(self):
        return time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

    def error(self, message):
        if self.instance.level <= LogLevel.ERROR:
            log = '[' + str(LogLevel.ERROR) + '] ' + str(self.get_current_time()) + ' : ' + str(message)
            print(message, file=sys.stderr)
            self.instance.write(str(log))

    def info(self, message):
        if self.instance.level <= LogLevel.DEBUG:
            log = '[' + str(LogLevel.DEBUG) + '] ' + str(self.get_current_time()) + ' : ' + str(message)
            print(message, file=sys.stderr)
            self.instance.write(str(log))

    def warning(self, message):
        if self.instance.level <= LogLevel.WARNING:
            log = '[' + str(LogLevel.WARNING) + '] ' + str(self.get_current_time()) + ' : ' + str(message)
            print(message, file=sys.stderr)
            self.instance.write(str(log))
