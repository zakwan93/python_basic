attenndees = ["Zakwan","Orlando","Chris","Sam"]

# .append method is use to add value at end of the list 
attenndees.append("Michal")

# .extend method is use to combined one list to another list
# ADD data of one list to existing list
attenndees.extend(["Erin","Krystal"])

# .Concat is achived by adding + sign bettween two list varriblae and store in new varrialbe

optional_ivitees = ["Mike","Elyse"]

potential_attedees = attenndees + optional_ivitees

to_line = ", ".join(attenndees)
cc_line = ", ".join(optional_ivitees)
print("To:  " + to_line)
print("Cc:  " + cc_line)

print("There are",len(potential_attedees),"attenndees currently! ")