#while example of numbers taqbal alqesma 3la 4

print("program start")
i=0
while (i<100):
    if(i%4==0):
        print("count {}".format(i))
    i+=1
    
    
print("program end\n")


######################################################


#for example, printing list items (iterator)

l=[1,2,4,'Hi',5.7]
for item in l: #pass on every "item" on "l"
    print(item)
print("program end\n")

##########################################################

#break - continue example

word="realmadrid"
for letter in word:
    print (letter)
    if(letter=='m'):
        break #stops at 'm' (include m)
print("program end\n")

word="realmadrid"
for letter in word:
    if(letter=='m'):
        continue #skipping 'm'
    print(letter)
    
######################################################








    