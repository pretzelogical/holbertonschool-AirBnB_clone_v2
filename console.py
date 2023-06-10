import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
