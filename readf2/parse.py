import time
from autof2.interface.send_data import SendData
from autof2.interface import window
##from autof2.navigation import navigation

class Order:
    def __init__(self,category, name,grade,colour, client,quantity, supplier, comment=''):
        self.supplier = supplier.strip()
        self.category = category.strip()
        self.name = name.strip()
        self.colour = colour.strip()
        self.grade = grade.strip()
        self.client = client.strip().strip('!')
        self.quantity = int(quantity.strip())
        self.comment = comment.strip()
        self.standing = client[0].strip() == '!'
    def __str__(self):
        return "%s %s %s %s %s %s " % (self.category,self.name, self.grade,self.colour,
                                        self.client,self.quantity)

    def __eq__(self,other):
        return (self.category,self.name,self.colour,self.grade) == (other.category,other.name,other.colour,other.grade)
    def tupple(self):
        return (self.category,self.name, self.grade,self.colour,
                                        self.client,self.quantity)
    
        

#distribution list
def distribution_list_supplier(screen):
    ''' (list of str) -> str
    '''
    for i in range(20):
        try:
            line = screen[1]
            target = 'Inkoop advies avc'
            line = line[line.index(target) + len(target):].strip()
            line = line[:line.index(' ')].strip()
            break
        except:
            screen = process_scene(window.get_window())
            time.sleep(.1)
    return line


# main menu
def identify_screen(screen, target, line_num=2):
    for w in range(20):
        try:
            line = screen[line_num]
            #print(line)
            if target in screen[line_num]:
                return True
            break
        except:
            screen = process_scene(window.get_window())
            time.sleep(.1)
    return False
    

# helper functions
def process_scene(uscreen):
    for j in range(10):
        try:    
            return uscreen.split('\r\n')
        except:
            uscreen = helper.get_window()
    return None

def distribution_list_product(screen):
    supplier = distribution_list_supplier(screen)
    orders = []
    category = None
    grade = None
    
    for line in screen:
        #print(len(line))
        if (line[0:4] == '    ' and  line[4] != ' ') or (line[0:3] == '   ' and line[4] != ' '):
            category = line.strip()

        if category:
            if line[0] not in (' ','═','╚'):
                name = line[0:30].strip()
                grade = line[31:35].strip()
                colour = line[35:40].strip()
              
                if len(line) >= 95:
                    quantity = line[80:85].strip()
                    client = line[85:95].strip()
                    if client != '':
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
                if len(line) >= 103:
                    quantity = line[95:103].strip()
                    client = line[103:113].strip()
                    if client != '' :
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
                if len(line) >= 131:
                    quantity = line[113:121].strip()
                    client = line[121:131].strip()
                    if client != '':
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
    
            elif line[1] == '>':
                client = line[7:15].strip()
                for o in orders:
                    if (o.client, o.category, o.name, o.grade, o.client, o.quantity, o.supplier)== (client, category, name.strip('!'),grade,client,quantity, supplier):
                        o.comment += line[15:].strip()

            elif line[:67].strip().isdigit():
                if len(line) >= 80:
                    quantity = line[:67].strip()
                    client = line[68:80].strip()
                    if client != '':
                        print(category, name,grade,client,quantity,supplier)
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
                    
                if len(line) >= 95:
                    quantity = line[80:85].strip()
                    client = line[85:95].strip()
                    if client != '':
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
                if len(line) >= 103:
                    quantity = line[95:103].strip()
                    client = line[103:113].strip()
                    if client != '':
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
                if len(line) >= 131:
                    quantity = line[113:121].strip()
                    client = line[121:131].strip()
                    if client != '':
                        orders.append(Order(category, name,grade,colour,client,quantity,supplier))
    return orders

def order_categories(screen):
    categories = []
    line_num = 6
    while line_num < 30 and "═" not in screen[line_num]:
        if screen[line_num][1] == ' ':
            start = 1
        else:
            start = 0
            
        line = screen[line_num][start:]
        while True:
            try:
                start = line.index('║') +1
                line = line[start:]
                end = line.index('║')

                c = line[:end]
                if c.isspace() or c.strip() == '':
                    break
               
                cat_num = c[:3].strip()
                cat_name = c[3:].strip()
                categories.append((cat_num,cat_name))
##                print(cat_num + " , " + cat_name)
                line = line[end:]
            except:
                break
        line_num += 1

    categories.sort()
    return categories

def parse_order_category(cat_name):
    items = []
    send = SendData() 
    while True:
        screen = process_scene(helper.get_window())
        to_process = screen[6:]
        for line in to_process:
            if '═' in line:
                break
            line = line[4:]
            l = line.split('║')
            if l[0].isspace():
                break
            else:
                quantity = l[7][:l[7].index('x')]
                price = l[9].replace(',','.').strip('■').strip('▲').strip('█').strip('▼')
                print(price)
                items.append((l[0].strip(),l[1].strip(),l[2].strip(),quantity.strip(),price.strip()))

            

        send.send('{PGDN}')
        time.sleep(0.1)
        new_screen = process_scene(helper.get_window())
        if new_screen == screen:
            time.sleep(0.1)
            new_screen = process_scene(helper.get_window())
            if new_screen == screen:
                break
    return {cat_name:items}

