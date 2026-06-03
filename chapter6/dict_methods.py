d ={} #empty dictionary

marks = {
    "urvi" : 100,
    "tia" :43,
    "manu" : 78,
    23: "ashi"
}

#print(marks.items()) #it gives key value pairs list
# and these key value pairs are in form of tuple

#how to get keys only?
#print(marks.keys())

#how to get values only?
#print(marks.values())

#how to change/ update values in dict

#marks.update({"urvi": 99, "renu":100} )



#print (marks)

print(marks.get("urvi"))
print(marks["urvi"])

print(marks.get("urvi2")) #gives none at output
print(marks["urvi2"]) #gives error at output