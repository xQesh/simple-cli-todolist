import sys
import os
import json
import time

#Set True when you want to get additional informations about app processes / errors
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
    @staticmethod
    def get():
        try:
            with open('tasks.json', 'r') as tasks:
                return json.load(tasks)
            if DEV_MODE: print('Data file loaded correctly')
        except:
            print('Data file loading error')

    @staticmethod    
    def upload(data):
        try:
            with open('tasks.json', 'w') as cfg:
                json.dump(data, cfg, indent = 4)
            if DEV_MODE: print('Data file saved correctly')
        except:
            print('Data file editing error')

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
                
            Main()

            if DEV_MODE:
                print('Cannot match any task ID')
                time.sleep(2)

    def add(self):
        os.system('cls')
        print('CREATING TASK')
        title = input('Title: ')
        descritpion = input('Description: ')
        
        data = self.get()

        id = len(data) + 1

        data[id] = {
            "title": title,
            "description": descritpion,
            "completed": False,
        }

        self.upload(data)

        if DEV_MODE:
            print('New task successfully created')
            time.sleep(2)

    def edit(self, id):
            data = self.get()
            for task_id, info in data.items():
                if task_id == id:
                    os.system('cls')
                    print('Current title: ', info['title'])
                    title = input('New title: ')

                    if title.strip() == "":
                        pass
                    else:
                        info['title'] = title

                    print('Current description: ', info['description'])
                    description = input('New description: ')

                    if description.strip() == "":
                        pass
                    else:
                        info['description'] = description

                    status = input('Completed? ( yes | no ): ')

                    if status == "yes":
                        info['completed'] = True
                    elif status == "no":
                        info['completed'] = False

                    self.upload(data)

                    if DEV_MODE:
                        print('Task edited successfully')
                        time.sleep(2)

                    return 
 

    def delete(self, id):
        data = self.get()

        del data[id]
        
        self.upload(data)

        if DEV_MODE:
            print('Task deleted successfully')
            time.sleep(2)

class Main:
    def __init__(self):
        handler = TasksHandler()

        running = True
        while running:
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

            print('Choose task by ID or quit')
            choice_main = input('Option ( ID | add | quit ): ')

            if choice_main == 'quit':
                sys.exit()
            elif choice_main == 'add':
                checking_details = False
                handler.add()
            else:
                checking_details = True
                while checking_details:
                    handler.detailed_mode(choice_main)
                    print('-------------------')
                    choice_detailed = input('Option ( edit | delete | back ): ')

                    if choice_detailed == 'edit':
                        checking_details = False
                        handler.edit(choice_main)
                    elif choice_detailed == 'delete':
                        checking_details = False
                        handler.delete(choice_main)
                    elif choice_detailed == 'back':
                        checking_details = False
                    else:
                        if DEV_MODE:
                            print('Invalid option')
                            time.sleep(2)
    if DEV_MODE:
        def __del__(self):
            print('Main object deleted')


class Launcher:
    config = ConfigHandler.get()
    
    if config['firstlaunch'] or config['username'] == "":
        config['username'] = input("Name: ")
        config['firstlaunch'] = False
        ConfigHandler.upload(config)

    Main()

Launcher()