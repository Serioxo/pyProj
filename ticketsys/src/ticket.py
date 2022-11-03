import random

def GenerateNewTicket():
    ticketid = random.randint(1234, 9999) + 1
    ticket = int(((ticketid * 16) / 2)) + 1
    ticketList = []

    ticketList.insert(1, ticket)

    fi = open("ticketDB", "a")

    if ticket == ticketList:
        ticketid = random.randint(1234, 9999) + 1
        ticket = int(((ticketid * 16) / 2)) + 1
    else:

        fi.write("Ticket ID: " + str(ticket) + "\n")

    fi.close()

    return ticket

def UserPromptTicket():
    print("#########################################################################\n")
    print("========= Welcome to the Ticket Report System =========\n")

    username = input("Input your Name: ")
    userDepartment = input("Input your Department: ")
    TicketIssue = input("Input your issue: ")

    userdata = [username, userDepartment, TicketIssue]

    fi = open("ticketDB", "a")
    fi.write(str(userdata) + "\n")
    fi.close()
    return userdata

def GenerateTicketWithUserInput():
    print(UserPromptTicket())
    print("Your Ticket has been Generated Here is the ID of your ticket: ", GenerateNewTicket())


GenerateTicketWithUserInput()
