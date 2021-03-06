import tkinter as tk
from bs4 import *
from tkinter import *
from PIL import Image, ImageTk
import time


class MainApp:

    def __init__(self):

        root = Tk()
        root.title("NewsReader App")
        root.geometry('1000x1000')
        root.resizable(False,False)
        root.configure(background="white")
        root.wait_visibility(root)
        root.wm_attributes('-alpha',0.85)

        self.frame1=tk.Frame(root,bg="gray19")
        self.frame1.pack(expand='no',fill= 'both')

        greeting_label = tk.Label(self.frame1,
                 text='Welcome to your Personal News Reader',
                 font = ('URW Bookman L',18),
                 fg = 'white', bg='skyblue3').pack(expand='no', fill=tk.X)
        self.watch = tk.Label(self.frame1,
                 text= 'Current Time:{}'.format(time.strftime('%H:%M:%S'))
                ,bg = 'gray19', fg='OliveDrab1')
        self.watch.pack(expand='no', fill=tk.X)
        self.update_time()


        self.fetch_label = tk.Label(self.frame1,
                                    text = "Read Top News, Headlines, Sports,Business, Entertainment  News\n..All in one place!",
                                    font = ('Ubuntu condensed',12),
                                    fg = 'orange',
                                    bg = 'gray19')
        self.fetch_label.pack(expand = 'no', fill = tk.X , pady = 10)
        self.frame2 = tk.Frame(root, bg = "gray19")
        self.frame2.pack(expand = 'yes',fill = 'both')

        self.Categories = tk.Label(self.frame2,
                                   text = 'Categories',
                                   font='Pothana2000 20 bold',
                                   fg = 'white',
                                   bg = 'gray19',
                                   anchor = 'w',
                                   justify = 'left')
        self.Categories.pack(fill = tk.X,padx = 10,pady = 20)


        self.parent_label1 = tk.Label(self.frame2,bg = 'gray19')
        self.parent_label1.pack(fill = tk.X,padx = 10)

       
        photo1 = ImageTk.PhotoImage(Image.open('city.jpeg','r'))
        photo2 = PhotoImage(file = "science.png")
        photo3 = PhotoImage(file = "india.png")
        photo4 = PhotoImage(file = "entertainment.png")
        photo5 = PhotoImage(file = "business.png")
        photo6 = PhotoImage(file = "world.png")
        photo7 = PhotoImage(file = "miscellaneous.png")

        button_configs = { 'height': 200,
                          'width': 200,
                          'bd' : 0,
                          'bg' : 'gray19',
                          'activebackground' : 'orange1',
                          'borderwidth': 0,
                          'highlightthickness': 0}
        
        c1 = tk.Button(self.parent_label1,text='City',image=photo1)
        c1.config(button_configs)
        c1.image = photo1
        
        c2 = tk.Button(self.parent_label1,text='yes',image = photo2)
        c2.config(button_configs)
        c2.image = photo2
        
        c3 = tk.Button(self.parent_label1,text='yes',image = photo3)
        c3.config(button_configs)
        c3.image = photo3
        
        c4 = tk.Button(self.parent_label1,text='yes',image = photo4)
        c4.config(button_configs)
        c4.image = photo4
        
        c5 = tk.Button(self.parent_label1,text='yes',image = photo5)
        c5.config(button_configs)
        c5.image = photo5

        c6 = tk.Button(self.parent_label1,text='yes',image = photo6)
        c6.config(button_configs)
        c6.image = photo6

        c7 = tk.Button(self.parent_label1,text='yes',image = photo7)
        c7.config(button_configs)
        c7.image = photo7


        c1.grid(row=0,column=0,padx = 20,pady = 20)
        c2.grid(row=0,column=1,padx = 20,pady = 20)
        c3.grid(row=0,column=2,padx = 20,pady = 20)
        c4.grid(row=0,column=3,padx = 20,pady = 20)
        c5.grid(row=1,column=0,padx = 20,pady = 20)
        c6.grid(row=1,column=1,padx = 20,pady = 20)
        c7.grid(row=1,column=2,padx = 20,pady = 20)

        root.mainloop()
     
    
         
        

        


    def update_time(self):
        
        self.watch.configure(text='Current Time:{}'.format(time.strftime('%H:%M:%S')))
        self.frame1.after(200, self.update_time)
        
        

if __name__ == "__main__":

    obj = MainApp()
    
        
