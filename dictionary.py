#phonebook = {}

#phonebook["prova"] = 1
#phonebook["upo"] = 2

#print(phonebook["prova"])

#for name, number in phonebook.items():
    #print ("Phone number of %s is %d" % (name, number))

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
#initiized
# write your code here
phonebook["Jake"] = 938273443 #add
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:
    print ("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print ("Jill is not listed in the phonebook.")

