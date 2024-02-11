#!/usr/bin/python3
"""Define a class that inherts from cmd module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "State": State,
        "Review": Review,
        "Amenity": Amenity
        }


def check_error(arg):
    """checking error class"""
    if arg == "":
        print("** class name missing **")
    elif arg not in classes.keys():
        print("** class doesn't exist **")
    else:
        return True


def check_id(cls_name, id):
    """checking error class"""
    keey = f"{cls_name}"
    key = f"{classes[keey].__name__}.{id}"
    if id == "":
        print("** instance id missing **")
    elif key not in storage.all().keys():
        print("** no instance found **")
    else:
        return storage.all()[key]


def check_type(typ):
    """check type of data type"""
    try:
        typ = typ.split('"')[1]
        if '.' in typ:
            return float(typ)
        return int(typ)
    except (IndexError, ValueError):
        return typ


class HBNBCommand(cmd.Cmd):
    """start class"""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """usage: create an instance of class"""
        if check_error(arg):
            instance = classes[arg]()
            print(instance.id)
            storage.save()

    def do_show(self, arg):
        """usage: shows [class] the classes with id"""
        args = arg.split() + ['', '']
        if check_error(args[0]):
            instance = check_id(args[0], args[1])
            instance and print(instance)

    def do_destroy(self, arg):
        """usage: destory [class] delete an object"""
        args = arg.split() + ['', '']
        cls_name = args[0]
        id_ins = args[1]
        if check_error(args[0]):
            instance = check_id(cls_name, id_ins)
            if instance:
                key = f"{cls_name}.{id_ins}"
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """usage: all [class] display all objects"""
        ins_list = []
        if arg == "":
            ins_list = [str(val) for val in storage.all().values()]
            print(ins_list)
        elif check_error(arg):
            for value in storage.all().values():
                if arg == value.__class__.__name__:
                    ins_list.append(str(value))
            print(ins_list)

    def do_update(self, arg):
        """usage: update [class] updates objects"""
        args = arg.split(" ", 3) + ["", "", "", ""]
        cls_name, id, attribut, new_val = args[:4]
        new_val = check_type(new_val)
        if check_error(cls_name) and (instance := check_id(cls_name, id)):
            if attribut == "":
                print("** attribute name missing **")
            elif new_val == "":
                print("** value missing **")
            else:
                setattr(instance, attribut, new_val)
                instance.save()
                storage.save()

    def do_help(self, arg):
        """usage: help [class] show all command"""
        super().do_help(arg)

    def emptyline(self):
        """you enter an empty line"""
        pass

    def do_quit(self, arg):
        """usage: Quit cmd"""
        return True

    def do_EOF(self, arg):
        """usage: <Ctrl-D> quit the console"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
