from student import Student

s1 = Student("Rebecca", "Jackson", 914, 10)
s2 = Student("Anna", "Angelozzi", 520, 5)

print(s1)
print(s2)

print(s1.greeting())
print(s2.greeting())

print(s1.get_energy_level())
print(s2.get_energy_level())

s1.take_exam()
s2.take_exam()
s2.take_exam()

print(s1.get_energy_level())
print(s2.get_energy_level())