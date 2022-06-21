import cmd 
 
class CLI(cmd.Cmd): 
   def do_hola(self, line): 
       print("Hola") 
 
   def do_EOF(self, line): 
       return True 
 
if __name__ == '__main__': 
   CLI().cmdloop()
