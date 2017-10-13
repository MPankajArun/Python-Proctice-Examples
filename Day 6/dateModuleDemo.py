from datetime import date

now = date.today()
print "Today : ",now
print "----------------------------------------------------------"
ord1 = now.toordinal()+3

print "Date after 3 days: ",date.fromordinal(ord1).strftime('%m-%d-%y')

print "----------------------------------------------------------"
birthday = date(1992,05,20)
age = now - birthday
print "Age : ",age
print "----------------------------------------------------------"

print dir(date)
print "----------------------------------------------------------"

"""
A young boy enters a barber shop and the barber whispers to his Customer, "This is the dumbest kid in the world. Watch while I prove it to you."

The barber puts a five rupee coin in one hand and two one rupee coins (1+1=2) in the other, then calls the boy over and asks, "Which do you want, son?"

The boy takes the two one rupee coins and leaves.

"What did I tell you?" said the barber. "That kid never learns!"

Later, when the customer leaves, he sees the same young boy coming out of the ice cream store.

"Hey, son! May I ask you a question?

Why did you take two one rupee coins instead of five rupee coin?"

The boy licked his cone and replied,

"BECAUSE THE DAY I TAKE THE FIVE RUPEE COIN, THE GAME IS OVER"

"""
