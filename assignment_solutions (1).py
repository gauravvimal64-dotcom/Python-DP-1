

# 1. Swap two variables without using a third variable
a = 5
b = 10
a, b = b, a
print("1) After swapping: a =", a, ", b =", b)

# 2. Take user's name and age, print message
# Uncomment below lines to take real input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
name, age = "TestUser", 25  # demo values
year_100 = 2025 - age + 100
print(f"2) Hello {name}, you will turn 100 years old in {year_100}.")

# 3. Check if number is positive, negative, or zero
num = 5
if num > 0:
    print("3) Positive")
elif num < 0:
    print("3) Negative")
else:
    print("3) Zero")

# 4. Print numbers from 1–50 divisible by 3 and 5
print("4) Numbers divisible by 3 and 5 from 1–50:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print()

# 5. Check if string is palindrome
s = "madam"
if s == s[::-1]:
    print("5) Palindrome")
else:
    print("5) Not Palindrome")

# 6. Find the second largest number in a list
nums = [10, 20, 4, 45, 99, 99]
unique_nums = list(set(nums))
unique_nums.sort()
print("6) Second largest number:", unique_nums[-2])

# 7. List comprehension → even numbers from 1 to 100
evens = [x for x in range(1, 101) if x % 2 == 0]
print("7) Even numbers from 1 to 100:", evens)

# 8. Sort list of strings & search for one
words = ["apple", "banana", "cherry", "date", "fig"]
words.sort()
print("8) Sorted list:", words)
search = "banana"
if search in words:
    print("   Found:", search)
else:
    print("   Not found")

# 9. Remove duplicates from a list (without set)
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in lst:
    if item not in unique_list:
        unique_list.append(item)
print("9) List without duplicates:", unique_list)

# 10. Tuple → sum, max, min
t = (10, 20, 30, 40, 50)
print("10) Sum:", sum(t))
print("    Max:", max(t))
print("    Min:", min(t))

# 11. Tuple → List → Modify → Back to Tuple
t = (1, 2, 3, 4, 5)
lst = list(t)
lst.append(6)
t = tuple(lst)
print("11) Modified tuple:", t)

# 12. Count word frequency using dictionary
text = "this is a test this is only a test"
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("12) Word frequency:", freq)

# 13. Nested dictionary for student scores
students = {
    "Alice": {"Math": 90, "Science": 85, "English": 88},
    "Bob": {"Math": 75, "Science": 95, "English": 80},
    "Charlie": {"Math": 82, "Science": 78, "English": 92}
}
highest_student = max(students, key=lambda name: sum(students[name].values()))
print("13) Top student:", highest_student)

# 14. Update salary of employee
employees = {"John": 50000, "Mary": 60000, "Sam": 55000}
name, new_salary = "Mary", 65000
if name in employees:
    employees[name] = new_salary
    print("14) Updated employees:", employees)
else:
    print("14) Employee not found.")

# 15. Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("15) Union:", set1 | set2)
print("    Intersection:", set1 & set2)
print("    Difference (set1 - set2):", set1 - set2)

