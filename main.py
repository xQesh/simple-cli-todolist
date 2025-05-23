import sys
import os
import json

#Set True when you want to get additional informations about app processes
DEV_MODE = True

class ConfigHandler:
    def get():
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
    #def __init__(self):
    #    self.get()

    @staticmethod
    def get():
        with open('tasks.json', 'r') as tasks:
            return json.load(tasks)
        
    def detailed_mode(self, id):
            for task_id, info in self.get().items():
                if task_id == id:
                    os.system('cls')
                    print('ID:', id)
                    print('TITLE:', info["title"])
                    print('DESCRIPTION:', info["description"])
                    if info["completed"]:
                        status = 'completed'
                    else:
                        status = 'uncompleted'
                    print('STATUS:', status)
                    return

            if DEV_MODE:
                print('ID that you chose dont match any task')

    def add():
        pass

    def delete():
        pass

    def change():
        pass

class Main:
    def __init__(self):
        os.system('cls')          
        username = ConfigHandler.get()['username']
        print(f'Welcome {username}!')
        print('Your tasks:')
        print("ID       TITLE      STATUS")

        tasks = TasksHandler.get()

        for id, info in tasks.items():    
            if info["completed"]: 
                status = "COMPLETED" 
            else: 
                status = "UNCOMPLETED"
            print(f'{id} - {info["title"]} - {status}')


        while True:
            print('Choose task by ID or quit')
            choice = input('Option: ')
            if choice == 'quit':
                sys.exit()
            else:
                handler = TasksHandler()
                handler.detailed_mode(choice)

class Launcher:
    config = ConfigHandler.get()
    
    if config['firstlaunch'] or config['username'] == "":
        config['username'] = input("Name: ")
        config['firstlaunch'] = False
        ConfigHandler.upload(config)

    Main()

Launcher()