My Solution: import inflect
p = inflect.engine()
Ist = |]
while True:
try:
name = input("Names: ")
Ist.append (name)
except EOFError:
print ("\n")
break
for name in Ist:
mylist = p.join ((Ist), final_sep=",")
print (f"Adieu, adieu, to {mylist}")
