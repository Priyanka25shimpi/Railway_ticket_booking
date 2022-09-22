class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of train is {self.name}")
        print(f"The number of seats available in train are {self.seats}")

    def fareInfo(self):
        print(f"The fare for one person is : Rs.{self.fare}")

    def bookTicket(self):
        b=int(input("press 1 if you want to book a ticket... "))
        if(self.seats>0):
            print(f"your ticket has been booked !, your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry, the train is full. please try tatkal !")

    def cancelTicket(self):
        a=int(input("press 2 to cancel your ticket-> "))
        if a == 2:
            print("your ticket has been canceled")
            self.seats = self.seats + 1

intercity = Train("Intercity Express : 14009", 90, 4)

intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getStatus()