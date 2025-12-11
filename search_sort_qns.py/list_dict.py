"""
A store keeps a list of product dictionaries:

products = [
    {"id": 101, "name": "Laptop", "price": 900, "stock": 12},
    {"id": 205, "name": "Keyboard", "price": 25, "stock": 85},
    {"id": 150, "name": "Monitor", "price": 180, "stock": 30},
    ...
]

Write a python program to:
a) Sort the products:
    i.   by price (low → high)
    ii.  by stock (high → low)
    iii. alphabetically by name

b) Search for a product:
    i.   by product ID (binary search)
    ii.  by name (linear search / partial match)
    iii. return all products with price within a user-defined range
"""

# -----------------------------------------------------
# A) Sorting Functions (Bubble Sort)
# -----------------------------------------------------

# i. Sort by price (low to high)
def price_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['price'] > lst[j + 1]['price']:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


# ii. Sort by stock (high to low)
def stock_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['stock'] < lst[j + 1]['stock']:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


# iii. Sort by name (alphabetically)
def alpha_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['name'].lower() > lst[j + 1]['name'].lower():
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


# -----------------------------------------------------
# Input product list from user
# -----------------------------------------------------

lst = []
n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\n--- Product {i+1} ---")
    pid = int(input("Enter product ID: "))
    name = input("Enter product name: ")
    price = int(input("Enter price: "))
    stock = int(input("Enter stock left: "))

    product = {
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock
    }
    lst.append(product)


# -----------------------------------------------------
# Sort list for searching by ID
# -----------------------------------------------------

def ids(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['id'] > lst[j + 1]['id']:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


# Sorted versions (for reference)
result1 = price_sort(lst.copy())      # Sorted by price
result2 = stock_sort(lst.copy())      # Sorted by stock
result3 = alpha_sort(lst.copy())      # Sorted alphabetically
result4 = ids(lst.copy())             # Sorted by ID


# -----------------------------------------------------
# b iii. Return all products within a price range
# -----------------------------------------------------

def ranges(lst, low, high):
    result = []
    for item in lst:
        if low < item['price'] < high:   # Change to <= if inclusive
            result.append(item)
    return result


# Get range input from user
print("\n--- Price Range Search ---")
n1 = int(input("Enter lower price: "))
n2 = int(input("Enter upper price: "))

result6 = ranges(lst, n1, n2)
print("\nProducts in price range:")
print(result6)


# -----------------------------------------------------
# Uncomment BELOW sections to enable part (b i) and (b ii)
# -----------------------------------------------------

"""
# b i. Binary search by product ID
def search(lst, target):
    lower = 0
    upper = len(lst) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid]['id'] == target:
            return mid
        elif lst[mid]['id'] > target:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1

target = int(input("Enter ID to search: "))
index = search(result4, target)
print("Product found at index:", index)
"""


"""
# b ii. Linear search (partial match by name)
def linear(lst, name):
    name = name.lower()
    for i in range(len(lst)):
        if name in lst[i]['name'].lower():
            return i
    return -1

search_name = input("Enter product name to search: ")
index = linear(result3, search_name)
print("Product found at index:", index)
"""
