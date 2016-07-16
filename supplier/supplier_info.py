import os

class Supplier:
    extention = '.f2s'
    identifier = 'Assortment Codes'
    product_order = ['f2_code','price','packing','product_name','grade','colour']

    def __init__(self, filepath,supplier_code):
        if not os.path.isdir(filepath):
            os.makedirs(filepath)
            
        self.filepath = filepath
        if  filepath[-1] not in ('\\','/'):
##            self.filepath.replace('/','\\')
            self.filepath += '\\'
        self.filename = self.filepath + supplier_code + Supplier.extention
        self.supplier_code = supplier_code
##        self.read_file()

    def read_file(self):
        with open(self.filename,'r') as file:
            self.supplier_code = file.readline()
            self.supplier_name = file.readline()
            self.contact_firstname = file.readline()
            self.contact_lastname = file.readline()
            self.contact_email = file.readline()
            self.assortment = []
            line = file.readline().strip() 
            while True:
                if line == Supplier.identifier:
                    break
                else:
                    line = file.readline().strip()
            line = file.readline().strip()
            while line:
                product = {}
                index = 0
                
                for l in line.split('\t'):
                    product[Supplier.product_order[index]] = l.strip()
                    index += 1
                if product not in self.assortment:
                    self.assortment.append(product)
                line = file.readline().strip()
    def create_file(self,supplier_name,contact_firstname,contact_lastname,contact_email):
        if not os.path.isfile(self.filename):
            with open(self.filename,'w') as file:
                file.write(self.supplier_code + '\n')
                file.write(supplier_name + '\n')
                file.write(contact_firstname + '\n')
                file.write(contact_lastname + '\n')
                file.write(contact_email + '\n')
                file.write(Supplier.identifier + '\n')
                    

    def add_product(self,f2_code,price,packing,product_name,grade,colour):
        if os.path.isfile(self.filename):
            with open(self.filename,'a') as file:
                for c in (f2_code,price,packing,product_name,grade,colour):
                    file.write(c)
                    file.write('\t')
            
                file.write('\n')

    def compact_file(self):
        if os.path.isfile(self.filename):
            self.read_file()
            os.remove(self.filename)
            self.create_file(self.supplier_name,self.contact_firstname,self.contact_lastname,self.contact_email)
            for a in self.assortment:
                self.add_product(a['f2_code'],a['price'],a['packing'],a['product_name'],a['grade'],a['colour'])
            
        
def list_suppliers(filepath):
    suppliers = []
    for s in os.listdir(filepath):
        if s[-4:] == '.f2s':
            suppliers.append(s[:-4])
    return suppliers
        
    
        
        
    
                
            
                
  
            
##filepath = 'C:\\Python32\\Lib\\autof2\\supplier\\'            
## 
##A = Supplier(filepath,'CATEST2')
##A.create_file('Antoine Inc','Antoine','Wood','antoinewood@gmail.com')
##A.add_product('1afafdas','0.50','500','Stuff','50','Red')
##A.add_product('2afafdas','0.50','500','Stuff','50','Red')
##A.add_product('3afafdas','0.50','500','Stuff','50','Red')
##A.add_product('3afafdas','0.50','500','Stuff','50','Red')
##A.add_product('4afafdas','0.50','500','Stuff','50','Red')
##A.add_product('5afafdas','0.50','500','Stuff','50','Red')
##A.add_product('6afafdas','0.50','500','Stuff','50','Red')
##
##A.read_file()
