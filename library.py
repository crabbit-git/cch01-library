library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# TODO - Print welcome statement including library name
print("Welcome to " + library["name"] + "!\n")

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        # TODO - List all books
        for book in library["books"]:
            print(book["title"], "by", book["author"])
        print() # This just prints a blank line outside of the for loop for better spacing in the terminal output

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title
        title_search = input("Which title are you looking for?\n")
        # The Library is a dictionary containing two keys, the second of which is a list which in turn contains a list of dictionaries.
        # Each of these sub-dictionaries consists of a book author and title.
        # Here, we only want to search the titles specifically, so let's pull the list of titles out into a new list first:
        titles = []
        for book in library["books"]:
            titles.append(book["title"])
        # Then, let's make another list containing the search results. List comprehension helps with this.
        # I want a success message if there have been any matches, and a failure message if there are none, so I'll also use an if/else.
        # So that case matching doesn't matter, I'll casefold both the search query and the "if" condition.
        # Also, it would be a pretty bad search engine if it required an exact and complete match of the user input
        # (i.e. the entire title entered exactly as it appears in the library's system), so I'll use the string method "__contains__".
        title_results = [title for title in titles if title.casefold().__contains__(title_search.casefold())]
        if title_results != []:
            print("The following title matches were found:")
            for title_result in title_results:
                # print(title_result)
                # ... prints only the titles, not the authors, so I want to search the original dictionary for the search results instead
                # to locate the matched title's list index, then print the values of both keys (author and title) from the sub-dictionaries,
                # as I did with the "list all" response above.
                # Luckily, the list comprehension meant that my title results were kept stored as exact matches to the original titles
                # held in each book's subdictionary, so I can do an "if" statement to check if the titles in the result list match those.
                for book in library["books"]:
                    if title_result == book["title"]:
                        print(book["title"], "by", book["author"])
        else:
            print("Sorry, it doesn't look like we have that at the moment. Our selection is updated periodically, so please check back later!")
        print()

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book