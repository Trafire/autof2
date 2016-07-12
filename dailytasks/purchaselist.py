from autof2.navigation import navigation
from autof2.interface import window
from autof2.interface.send_data import SendData
from autof2.readf2 import parse
from autof2.email import email

import time

def get_purchase_list_report(from_date,to_date,supplier ):
    send = SendData()
    run_purchase_list(from_date, to_date,supplier)
    screen = parse.process_scene(window.get_window())
    o = parse.distribution_list_product(screen)
    i = 0
    while '< More >' in screen[-1] and i < 10:
        send.send('{enter}')
        time.sleep(0.8)
        screen = parse.process_scene(window.get_window())
        o.extend(parse.distribution_list_product(screen))
        i+=1
    return o

def run_purchase_list(from_date, to_date,supplier, new = True):
    if new:
        navigation.to_purchase_list()
    window.drag_window()
    send = SendData()
    send.send(from_date)
    send.send('{enter}')
    send.send(to_date)
    send.send('{enter}')
    send.send('{DOWN}')
    send.send(supplier)
    send.send('{enter}')
    send.send('{F11}')
    send.send('n')
    send.send('screen')
    send.send('{enter}')

    for i in range(15):
        screen = parse.process_scene(window.get_window())
        if parse.identify_screen(screen,'Inkoop advies avc',1):
            return window.get_window()
        time.sleep(0.1)

def email_list(recipient, products):
    subject = "Purchase list for %s" % products[0].supplier
    title = products[0].supplier
    headers = ('category', 'client', 'grade','colour', 'comment', 'name', 'quantity')
    rows = []
    for p in products:
        rows.append(p.tupple())
        
    email.email_chart(title,headers,rows, subject, recipient,True)
    

a = get_purchase_list_report('11/07/16','19/07/16','CAROSA')
email_list("antoinewood@gmail.com",a)
