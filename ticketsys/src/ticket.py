import os
import random

def GenerateNewTicket():
    ticketid = random.randint(1234,9999) + 1
    ticket = int(((ticketid * 16) / 2)) + 1
    fi = open("ticketDB", "a")
    fi.write(str(ticket) + "\n")
    fi.close()

    return ticket

def CheckIDConflict():
    os.error(NotImplementedError)

print("Ticket ID: " , GenerateNewTicket())