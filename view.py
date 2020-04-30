from tkinter import *
from tkinter import ttk
from config import config
import os
import webbrowser

class App():
    window = None
    title = None
    tab_control = None
    about_tab = None
    program_tab = None
    settings_tab = None
    current_word = None
    next_button = None
    reload_dictionary_button = None
    next_button_callback = None
    reload_button_callback = None
    open_dictionary_button = None
    change_removing_button = None
    cat_button = None

    def __init__(self):
        self.title = config.get('application name')
        self.__create_window()
        self.__create_notebook()

    def set_next_button_callback(self, callback):
        self.next_button_callback = callback

    def set_reload_button_callback(self, callback):
        self.reload_button_callback = callback

    def __create_window(self):
        self.window = Tk()
        self.window.title(self.title)
        self.window.geometry('350x200')

    def __create_notebook(self):
        self.tab_control = ttk.Notebook(self.window)
        self.__create_main_tab()
        self.__create_about_tab()
        self.__create_settings_tab()
        self.tab_control.pack(expand=1, fill='both')

    def __create_settings_tab(self):
        self.settings_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.settings_tab, text='Settings')
        self.__add_dictionary_button()
        self.__add_change_button()
        self.__add_cat_button()

    def __add_cat_button(self):
        self.cat_button = Button(self.settings_tab, text='Show me cats!', command=self.__cat_button_clicked)
        self.cat_button.pack(side=TOP, expand=1)

    def __cat_button_clicked(self):
        webbrowser.open_new(r'https://www.reddit.com/r/cats/')
    
    def __add_change_button(self):
        self.change_removing_button = Button(self.settings_tab, text='Remove word from pool = ' + str(config.get('remove words from pool')), command=self.__remove_button_clicked)
        self.change_removing_button.pack(side=TOP, expand=1)
    
    def __remove_button_clicked(self):
        config['remove words from pool'] = not config['remove words from pool']
        self.reload_button_callback()
        self.change_removing_button.configure(text='Remove word from pool = ' + str(config.get('remove words from pool')))

    def __add_dictionary_button(self):
        self.open_dictionary_button = Button(self.settings_tab, text='Edit dictionary', command=self.__dictionary_button_clicked)
        self.open_dictionary_button.pack(side=TOP, expand=1)

    def __dictionary_button_clicked(self):
        os.system("start " + os.path.expanduser(config.get('dictionary location')))

    def __create_about_tab(self):
        self.about_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.about_tab, text='About')
        lbl = Label(self.about_tab, text=self.__create_about())
        lbl.pack(side=BOTTOM, expand=1)

    def __create_about(self):
        message = "Name: " + config.get('application name') + '\n'
        message += "Version: " + str(config.get('version')) + '\n'
        message += "Author: " + config.get('author') + '\n'
        message += "License: " + config.get('license') + '\n'
        return message

    def __create_main_tab(self):
        self.program_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.program_tab, text='Main')
        self.__add_reload_button()
        self.current_word = Label(self.program_tab, text= '')
        self.current_word.pack(side=TOP, expand=1)
        self.__add_next_button()

    def __next_button_clicked(self):
        word = self.next_button_callback()
        self.current_word.configure(text=word)

    def __add_next_button(self):
        self.next_button = Button(self.program_tab, text='Next word', command=self.__next_button_clicked)
        self.next_button.pack(side=BOTTOM, expand=1)

    def __reload_button_clicked(self):
        self.reload_button_callback()
        self.__next_button_clicked()

    def __add_reload_button(self):
        self.next_button = Button(self.program_tab, text='Reload dictionary', command=self.__reload_button_clicked)
        self.next_button.pack(side=TOP, expand=1)

    def run(self):
        self.window.mainloop()


