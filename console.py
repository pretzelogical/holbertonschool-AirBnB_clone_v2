#!/usr/bin/python3
""" Console to manage the hbnb data"""


import cmd
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit the program when End-of-File (EOF) character is received
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered
        """
        pass

    def help_quit(self):
        """
        Help documentation for the quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help documentation for the EOF command
        """
        print("Exit the program when End-of-File (EOF) character is received")

    def do_create(self, args):
        """
        Create a new instance of BaseModel, save it to the JSON file, and print the id
        """
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        Print the string representation of an instance based on the class name and id
        """
        if not args:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                obj_dict = storage.all()
                instance_key = "{}.{}".format(args_list[0], args_list[1])
                if instance_key in obj_dict:
                    print(obj_dict[instance_key])
                else:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
