from autof2.interface.send_data import SendData
from autof2.navigation import navigation
from autof2.readf2 import parse
import time

def purchase_list(purchases, date):
    send = SendData()
    navigation.to_input_purchase(date)
    time.sleep(.5)
    if parse.need_input():
        send.send('{insert}')
    for p in purchases:
        send.f2_purchase(p['f2_code'],p['price'],p['quantity'],p['packing'],p['supplier'])
##    send.send('{f12}')
##    send.send('^a')
    

        
def virtual_purchase_list(purchases, date):
    send = SendData()
    navigation.to_virtual_purchase(date)
    time.sleep(.5)
    if parse.need_input():
        send.send('{insert}')
    for p in purchases:
        send.f2_purchase(p['f2_code'],p['price'],p['quantity'],p['packing'],p['supplier'])
    send.send('{F12}')
    time.sleep(3)
    set_availability(date,6)
    

def set_availability(date, days):
    send = SendData()
    navigation.to_virtual_purchase(date)
    time.sleep(.5)
    if parse.need_input():
        send.send('^a')
        send.send('{F11}')
        send.send('{enter}')
        send.send(date)
        send.send('{enter}')
        send.send(date)
        send.send('{home}')
        send.send('{+ %i}' % days)
        send.send('{F11 3}')
        send.send('y')
        
    
        
        
    
    
    
##virtual_purchase_list(1,'22/07/16')    
    

