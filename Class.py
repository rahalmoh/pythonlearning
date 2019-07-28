

class Car:
    def GetOwner(self):
        print("Owner is", self._Name)

    def SetOwner(self, Name):
        self._Name=Name

def main():

    polo=Car() # creating instanse
    polo.SetOwner("Muhammad Rahal")
    polo.GetOwner()

    golf=Car() 
    golf.SetOwner("ameer rahal")
    golf.GetOwner()

#print("github nesayon....fdfsdfs...")


main()


