import tkinter as tk
from bs4 import *
from tkinter import *
import urllib
from PIL import Image, ImageTk
import io
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

        frame1=tk.Frame(root,bg="gray19")
        frame1.pack(expand='yes',fill='both')


        time_str = time.strftime('%H:%M:%S')

        
        greeting_label = tk.Label(frame1,
                 text='Welcome to your Personal News Reader',
                 font = ('URW Bookman L',18),
                 fg = 'white', bg='skyblue3').pack(expand='no', fill=tk.X)
        tk.Label(frame1,
                 text='Current Time:{}'.format(time_str),
                 
                 bg = 'gray19', fg='OliveDrab1').pack(expand='no', fill=tk.X)


if __name__ == "__main__":

    obj = MainApp()
    
        
