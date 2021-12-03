import subprocess , os
from tkinter import messagebox
from tkinter import filedialog
class Cmd:
    def __init__(self,tk, app):
        
        self.app = app
        self.tk = tk 
        self.default_compileur_path_var = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dart-sass\\sass.bat")
        self.option = tk.IntVar()
        self.css_path_var = tk.StringVar()
        self.sass_path_var = tk.StringVar()
        
        self.label_error_var = tk.StringVar()


            
    def simple_compilation(self ,css_file:str ,sass_file:str):
        output = subprocess.Popen(f'{self.default_compileur_path_var} "{sass_file}" "{css_file}"', shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout , stderr = output.communicate()


        print(output.returncode)
        if output.returncode == 0:
            # print(stdout.decode())
            # print(stderr.decode().split()[0])
            self.label_error_var.set("")
        else:
        
            stderrlist = stderr.decode().split()
            file = stderrlist[-4].split('\\')[-1]
            message_error = f"{stderrlist[0]} {file} {stderrlist[1]} {stderrlist[2]} ligne : {stderrlist[-3].split(':')[0]}"
            print(stderr.decode())
            self.label_error_var.set(f"{message_error.lower()}")
            # print(message_error)


    def watch_compilation(self ,css_file:str ,sass_file:str):
        cmd = f'@echo off\n{self.default_compileur_path_var} "{sass_file}" "{css_file}" --watch'
        path = os.path.dirname(sass_file)+"/watch-file.bat"
        subprocess.os.system(f'start {self.default_compileur_path_var} "{sass_file}" "{css_file}" --watch')
        
        with open(path, "w+") as watch_file:
            watch_file.write(cmd)

        
    def compressor_css_file(self ,css_file:str ,sass_file:str):
        output = subprocess.Popen(f'{self.default_compileur_path_var} "{sass_file}" "{css_file}" --style=compressed --no-source-map',shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout , stderr = output.communicate()

        if output.returncode == 0:
            self.label_error_var.set("")
        else:
        
            stderrlist = stderr.decode().split()
            file = stderrlist[-4].split('\\')[-1]
            message_error = f"{stderrlist[0]} {file} {stderrlist[1]} {stderrlist[2]} ligne : {stderrlist[-3].split(':')[0]}"
            print(stderr.decode())
            self.label_error_var.set(f"{message_error.lower()}")
            # print(message_error)


    def select_method(self , option=1):
        css_file = self.css_path_var.get()
        sass_file = self.sass_path_var.get()
        controle = self.message_error(css_file=css_file , sass_file=sass_file )

        if controle == True:
            if option == 1:
                self.watch_compilation(css_file ,sass_file)
            elif option == 0:
                self.simple_compilation(css_file ,sass_file)
            elif option == 2:
                self.compressor_css_file(css_file ,sass_file)

    def open_css_file(self):
  
        self.app.cssfile = filedialog.askopenfilename(filetypes=(("css files" , "*.css"),("alls" , "*.*"),))
        if self.app.cssfile.split('.')[-1] == "css":
            self.css_path_var.set(self.app.cssfile)
            print(self.css_path_var.get())
        elif  self.app.sassfile == "":
            pass
        else:
            print("[error] You must select the css file")
            messagebox.showinfo("css" , "You must select the css file")

    def open_sass_file(self):

        self.app.sassfile = filedialog.askopenfilename(filetypes=( ("scss files" , "*.scss"),("sass files" , "*.sass") ,("alls" , "*.*"),))

        if(self.app.sassfile.split('.')[-1] == "scss") or  (self.app.sassfile.split('.')[-1] == "sass"):
            self.sass_path_var.set(self.app.sassfile)
            print(self.sass_path_var.get())
        elif  self.app.sassfile == "":
            pass
        else:
            print("[error] You must select the scss or sass file")
            messagebox.showinfo("sass" , "You must select the scss or sass file")


    def message_error(self, sass_file:str , css_file:str) -> bool:

        if css_file == "" and sass_file == "":
            messagebox.showinfo("scss and css" , "You must select the css and scss file")
            return False
            
        elif sass_file == "" and css_file != "":
            messagebox.showinfo("scss" , "You must select the scss file")
            return False

        elif css_file == "" and sass_file != "":
            messagebox.showinfo("css" , "You must select the css file")
            return False
        
        return True