#list
Reg_No=[20,40,60,80,100]
Reg_No.append(60)
Reg_No.remove(80)
Reg_No[0]=5
print("Updated List:",Reg_No)

#dict
data={"Name":"Shobhini","Age":20,"City":"Coimbatore"}
data["Gender"]="Female"
del data["Age"]
data["City"]="Delhi"
print("Updated Dictionary:",data)

#set
n={3,5,7,9}
n.add(11)
n.remove(5)
n.discard(3)
n.add(13)
print("Updated Set:",n)




