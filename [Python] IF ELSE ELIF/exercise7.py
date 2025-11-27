exam1 = float(input("Put the medium of the student: "))
exam2 = float(input("Put the second medium of the student: "))
exam3 = float(input("Put the third medium of the student: "))

medium = (exam1 + exam2 + exam3) / 3
if medium >=7:
    print("Approved")
elif 5 <= medium < 7:
    print("Recovery")
else:
    print("Reproved")