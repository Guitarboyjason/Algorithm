class Note():
    def __init__(self,letters:str=""):
        self.Content = letters
    
    def write(self,letters:str):
        self.Content = letters
    
    def remove(self):
        self.Content = ""
        
    def __str__(self):
        return self.Content
    
    def __add__(self,other):
        return self.Content + other.Content
    
class Notebook():
    def __init__(self):
        self.page = []

    def insert(self,note:Note):
        if len(self.page) < 300:
            self.page.append(note)
            print("insert completed")
        else:
            print("sorry, book is full")


note = Note()
print(note)
note = Note("Hello")
print(note)

note1 = Note()
note2 = Note()
note1.write("Hello")
note2.write("World!")
print(note1+note2)