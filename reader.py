#definitions
TABLE_HEIGHT = 40
CELL_HEIGHT = TABLE_HEIGHT/4


def cell_text_maker(string):
    string = str(string)
    return '|'+string+' '*(int)(CELL_HEIGHT-2-len(string))+'|'

def print_table(db):
    print('-'*TABLE_HEIGHT)
    print(cell_text_maker("ID")+cell_text_maker("Name")+cell_text_maker("Price")+cell_text_maker("Count"))
    print('-'*TABLE_HEIGHT)
    for key, item in db.items():
        print(cell_text_maker(key)+cell_text_maker(item['name'])+cell_text_maker(item['price'])+cell_text_maker(item['count']))
    print('-' * TABLE_HEIGHT)

def get_item(db,item_key):
    if item_key in db.items():
        return db[item_key]
    else:
        return 0





