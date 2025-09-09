  user_choice = int(input("What do you want to do? "))
    if user_choice == 1:
      add_note()
    elif user_choice == 2:
      view_notes()
    elif user_choice == 3:
      search_notes()
    elif user_choice == 4:
      delete_note()   
    else:
      print("Enter a valid choice to access your notes")
    