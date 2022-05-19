#write a guest list then expand and shrink it

invitees = ["shelly", "johnny", "david", "lindsey", "mom", "dad"]

print("the invitees are")
for guest in invitees:
	print(guest)

print("We can only invite two people for dinner")


invitees.insert(0, 'Jake')

while len(invitees)>2 :
	newinvites = invitees.pop(-1)
	print(newinvites, ", you are uninvited to dinner",sep="")


while len(invitees)>0 :
	print(invitees.pop(), ", you are still invited to dinner.", sep="")


print(invitees)
