#!/usr/bin/env python3
"""this is the console module of the hbnb project"""

import json
import cmd
import sys
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """this is a console"""
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, args):
        """this is a command to quit the console"""
        sys.exit(1)

    def do_EOF(self, arg):
        """close the programme"""
        print("")
        return  True

    def do_create(self, args):
        """this is to create an object
            create: <class name>
        """
        if not args:
            print("** class name missing **")
            return
        my_args = shlex.split(args)
        if my_args[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return 
        new_instance = HBNBCommand.classes[my_args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """this show a class instance based on the id
        show <className> <instanceid>
        """
        parse = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return

        if parse[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return

        if len(parse) <= 1:
            print("** instance id missing **")
            return
        storage.reload()

        all_objects = storage.all()
        key = parse[0] + "." + parse[1]
        if key in all_objects:
            ob = str(all_objects[key])
            print(ob)
        else:
            print("** no instance found **")


    def do_all(self, args):
        """this prints string representations of all the instance
        ie: all BaseModel or $ all
        """
        jsons = []
        arg = shlex.split(args)
        all_obj = storage.all()
        if not args:
            """if there are no args"""
            for key in all_obj:
                jsons.append(str(all_obj[key]))
            print(json.dumps(jsons))
            return

        if arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        else:
            for key in all_obj:
                if type(all_obj[key]).__name__ ==  arg[0]:
                    jsons.append(str(all_obj[key]))
            print(json.dumps(jsons))

    def do_destroy(self, args):
        """
        this deletes an instance of a class based on 
        the class name and id ie destroy BaseModel <id>
        """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objects = storage.all()
        key = arg[0] + "." + arg[1]
        if key in objects:
            del objects[key]
            storage.save()
            return
        else:
            print("** no instance found **")

    def do_update(self, args):
        """this is an update function 
        format:
        update <class name> <id> <attribute name> "<attribute value>"
        only one attribut can be updated
        """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objects = storage.all()
        key = ".".join(arg[:2])
        if key in objects:
            obj = objects[key]
        else:
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return

        if len(arg) == 3:
            print("** value missing **")
            return
        if len(arg) > 4 and arg[4] == "1":
            del arg[4]
        
            arg = arg[2:]
            for i in range(0, len(arg), 2):
                setattr(obj, arg[i], arg[i + 1])
                obj.save()
        else:
            setattr(obj, arg[2], arg[3])
            obj.save()





    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
