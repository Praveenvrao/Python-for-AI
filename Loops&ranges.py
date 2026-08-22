# If & If else & elif statements

age = 2
if age >= 18:
    print("You are an adult so please cast your vote.")
else:
    print("You are not an adult so please wait for few years to cast your vote.")

Availability = True
Balance_for_Ticket = 100
if Availability == True:
    if Balance_for_Ticket >= 100:
        print("You can book your ticket.")
    else:
        print("You don't have enough balance to book your ticket.")
elif Availability == False:
    print("Sorry, the ticket is not available.")
else:
    print("Please check the availability and Balance correctly.")


# Ranges
for i in range(5):
    print(i)

for j in range(1, 10, 2):
    print(j)

for k in range(10, 0, -1):
    print("Just Testing the range function in reverse order: ", k)

