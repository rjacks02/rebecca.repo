lst = [10, 20, 30, 40, 50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40)
print(lst)

lst.pop(2)
print(lst)

lst.reverse() #alters original list
print(lst)

lst.sort() #alters original list
print(lst)

lst[0] = 500
print(lst)

lst = lst[1:]
print(lst)

index = lst.index(7)
print(index)

lst.append(20)
lst.append(20)
lst.append(20)

print(lst)

num20 = lst.count(20)
print(num20)

lst_copy = lst
print(lst_copy)
lst_copy[1] = 99
print(lst_copy)
print(lst)

new_copy = lst.copy() #or new_copy = lst[:]
print(new_copy)
new_copy[0] = 1000
print(lst)
print(new_copy)

empty_lst = []
for val in lst:
    empty_lst.append(val)
print(empty_lst)

empty_lst = [0] * 10
print(empty_lst)
empty_lst[1] = 100
print(empty_lst)

squares = []
for i in range(1,10):
    squares.append(i**2)
print(squares)

plus_5 = [val+5 for val in lst]
print(plus_5)

small_vals = [x for x in lst if x<20]
print(small_vals)

fav_foods = {"Kathleen" : "pizza", "Maya" : "ice cream", "Tom" : "ice cream", 
             "Eric" : "steak"} #keys must be unique
print(fav_foods)

mff = fav_foods["Maya"]
print(mff)

for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}")

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

# print(fav_foods["Bob"])
    
if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)