import shelve
import reader

db = shelve.open("items.db")

reader.print_table(db)




