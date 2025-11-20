# Exercise 3-4: Guest List
# A list of guests I'd like to have for dinner
guests = ["Richard", "Sabrina", "Taylor", "Chase"]

# An invite to each guest.
for guest in guests:
    print("Hi " + guest.title() + ", I would be honored if you joined me for dinner.")

# Exercise 3-5: Changing Guest List
# The guest who can't make it
print("\n" + guests[1].title() + " can't make it to dinner.")
# Replacing the guest who can't come
guests[1] = "David"

# Updated invitations
for guest in guests:
    print("Hi " + guest.title() + ", I would be delighted if you could join me for dinner.")

# Exercise 3-6: More Guests
# Announce a bigger table
print("\nGood news! I've found a bigger table.")

# Add three more guests
guests.insert(0, "Willis")   # head index  
guests.insert(2, "Mark")     # median index
guests.append("Jude")        # terminal index

# Final invitations
for guest in guests:
    print("Hi " + guest.title() + ", please come to dinner.")
