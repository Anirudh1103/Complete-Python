# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

class Train:
    trains = [
    ["Shatabdi Express","12001", "New Delhi", "Bhubaneswar", 1200, 100],
    ["Rajdhani Express", "12301", "New Delhi", "Howrah", 1500, 0],
    ["Duronto Express", "12221", "New Delhi", "Mumbai", 1800, 120],
    ["Tejas Express", "12121", "New Delhi", "Lucknow", 1000, 150],
    ["Sampark Kranti Express", "12222", "New Delhi", "Ahmedabad", 1400, 90],
    ["Garib Rath Express", "12231", "New Delhi", "Chennai", 900, 180],
    ["Humsafar Express", "12321", "New Delhi", "Kolkata", 1300, 110]
    ]
    def bookTicket(self,TrainNo,NoOfTickets):
        for items in Train.trains:
            if(TrainNo == items[1][0]):
                if(items[1][4] > 0):
                    items[1][4] - NoOfTickets
                else:
                    return f"{NoOfTickets} tickets are not available for the train \n {items}"
        return "Your ticket has been booked and confirmed"
    def getFare(self,TrainNo):
        for items in Train.trains.items():
            if(TrainNo == items[1][0]):
                return items[1][3]
    def getTrainInfo(TrainName):
        return Train.trains[TrainName]

IR = Train()
fro = input("From: ")
to = input("To: ")
train_no = ""
for item in IR.trains:
    if fro == item[2] and to == item[3]:
        print(f"{item[0]} is available")
        train_no += item[1]
ans = input("do you want to book ticket yes/no: ")
if(ans == "yes"):
            NoOfTickets = int(input("Enter the number of tickets: "))
            print(IR.bookTicket(item[1],NoOfTickets))