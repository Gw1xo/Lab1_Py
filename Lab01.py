
# Task 1
var1 = int(input("Enter int var1 ="))
var2 = int(input("Enter int var2="))
var3 = float(input("Enter float var3 ="))
var4 = float(input("Enter float var4 ="))

# Task 2
# list creation and initialization
rezlist = [round(var1 + var2 + var3 + var4 , 3)]
rezlist.append(round(var1 - var2 - var3 - var4 , 3))
rezlist.append(round(var1 * var2 * var3 * var4 , 3))
rezlist.append(round(var1 / var2 / var3 / var4 , 3))
rezlist.append(round(var3 ** var2 , 3))
rezlist.append(round(var1 // var2 , 3))
rezlist.append(round(var1 % var3 , 3))

# Displaying the results on the screen
print(f"var1 // var4 = {rezlist[6]}")
print(f"\nvar1 + var2 + var3 + var4 = {rezlist[0]}")
print(f"var1 - var2 - var3 - var4 = {rezlist[1]}")
print(f"var1 * var2 * var3 * var4 = {rezlist[2]}")
print(f"var1 / var2 / var3 / var4 = {rezlist[3]}")
print(f"var1 ** var2 = {rezlist[4]}")
print(f"var3 // var4 = {rezlist[5]}")
print(f"List = {rezlist}")


# Task 3
# Displaying the length of list
print(f"List length = {len(rezlist)}")
# Displaying even numbers of list
print(f"Even numbers of list = {[i for i in rezlist if (i%2 == 0) and (i != 0)]}")

# Task 4
rezlist[1], rezlist[4] = rezlist[4], rezlist[1]
print(f"Permutation of the 2 and 5 elements of the list = {rezlist}")

# Task 5
name = input("Input name:")
print(f"Hi, I`m {name}, and I was doing this lab work")
print("Висновки: На лабораторній роботі я ознайомився з алгоритмами послідовної структури,\n"
      "з процедурами запуску програм, які реалізують ці алгоритми на мові Python;\n"
      "ознайомився з інтегрованим середовищем розробки PyCharm")