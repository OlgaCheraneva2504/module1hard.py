grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]    # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}    
list_of_students = sorted(list(students))
x = len(grades)
n = len(grades) - x
a = 0
average_prices = {}
while a < x:
        a = n + a
        b = sum(grades[a]) / len(grades[a])
        average_prices.update({list_of_students[a]: b})
        a += 1
print(average_prices)
















