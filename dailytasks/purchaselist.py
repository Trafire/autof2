from autof2.navigation import navigation
from autof2.interface import window
from autof2.interface.send_data import SendData
from autof2.readf2 import parse
from autof2.email import email
from autof2.helper import dates
import time

def get_purchase_list_report(from_date,to_date,supplier ):
    send = SendData()
    run_purchase_list(from_date, to_date,supplier)
    time.sleep(1)
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


def email_list_internal(start_date, end_date, supplier_code, day=dates.todays_date()):
    supplier_code = supplier_code.upper()
    supplier_file_name = "C:\\Users\\Antoine\\Desktop\\Tools\\frontend\\suppliers\\supplier_info.csv"
    products = get_purchase_list_report(start_date, end_date,supplier_code)
    suppliers = {}
    with open(supplier_file_name, 'r') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            line = line.strip().split(',')
            supplier = {}
            for i in range(1,len(headers)):
                supplier[headers[i]] = line[i]
            suppliers[line[0]] = supplier
    try:
        supplier = suppliers[supplier_code]
    except:
        supplier = suppliers["METZ"]

    
    subject = "FleuraMetz order for %s - %s" % (supplier['supplier_name'], day)
    recipient = supplier['email']

    intro_text = """ Hello {0},
    Can I get the following for {1} please:
    Thanks,
    Antoine
    
    """.format(supplier['sales_name'], day)
    print(intro_text)
                                      
                
    title = "Order for %s" % supplier['supplier_name'] 
    headers = ('category', 'Product', 'grade','colour', 'Client', 'quantity', 'Comment')
    rows = []
    for p in products:
        print(p)
        rows.append(p.tupple())
    print(rows)    
    email.email_chart(title,headers,rows,subject, recipient,True)


def email_list_supplier(start_date, end_date, supplier_code, day=dates.todays_date()):
    supplier_code = supplier_code.upper()
    supplier_file_name = "C:\\Users\\Antoine\\Desktop\\Tools\\frontend\\suppliers\\supplier_info.csv"
    products = get_purchase_list_report(start_date, end_date,supplier_code)
    suppliers = {}
    with open(supplier_file_name, 'r') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            line = line.strip().split(',')
            supplier = {}
            for i in range(1,len(headers)):
                supplier[headers[i]] = line[i]
            suppliers[line[0]] = supplier
    try:
        supplier = suppliers[supplier_code]
    except:
        supplier = suppliers["METZ"]

    
    subject = "FleuraMetz order for %s - %s" % (supplier['supplier_name'], day)
    recipient = supplier['email']

    intro_text = """ Hello {0},
    Can I get the following for {1} please:
    Thanks,
    Antoine
    
    """.format(supplier['sales_name'], day)
    print(intro_text)
                                      
                
    title = "Order for %s" % supplier['supplier_name'] 
    headers = ('category', 'Product', 'grade','colour', 'quantity', 'Comment')
    rows = []
    product = {}
    for p in products:
        p = p.tupple()
        if p[:-2] not in product:
            product[p[:-2]] = p[-1]
        else:
            product[p[:-2]] = product[p[:-2]] + p[-1]

    for p in product:
        rows.append(p + (product[p],))
   
    
    rows.sort()
    email.email_chart(title,headers,rows,subject, recipient,True)
    

##ask = get_purchase_list_report('19/07/16','26/08/16','CADens')
##email_list_internal('21/08/16','27/08/16','CAPINN','20/08/16') #"CAROSA", ask, "C:\\Users\\Antoine\\Desktop\\Tools\\frontend\\suppliers\\supplier_info.csv")
##email_list_internal('20/08/16','27/08/16','CADENS','20/08/16')
