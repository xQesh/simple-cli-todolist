import sys
import os
import json

#Set True when you want to get additional informations about app processes
DEV_MODE = True

class ConfigHandler:
    def load():
        try:
            with open('config.json', 'r') as cfg:
                return json.load(cfg)
            if DEV_MODE: print('Config file loaded correctly')
        except:
            print('Config file loading error')

    def upload(config):
        try:
            with open('config.json', 'w') as cfg:
                json.dump(config, cfg, indent = 4)
            if DEV_MODE: print('Config file saved correctly')
        except:
            print('Config file editing error')

class TasksHandler:
    def load():
        with open('tasks.json', 'r') as tasks:
            return json.load(tasks)        

    def add():
        pass

    def delete():
        pass

    def change():
        pass

class Main:
    def __init__(self):
        os.system('cls')          
        username = ConfigHandler.load()['username']
        print(f'Welcome {username}!')
        print('Your tasks:')
        print("ID       TITLE      STATUS")

        tasks = TasksHandler.load()

        for id, info in tasks.items():    
            if info["completed"]: 
                status = "COMPLETED" 
            else: 
                status = "UNCOMPLETED"
            print(f'{id} - {info["title"]} - {status}') 

class Launcher:
    config = ConfigHandler.load()
    
    if config['firstlaunch'] or config['username'] == "":
        config['username'] = input("Name: ")
        config['firstlaunch'] = False
        ConfigHandler.upload(config)

    Main()

Launcher()