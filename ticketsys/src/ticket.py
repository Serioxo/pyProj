import os
import random



def GenerateNewTicket():
    ticketid = random.randint(1234,9999) + 1
    ticket = int(((ticketid * 16) / 2)) + 1
    ticketList = []

    ticketList.insert(1,ticket)

    fi = open("ticketDB", "a")

    if ticket == ticketList:
        ticketid = random.randint(1234,9999) + 1
        ticket = int(((ticketid * 16) / 2)) + 1 
    else:

        fi.write(str(ticket) + "\n")

    fi.close()

    return ticket


def UserPromptTicket():
    print("#########################################################################\n")
    print("========= Hello, Please input an issue you are having. =========\n")

    TicketIssue = input("")



def GenerateTicketWithUserInput():
    UserPromptTicket()

    print("Your Ticket has been Generated Here is the ID of your ticket: ", GenerateNewTicket())


GenerateTicketWithUserInput()