def parse_virtual_order_category(cat_name):
    items = []
    send = SendData()
    time.sleep(0.2)
    while True:
        time.sleep(0.1)
        screen = process_scene(helper.get_window())
        to_process = screen[6:]
        for line in to_process:
            if '═' in line:
                break
            line = line[4:]
            l = line.split('║')
            
            if l[0].isspace():
                print(cat_name,l)    
                break
            else:
                quantity = l[7][:l[7].index('x')]
                packing = l[7][l[7].index('x') + 1:].strip()
##                print(packing) 
                price = l[9].replace(',','.').strip('■').strip('▲').strip('█').strip('▼')
##                print(price)
                items.append((l[0].strip(),l[1].strip(),l[2].strip(),quantity.strip(),price.strip(),packing))

            
        time.sleep(0.2)
        send.send('{PGDN}')
        time.sleep(0.2)
        print("next")
        new_screen = process_scene(helper.get_window())
        if new_screen == screen:
            time.sleep(0.5)
            new_screen = process_scene(helper.get_window())
            if new_screen == screen:
                break
    
    
    return {cat_name:items}

def parse_assortment_category_section(cat_name, max_pages = 30):
    send = SendData()
    send.send('{home}{home}')
    screen = process_scene(window.get_window())
    old_screen = screen
    items = []

    for count in range(max_pages):
        to_process = screen[6:]
        seperated = []
        good_list = []

        for line in to_process:
            seperated.append(line.split('║'))
        for line in seperated:
            if '═' in line[0]:
                break
            if line[1].strip() != '':
                good_list.append(line)
##        for line in good_list[2:]:
##            send.send('{DOWN}')
            
        for line in good_list:
            send.send(line[1])
            time.sleep(.15)
            screen = process_scene(window.get_window())
            code = screen[-2][69:82].strip()
            name = line[2][:-4].strip()
            name = name[len(cat_name):].strip()
            colour = line[3].strip()
            length = line[4].strip()
            quality = line[5].strip()
            packing = int(line[6].strip())
            new_item = (code,cat_name,name,colour, length, quality, packing)
            if new_item in items:
                return items

            items.append(new_item)
                
            print((code,cat_name,name,colour,length,quality,packing))
        send.send('{PGDN}')
        send.send('{home}')
        time.sleep(.3)
        new_screen = process_scene(window.get_window())
        screen = new_screen
        if new_screen[6:] ==  old_screen[6:]:
            break
        old_screen = new_screen

    return items

def parse_input_purchase(screen):
    send = SendData()
    screen = screen[6:]
    new_screen = None
    items = {}
    while True:
        
        for line in screen:
            if '══' in line:
                break
            line = line.split('║')
    ##        print(line)
            lot = line[1].strip()
            price = line[6].strip().replace(',','.')
            items[lot] = price

        send.send('{PGDN}')
        time.sleep(0.5)
        new_screen = process_scene(helper.get_window())[6:]
        if screen == new_screen:
            break
        screen = new_screen
    return items
    

        
##        i = 1
##        i = screen[line_num][i:].index('║')
##
##        next_line = screen[line_num][i + 5:].index('║')
##
##        cat_num = screen[line_num][i + 2:i + 5]
##
##        cat_name = screen[line_num][i + 5 : i + 16]
##        print(cat_name)
##        

    
def price(items,from_date,to_date,margin):
    
    navigation.to_virtual_stock(from_date,to_date)
    screen = process_scene(helper.get_window())
    send = SendData()
    
    for i in items:
        if items[i]:
            print(i, items[i],'... ',end='')
            price = '{0:.2f}'.format(float(items[i])*margin)
            print(price)
            commands = ('{F7}',i,'{right}','{enter}','{F2}','{enter}')
            for cmd in commands:
                send.send(cmd)

            for n in range(8):
                send.send('{F10}')
                send.send(price)
                send.send('{enter}')
            send.send('{f11}')
            send.send('{f12}')
        
def need_input():
    screen = process_scene(window.get_window())
    index = 0
    for i in screen:
        index += 1
    if 'Visible' in screen[24] and 'Buyer' in screen[29]:
        return False
    return True

  #  def parse_assortment_report(filename = "assortment_report.html"):
        
##from database import *        
        
        
##if __name__ == "__main__":
##
####    for date, margin in (('01/02/16',1.5),('31/01/16',1.6),('30/01/16',1.45),('02/02/16',1.6)):
##    for date, margin in (('02/02/16',1.6),):
##        send = SendData()
##        screen = process_scene(helper.get_window())
##        navigation.to_virtual_purchase(date)
##        items = parse_input_purchase(screen)
##        price(items,date,date,margin)
##
    

        
##    cat_name = 'Ecuador Roses'
##    a = parse_assortment_category_section(cat_name)
    #c = order_categories(screen)
##    print(parse_order_category('cat_name'))
    
##    helper.run_purchase_list("011115", "071115","CASIFL")
##    time.sleep(1)
##    screen = process_scene(helper.get_window())  
##    o = distribution_list_product(screen)
##    for i in o:
##        print(i.client, i.name, i.quantity, i.comment )

##time.sleep(1)

##screen = process_scene(helper.get_window())#
##
##send = SendData()
##items = {}
##
##
##items = parse_input_purchase(helper.get_window())
##price(items,'010516','150516',1.5)


##for date, margin in (('03/05/16',1.6),):
##        send = SendData()
##        screen = process_scene(helper.get_window())
##        navigation.to_virtual_purchase(date)
##        items = parse_input_purchase(screen)
##        price(items,date,date,margin)

        
a = parse_assortment_category_section('Alstro ON')
