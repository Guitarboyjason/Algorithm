class SoccerPlayer(object):
    def __init__(self,name : str,position:str,back_number:int):
        self.__name = name
        self.__position = position
        self.__back_number = back_number
    
    def __str__(self):
        return "Hello, My name is {}, my position is {} and my backnumber is {}".format(self.__name,self.__position,self.__back_number)
    def change_name(self,new_name:str):
        print("선수의 이름을 초기화 합니다.")
        self.__name = new_name
        
    
player1 = SoccerPlayer("jason","MF",17)
print(player1)
player1.change_name("park")
print(player1)