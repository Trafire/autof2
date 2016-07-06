from autof2.readf2 import parse
from autof2.interface import window
from autof2.interface.send_data import SendData

import time



# change menues
def to_main(tries = 25):
    send = SendData()
    screen = None
    for ik in range(tries):
        print(ik)
        for j in range(10):
            try:
                screen = parse.process_scene(window.get_window())
                break
            except:
                time.sleep(0.1)

            time.sleep(0.1)
                
        if parse.identify_screen(screen,'Main Menu'):
            send.send('{UP}')
            return True
        send.send('{F12}')
    return False

def traverse(menu_list):
    send = SendData()
    for m in menu_list:
        print(m)
        send.send(m)
        send.send('{ENTER}')

def to_purchase_list():
    if to_main():
        time.sleep(0.2)
        menus = ('Purchase','Purchaselist','Advanced')
        traverse(menus)
        time.sleep(.2)
        screen = parse.process_scene(window.get_window())
        
        if parse.identify_screen(screen,'Advanced'):
            send = SendData()
            send.send('{UP}')
            send.send('{ENTER}')
            time.sleep(.1)
            screen = parse.process_scene(window.get_window())
            if parse.identify_screen(screen,'√',8):
                print("check")
                send.send('{UP}')
                send.send(' ')
                send.send('{ENTER}')
        else:
            return False

        time.sleep(.1)
        screen = parse.process_scene(window.get_window())
        return parse.identify_screen(screen,'Advanced') and  not parse.identify_screen(screen,'√',8)

        
def to_order_order(date='',client='',plist = '03'):
    send = SendData()
    if to_main():
        time.sleep(0.02)
        menus = ('order','order')
        traverse(menus)
        time.sleep(.5)
        screen = parse.process_scene(window.get_window())
        if client and date:
            if parse.identify_screen(screen,'Order'):
                send.send(client)
                send.send('{HOME}')
                send.send('{LEFT}')
                send.send(date)
                send.send('{F11}')
                send.send('{ENTER}')
                send.send('F')
                send.send('{ENTER}')
                send.send(plist)
                time.sleep(0.2)

    else:   
        return False

def to_order_category(cat_num, cat_name):
    send = SendData()
    send.activate_window()
    send.send(cat_num)
    
    

    for i in range(5):
        screen = parse.process_scene(window.get_window())
        if parse.identify_screen(screen, cat_name, 4):
            return True
        time.sleep(.1)
        screen = parse.process_scene(window.get_window())
    return False        

def to_virtual_stock(from_date,to_date):
    send = SendData()
    if to_main():
        time.sleep(0.02)
        menus = ('stock','Stock virtual products','Edit stock virtual')
        traverse(menus)
        time.sleep(.5)
##            screen = parse.process_scene(window.get__window())
        send.send(from_date)
        send.send('{enter}')
        send.send(to_date)
        send.send('{f11}')
        send.send('{enter}')
        send.send('{down}')
        send.send('{enter}')
def to_virtual_purchase(date):
    send = SendData()
    if to_main():
        time.sleep(0.04)
        menus = ('Purchase','Default','Insert virtual')
        traverse(menus)
        time.sleep(.5)
        send.send('{enter}')
        send.send(date)
        send.send('{enter}')
##        send.send('{enter}')
##        send.send('Insert virtual purchases')
##        send.send('{enter}')
##        time.sleep(.5)
##        send.send(date)
##        send.send('{enter}')

def to_menu(command_order):
    send = SendData()
    if to_main():
        time.sleep(0.02)
        traverse(command_order)
        time.sleep(0.02)
    
def to_distribution_report(date,supplier):
    send = SendData()
    command_order = ('Purchase','Purchase details (suppl)','Without distribution')
    to_menu(command_order)
    time.sleep(0.5)
    send.send('{enter}')
    time.sleep(0.5)
    send.send(date)
    send.send('{enter}')
    time.sleep(0.5)
    send.send(date)
    send.send('{enter}')
    send.send(supplier)
    send.send('{enter}')
    send.send('laserprinter')
    send.send('{enter}')
    

##if __name__ == "__main__":
##    to_virtual_purchase('05/05/16')
##    send = SendData()
##    send.send('{end}')
##    send.send('{down}')
##    send.send('{end}')
####    time.sleep(1)
##    send.send('{insert}')
##    import vday_roses
##    send.send('{f12}')
##
##    
##'''
##to_purchase_list()
##helper.run_purchase_list("011115", "071115","CASIFL")
##for i in range(15):
##    screen = parse.process_scene(window.get_window())
##    if parse.identify_screen(screen,'Inkoop advies avc',1):
##        print(window.get_window())
##        break
####    time.sleep(0.1)
##'''
##
