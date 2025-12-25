"""
Library Management Program

Features:
a) Sort books
   i.   by title
   ii.  by author
   iii. by year published

b) Search books
   i.   by specific author
   ii.  by keyword in title (case-insensitive)
   iii. earliest published book

c) Autocomplete book titles based on prefix
"""

# -------------------------------------------------
# a) SORTING FUNCTIONS (Bubble Sort)
# -------------------------------------------------

def sort_by_title(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['title'].lower() > lst[j + 1]['title'].lower():
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


def sort_by_author(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['author'].lower() > lst[j + 1]['author'].lower():
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


def sort_by_year(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j]['year'] > lst[j + 1]['year']:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


# -------------------------------------------------
# b) SEARCH FUNCTIONS
# -------------------------------------------------

# i. Search by specific author (linear search)
def search_by_author(lst, author_name):
    result = []
    for book in lst:
        if book['author'].lower() == author_name.lower():
            result.append(book)
    return result


# ii. Search by keyword in title (case-insensitive)
def search_by_title_keyword(lst, keyword):
    result = []
    for book in lst:
        if keyword.lower() in book['title'].lower():
            result.append(book)
    return result


# iii. Earliest published book (min search)
def earliest_book(lst):
    earliest = lst[0]
    for book in lst:
        if book['year'] < earliest['year']:
            earliest = book
    return earliest


# -------------------------------------------------
# c) AUTOCOMPLETE FUNCTION
# -------------------------------------------------

def autocomplete_titles(lst, prefix):
    result = []
    for book in lst:
        if book['title'].lower().startswith(prefix.lower()):
            result.append(book['title'])
    return result


# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------

books = []
n = int(input("Enter number of books: "))

for i in range(n):
    print(f"\nBook {i+1}")
    book = {
        "title": input("Enter title: "),
        "author": input("Enter author: "),
        "year": int(input("Enter year of publication: "))
    }
    books.append(book)

print("\n--- Sorted by Title ---")
print(sort_by_title(books.copy()))

print("\n--- Sorted by Author ---")
print(sort_by_author(books.copy()))

print("\n--- Sorted by Year ---")
print(sort_by_year(books.copy()))

author = input("\nEnter author name to search: ")
print("\n--- Books by Author ---")
print(search_by_author(books, author))

keyword = input("\nEnter keyword to search in title: ")
print("\n--- Books Matching Keyword ---")
print(search_by_title_keyword(books, keyword))

print("\n--- Earliest Published Book ---")
print(earliest_book(books))

prefix = input("\nEnter prefix for autocomplete: ")
print("\n--- Autocomplete Titles ---")
print(autocomplete_titles(books, prefix))
