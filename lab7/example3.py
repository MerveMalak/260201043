books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
book_dict = {}
for book in books:
  book_dict[book] = (len(book),len(set(book)),(len(book)+len(set(book)))/2)
for current_key,current_value in book_dict.items():
  print(current_key," -> ",current_value)
