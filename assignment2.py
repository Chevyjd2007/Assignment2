import socket

class assignment2:
    # Task 1
    def __init__ (self, year: int) -> None:
        self.year = year

    #Task 2
    def tellAge (self, currentYear: int) -> None:
        age = int(currentYear) - int(self.year)
        print("Your age is " + str(age))

    #Task 3
    def listAnniversaries(self) -> list[int]: 
        anniversaries = []
        currentYear : int = 2023
        difference : int = currentYear - int(self.year)
        cursor : int = difference / 10
    
        i = 1
        while i <= cursor:
            anniversaries.append(i * 10)
            i += 1

        return anniversaries

    #Task 4
    def modifyYear(self, n: int) -> str:
        modifiedYear : str = ""
        #Part 1 of task 4
        for i in range(n):
            modifiedYear = str(self.year)[0: 2] + modifiedYear

        #Part 2 of task 4
        multipliedYear : str = str(self.year * n)
        odd_chars = multipliedYear[::2]
        
        return modifiedYear + odd_chars
    
    #Task 5
    @staticmethod
    def checkGoodString(String : str) -> bool:
        if len(string) < 9:
            return False
        
        # Check if the string starts with a lowercase letter
        if not string[0].islower():
            return False
        
        # Count numbers in the string
        numCount = sum(1 for char in string if char.isdigit())

        # Check if the string contains exactly one number
        if numCount != 1:
            return False
        
        return True
    
    #Task 5
    @staticmethod
    def connectTcp(host: str, port: int) -> bool:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            s.connect((host, port))
            
            s.close()
            
            return True
        
        except Exception as e:
            return False



#Check for task 6
#retval = Assignment2.connectTcp("www.google.com", 80)
#if retval:
#    print("Connection established correctly")
#else:
#    print("Some error")





#Check for task # 4
#print(Assignment2(1782).modifyYear(3))

#Check for task # 3
#a = Assignment2(2000)
#ret = a.listAnniversaries()
#print(ret)

#Check for task # 2
#year = input("What is your birth year: ")
#currentYear = input("What is the current year: ")

#Assignment2(year).tellAge(currentYear)
