# exercise 1
inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)

# exercise 2
stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

total = 0

for x in prices:
    print(x)
    print("price:", prices[x])
    print("stock:", stock[x])
    profit = prices[x] * stock[x]
    print("Profits from the entire stock: ", profit)
    print()

    total+=profit
print("Total:", total)

# exercise 3

fruit_list = ["banana", "orange", "apple", "pear", "sunkist", "melon", "avocado", "peach"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }


def compute_bill(fruit_list):
    total = 0
    for x in fruit_list:
      if stock.get(x, 0) > 0:
        total += prices.get(x, 0)
        stock[x] -= 1
    return total

print("Total Price: ", compute_bill(fruit_list))

# exercise 4
eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}
mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = ["eren","mikasa","armin"]
for x in students:
    print("Student name:", eval(x + "['name']"))
    print("Homework scores:", eval(x + "['homework']"))
    print("Quizzes scores:", eval(x + "['quizzes']"))
    print("Test scores:", eval(x + "['tests']"))
    print()

def average(numbers):
    total = float(sum(numbers)) / len(numbers)
    return total

def get_average(student):
    homework = average(eval(s + "['homework']")) * 0.1
    quizzes = average(eval(s + "['quizzes']")) * 0.3
    tests = average(eval(s + "['tests']")) * 0.6
    return homework + quizzes + tests

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for i in students:
        results.append(get_average(i))
    return average(results)

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))