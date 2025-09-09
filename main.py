print("NOTES APP!")
print("1. ADD NOTE")
print("2. VIEW NOTES")
print("3. SEARCH NOTES")

def add_note():
  try:
    title = input("Enter Note Title: ")
    note_text =  input("Enter Text: ")
    
    with open("Notes.txt" , "a") as file:
      file.write(f"Title : {title} \n")
      file.write(f"\n Note : {note_text}\n ")
    print("Note added succesfully!")
  except FileNotFoundError:
    print("Error adding Note. Please Try again!")


def view_notes(): #Displays the titles of the notes
  try:
    with open("Notes.txt" , "r") as file :
      for line in file:
        line = line.strip()
        if line.startswith("Title"):
          title_parts = line.split(":")#Splits the title into 2 parts, the "Title" and the actual title text and returns a list
          print(title_parts[1] , "\n")
  except FileNotFoundError:
    print("Error viewing files!")
def search_notes():
  search_query = input("Enter the title of the note:  ")
  with open("Notes.txt" , "r") as file:
    found = True
    for line in file:
      if search_query.lower() in line.lower():
        print("Found: " , search_query.strip())
        found = True
  if not found:
    print("No matches found1")
def main():
  user_choice = int(input("What do you want to do? "))
  if user_choice == 1:
    add_note()
  elif user_choice == 2:
    view_notes()
  elif user_choice == 3:
    search_notes()
  else:
    print("Enter a valid choice to access your notes")
    
  
if __name__ == "__main__":
  main()
  