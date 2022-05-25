def checknr(number, checknumber, nr_correct, nr_correct_position):
     count_nr_correct = 0
     count_nr_correct_position = 0
     lnumber = str(number).zfill(len(checknumber))
     for i in range(len(checknumber)):
         if lnumber[i] in checknumber:
             count_nr_correct += 1
         if lnumber[i] == checknumber[i]: 
             count_nr_correct_position += 1 
     return    nr_correct == count_nr_correct and \
               nr_correct_position == count_nr_correct_position        
def chechnr2(number, checknumber, nr_correct , nr_correct_position):
    lnumber =str(number).zfill(len(checknumber))
    return nr_correct == sum(lnumber[i] in checknumber for i in range(len(checknumber))) 
    nr_correct_position == sum(lnumber[i]==checknumber for i in range(len(checknumber)))
for cnumber in range(1000):
    if checknr(cnumber, "690", 1, 1)  and \
       checknr(cnumber, "741", 1, 0)  and \
       checknr(cnumber, "504", 2, 0)  and \
       checknr(cnumber, "387", 0, 0)  and \
       checknr(cnumber, "219", 1, 0):
       print("Kod bulundu: " + str(cnumber).zfill(3))
       

   


