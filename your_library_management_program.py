Your_library = []
My_Book = input("Enter the name of a book you own: ")
another_book = input("Enter the name of another book you own (or press 'Enter' to skip) ")
Your_library.append(My_Book)
Your_library.append(another_book)
if another_book == "":
  Your_library.remove("")
  print("\nYour_library: ",Your_library)
else:
  print("\nYour_library: ",Your_library) 
You_Wishlist = []
future_book = input("\nEnter the name of a book you wish to have in the future: ")
another_future_book = input("Enter the name of another book you wish to have (or press 'Enter'to skip) ")
You_Wishlist.append(future_book)
You_Wishlist.append(another_future_book)
if another_future_book == "":
  You_Wishlist.remove("")
  print("\nYou Wishlist: ",You_Wishlist)
else:
  print("\nYou Wishlist: ",You_Wishlist)
wish = input("\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip) ")
if wish in You_Wishlist:
  Your_library.append(wish)
  You_Wishlist.remove(wish)
  print("\nUpdate_library: ", Your_library)
  print("Update_Wishlist: ",You_Wishlist)
else:
  print("\nUpdate_library: ", Your_library)
  print("Update_Wishlist: ",You_Wishlist)
print()  
donnate_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter'to skip) ")
if donnate_book in Your_library:
  Your_library.remove(donnate_book)
  print("\nFinal_Library_after_Donations: ", Your_library)
else:
   print("\nFinal_Library_after_Donations:", Your_library)