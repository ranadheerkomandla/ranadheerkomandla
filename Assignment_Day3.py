#Scenario1
l=[1, 4, 9, 10, 23];
print("elements in the list: ", l);
print("slicing elements from list: ", l[1:3] , l[3:5]);
l.append(90);
print("New List: ", l);
print("Average value of the list: ", sum(l)/len(l));
del l[1:3];
print("List after deleting elements: ", l);

#Scenario 2
inputword=input("Please enter list of words")
l1=inputword.split()
print(l1)
l1.sort()
print("New list of words: ", l1)

#Scenario3
Sentence=input("Please enter sentence in the lower case:")
print("Sentence in the upper case: ", Sentence.upper())

#Scenario4
ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
}
#1
print('Dictionary: ', ages)
print("Students count in the Dictionary: ", len(ages));

#2
def getaverageage(val):
    sumvalues=sum(ages.values())
    dictlength=len(ages.values())
    averageage=sum(ages.values())/len(ages.values())
    print("Sum of the Dictionary Values: ", sumvalues, "& Length of the Dictionary values: ", dictlength)
    print("average value of the dictionary values: ", averageage)
    return averageage

print(getaverageage(ages.values()))

#3
def oldstudentname(val):
    all_ages=list(ages.values())
    all_names=list(ages.keys())
    print("All values in the dictionary: ", all_ages)
    print("All Names in the dictionary: ", all_names)
    old_student_age=max(all_ages)
    print("Oldest Student Age: ", old_student_age)
    Old_Student_Name=all_names[all_ages.index(old_student_age)]
    return Old_Student_Name


print("Oldest Student Name is: ", oldstudentname(ages.values()))

#4

