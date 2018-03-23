#import win32api
import win32com.client
import time
from tkinter import messagebox


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SendData(metaclass=Singleton):
    def __init__(self, window_name = "Connect 2000 (© Uniware Computer Systems BV) (Session 1 : 192.168.180.1)", shell = win32com.client.Dispatch("WScript.Shell")):
        self.window_name = window_name
##        self.window_name = 'notepad'
        self.shell = shell
    def activate_window(self):
        if self.shell.AppActivate(self.window_name):
            self.shell.AppActivate(self.window_name)
        else:
            #messagebox.showinfo(message= self.window_name + " is not open, please prepare window to accept input.\nOutput will instead print to Notepad")
            if not self.shell.AppActivate("Notepad"):
                self.shell.Run("Notepad")
                self.shell.AppActivate("Notepad")
            time.sleep(.05)
             
        time.sleep(.1)
 
    def send(self, data):
         
        self.shell.SendKeys(data)
        time.sleep(.01)

    def send_exact(self, data):
        data = data.replace('+', '{+}')
        data = data.replace('%', '{%}')
        data = data.replace('^', '{^}')
        data = data.replace('[', '{[}')
        data = data.replace(']', '{]}')
        data = data.replace('~', '{~}')
        data = data.replace('(', '{(}')
        data = data.replace(')', '{)}')
        self.send(data)
 
    def f2_purchase(self, assortment_code, price, number, packing, supplier):
        assortment_code = assortment_code.replace('+','{+}')
        assortment_code = assortment_code.replace('%','{%}')
        assortment_code = assortment_code.replace('^','{^}')
        assortment_code = assortment_code.replace('[','{[}')
        assortment_code = assortment_code.replace(']','{]}')
        assortment_code = assortment_code.replace('~','{~}')
        assortment_code = assortment_code.replace('(','{(}')
        assortment_code = assortment_code.replace(')','{)}')
 
        cmd_order = [assortment_code,'{enter}','{down}',price,'{enter}',' ','{enter}',number,'{enter}',packing,'{enter}',supplier,'{F11}','{enter}']
        for cmd in cmd_order:
            self.send(cmd)
            #time.sleep(.01)
##        print (assortment_code)
 
    def f12(self):
        self.send('{F12}')

    def enter_csv(self,filename):
        import csv
        self.activate_window()
        with open(filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            for row in spamreader:
                if row[0] != '':
                    self.f2_purchase(row[0], row[1], row[2], row[3], row[4])


#### testing code####################
##purchases = SendData()
##
##purchases.activate_window()
##for i in range(10):
##    purchases.f2_purchase('RSR7','1.00','1','50','CASIFL')
##
##purchases.f12()
## dutch_window_name = 'Connect 2000 (© Uniware Computer Systems BV) (Session 1 : connect.metz.com)'
