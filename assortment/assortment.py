from autof2.assortment import assortment_info
from autof2.readf2 import parse
from autof2.navigation import navigation
import os

def update_assortment(filepath, category,assortment_order_index):
    if navigation.to_assortment_category(category):
        product = parse.parse_assortment_category_section(category)
        a = assortment_info.Assortment(filepath, category)
        a.create_file(assortment_order_index)
        a.read_file()
        for p in product:
            a.add_product(p)
        a.compact_file()
        return a.assortment

def get_categories(filepath):
    files = []
    file_list = os.listdir(filepath)
    for f in file_list:
        if  f[-4:] == '.f2a':
            files.append(f[:-4])
    return files


def get_product_list(filepath,category):
    a = assortment_info.Assortment(filepath,category)
    a.read_file()
    return a.assortment
    
    
    


    
        
        
    