import tkinter as tk
from src.cmd import Cmd

class Gui:

    def __init__(self):

        
        self.app = tk.Tk()
        self.tk = tk
        self.cmd = Cmd(tk , self.app)

        # ========= app =========
        self.app.resizable(0,0)
        self.app.title("Ht-SASS")
        self.app.config(bg="#282828")
        try:
            self.app.iconbitmap("src/assets/logo.ico")
        except Exception:
            pass
        
    def window_position(self,WINDOW_WIDTH = 550,WINDOW_HEIGHT = 200):

        screen_x = int(self.app.winfo_screenwidth())
        screen_y = int(self.app.winfo_screenheight())
        pos_x = (screen_x//2)-(WINDOW_WIDTH//2)
        pos_y = (screen_y//2)-(WINDOW_HEIGHT//2)
        
        self.app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{pos_x}+{pos_y}")

    def widget_position(self):
        top_frame_one = self.tk.Frame(self.app, bg="#039BE5")
        top_frame_two = self.tk.Frame(self.app, bg="#039BE5")
        center_frame = self.tk.Frame(self.app , bg="#282828")
        bottom_frame = self.tk.Frame(self.app , bg="#282828")

        button_open_sass = self.tk.Button(top_frame_one,command=self.cmd.open_sass_file, text="SASS FILE"  , width=10 ,bg="#CD669A" , fg="#FFFFFF" , font=("helvetica",10) , borderwidth=0)
        button_open_css = self.tk.Button(top_frame_two,command=self.cmd.open_css_file , text="CSS FILE" , width=10 ,bg="#CD669A" , fg="#FFFFFF" , font=("helvetica",10) , borderwidth=0)
            
        scss_path_label = self.tk.Label(top_frame_one ,textvariable = self.cmd.sass_path_var, bg="#039BE5", fg="#FFFFFF" , font=("helvetica",11))
        css_path_label  = self.tk.Label(top_frame_two ,textvariable = self.cmd.css_path_var, bg="#039BE5", fg="#FFFFFF" , font=("helvetica",11))
        
        radio_cmd_zero =  self.tk.Radiobutton(center_frame ,variable=self.cmd.option, text="watch" , value =1 ,indicatoron=0 , width=15, borderwidth=0 , fg="#FFFFFF" , bg="#CD669A" ,activebackground="#039BE5" , selectcolor="#0277BD")
        radio_cmd_one  = self.tk.Radiobutton(center_frame ,variable=self.cmd.option, text="compile" , value =0 ,indicatoron=0 , width=18, borderwidth=0 , fg="#FFFFFF" , bg="#CD669A" ,activebackground="#039BE5" , selectcolor="#0277BD")
        radio_cmd_two = self.tk.Radiobutton(center_frame ,variable=self.cmd.option, text="compressed" , value =2 ,indicatoron=0 , width=15, borderwidth=0 , fg="#FFFFFF" , bg="#CD669A" ,activebackground="#039BE5" , selectcolor="#0277BD")
        message_error = self.tk.Label(center_frame,textvariable=self.cmd.label_error_var ,bg="#282828", fg="#FFFFFF" , font=("helvetica",10))
        
        command_button = self.tk.Button(bottom_frame ,command=lambda:self.cmd.select_method(self.cmd.option.get()) ,text="run" , width=50 , borderwidth=0 , bg='#CD669A', fg="#FFFFFF" , activebackground="#0277BD" , )

        top_frame_one.pack(fill="both" , pady=1)
        top_frame_two.pack(fill="both" , pady=1)
        center_frame.pack(pady=30)
        bottom_frame.pack(pady=5)
        #####################
        ## widget position ##
        #####################

        # Top left
        scss_path_label.grid(row=0 , column=1)
        css_path_label.grid(row=1 , column=1)

        # Top right
        button_open_sass.grid(row=0 , column=0)
        button_open_css.grid(row=1 , column=0)

        # center
        radio_cmd_zero.grid(row=0 , column=0)
        radio_cmd_one.grid(row=0 , column=1)
        radio_cmd_two.grid(row=0 , column=2)
        message_error.grid(row=1 , column=0 , columnspan=3)


        # bottom
        command_button.pack()

    def app_menu(self):
        main_menu = self.tk.Menu(self.app)
        # cmd = self.tk.Menu(main_menu ,  tearoff=0)
        # main_menu.add_cascade(label="compiler",menu=cmd)
        # cmd.add_command(label="Open dart file" , command=self.cmd.compiler)
        # cmd.config(fg="#FFFFFF" , bg="#0277BD" ,activebackground="#CD669A" , selectcolor="#CD669A")
        
        # ===================================================================

        # the_help = self.tk.Menu(main_menu ,  tearoff=0)
        # main_menu.add_cascade(label="Help" , menu=the_help)
        # the_help.add_command(label='video',command=self.cmd.video )

        self.app.config(menu=main_menu)


    def run_app(self):
        self.app.mainloop()