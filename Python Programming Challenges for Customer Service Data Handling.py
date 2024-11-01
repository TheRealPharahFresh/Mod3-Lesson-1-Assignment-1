# Task 1:
#  Customer Service Ticket Tracker 
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def ticket_tracker():
    print("Welcome To The Ticket Tracker System")
    while True:
        print("Menu Options:\n1.Open A New Service Ticket\n2.Update Status Of A Existing Ticket\n3.Display All Tickets\n4.Exit")
        user_input = int(input("Which Option Do You Choose?: "))
        
        
        if user_input == 1:
            new_service_ticket()
        elif user_input == 2:
            update_existing_ticket()
        elif user_input == 3:
             display_tickets()
        elif user_input == 4:
             print("Exiting Now.....")
             break
        else:
             print("Invalid Choice Chosen")
             


def new_service_ticket():
     ticket_number = input("What is your ticket number? (e.x. Ticket001): ")
     if ticket_number in service_tickets:
          print("This ticket number already exist. Please Choose a different one!")
          return
     customer = input("What is your name?: ")
     issue = input("what is the issue? If there is one?:")
     status = input("Is this case open/closed?: ")
     service_tickets[ticket_number] = {"Customer": customer, "Issue": issue, "Status": status}
     print(service_tickets)
     print(f"New Ticket {ticket_number} created successfully!")


def update_existing_ticket():
        print("Which Ticket Would You Like To Update")
        display_tickets()
        ticket_number = input("Pick A Ticket To Update Out Of Tickets Provided")

        if ticket_number in service_tickets:
             new_status = input("Enter New Status open/closed")
             service_tickets[ticket_number]["Status"] = new_status
             print(f"Ticket {ticket_number} has been updated to {new_status}")
             print(service_tickets)
        else:
             print("Ticket is not found")


def display_tickets():
     if not service_tickets:
          print("No Tickets Available")
          return
     for ticket, info in service_tickets.items():
          print(f"{ticket}: Customer: {info['Customer']}, Issue: {info['Issue']}, Status: {info['Status']}")

          



        


ticket_tracker()



