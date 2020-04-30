from view import App
from log import Logger
from model import DictionaryReader

def main():
    dr = DictionaryReader()
    MyApp = App()
    MyApp.set_next_button_callback(dr.get_random_word)
    MyApp.set_reload_button_callback(dr.reload_dictionary)
    MyApp.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger = Logger()
        logger.error("Interrupt detected")