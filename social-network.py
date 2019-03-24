# Created 27 July 2017

class User:
    # Define the fields and methods for your object here.
    userName = ""
    userConnections = ""
    usersList = []
    connectionsDict = {}

    def __init__(self, name, networkClass):
        self.userName = name
        self.usersList = networkClass.usersList
        self.connectionsDict = networkClass.connectionsDict

    def getUsers(self, networkClass):
        usersList = networkClass.usersList
        print("Here are the users:")
        for users in usersList:
            print(users)
        return User.getUsers

    def getConnections(self, networkClass):
        connectionsFound = 0
        connectionsDict = networkClass.connectionsDict
        viewConnections = input("Username: ")
        for user, connections in connectionsDict.items():
            if viewConnections == user:
                connectionsFound += 1
                print ("Connections: ", connections)
        if connectionsFound == 0:
            print("Either user does not exist or user has no connections")
        return User.getConnections

class Network:
    # Define the fields and methods for your object here.
    userName = ""
    userConnections = ""
    usersList = []
    connectionsDict = {}

    def __init__(self, name):
        self.userName = name

    def addUser(self):
        newUserName = input("What would you like your username to be?: ")
        self.usersList.append(newUserName)
        return Network.addUser
    def addConnection(self):
        print(self.usersList)
        firstUsername = input("Username 1: ")
        secondUsername = input("Username 2: ")
        if firstUsername or secondUsername in self.usersList:
            firstConnections = []
            secondConnections = []
            firstConnections.append(secondUsername)
            secondConnections.append(firstUsername)
            self.connectionsDict.update({firstUsername: firstConnections})
            self.connectionsDict.update({secondUsername: secondConnections})
        else:
            print("One or more users don't exist")
        return Network.addConnection

def main():
    # Define the program flow for your user interface here.
    optionList = """
What would you like to do?
1. Add User
2. Print Users
3. Add Connection
4. Print Connections
5. Quit

Enter a number: """
    programOn = True
    while programOn:
        mainMenu = input(optionList)

        myUser = User(mainMenu, Network)
        myNetwork = Network(mainMenu)
        if mainMenu == "1":
            myNetwork.addUser()
        elif mainMenu == "2":
            myUser.getUsers(Network)
        elif mainMenu == "3":
            myNetwork.addConnection()
        elif mainMenu == "4":
            myUser.getConnections(Network)
        elif mainMenu == "5":
            print("Goodbye! Thank you for using this program!")
            programOn = False
        else:
            print("Not an option!")
# Runs your program.
if __name__ == '__main__':
    main()
