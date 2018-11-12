from sqlalchemy.orm import sessionmaker
from autof2.database.model import engine, F2Category, F2Assortment


def get_session():
    session = sessionmaker(bind=engine)
    return session()


def get_f2_code(category, product, grade, colour,packing):
    session = get_session()
    category = session.query(F2Category).filter_by(f2_category_description=category).first()
    return session.query(F2Assortment).filter_by(f2_name=product,
                                                 f2_category=category,
                                                 packing=packing,
                                                 f2_grade=grade,
                                                 f2_colour_code_id=colour).first()
## To test
#category = "Ecuador Roses"
#product = "Freedom"
#grade = "50"
#colour = "RD"
#packing = "25"
#data = get_f2_code(category, product, grade, colour,packing)
#print(data)