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

# I am defining search functions up top so I can reference them later. The first part of the code to call on this function is "option 2".
def title_search():
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
        print("\nThe following title matches were found:\n")
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
        print()
    else:
        print("Sorry, it doesn't look like we have that at the moment. Our selection is updated periodically, so please check back later!\n")
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
    option = input("\nWhat would you like to do?\n")

    if option == "1":
        print("Listing all books...\n")
        # TODO - List all books
        # If this were an actual real-world application, I'd be refactoring the "books" subdictionary to separate out author surname
        # and forename so that I could then sort by author surname when returning the list of books, but that would be a pretty significant
        # modification to the code provided and might make the instructors' heads hurt (and mine), so I won't do that. Yet.
        # Instead, I'll just print the "books" sublist as-is:
        for book in library["books"]:
            print(book["title"], "by", book["author"])
        print() # This just prints a blank line outside of the for loop for better spacing in the terminal output

    if option == "2":
        print("Searching for a book by title...\n")
        # TODO - Search for a book by title
        # See the comments on the function definition near the top of the code for notes on how I approached this.
        title_search()

    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        # First off, we need two user inputs: the author and the title.
        add_author = input("Please enter the author of the book you would like to add:\n")
        add_title = input("Please enter the title of the book:\n")
        # The top of the hierarchy is a list, but the thing we want to modify is a sub-list inside it.
        # The goal is to add a new value in the form of a dictionary. Append can do this without having to specify a new variable.
        # If there was some reason to keep the original version of the library then I'd keep this as a new variable instead, but
        # I can't think of one right now, so I will instead just modify it directly.
        library["books"].append(
            {
                "author": add_author,
                "title": add_title
            }
        )
        print(add_title, "by", add_author, "has been successfully added to", library["name"] + "!\n")

    if option == "4":
        print("Removing a book...\n")
        # TODO - Remove a book
        # We could do this by index, but that'd be kind of a weird way of writing a program like this if it were to be used IRL.
        # It's probably better to use the search function from before.
        # This is the main reason I have defined the search code as a function rather than leaving it hardcoded to option 2:
        # otherwise, I'd have to repeat the same code again below.
        title_search()
        # I want to make sure that only the specific book the user wants rid of is deleted, so I want to check if the search results
        # exceed one list item. However, I'm struggling to get this to work. I thought I could just get the search function to return
        # "title_results", but it seems not to work and I'm not yet sure why. I'll comment this bit out for now.
        # if len(title_results) > 1:
            # print("More than one book matches your search query. Please try a more specific query.\n")
        # In case the user couldn't remember the book title but knew the author, I would ideally like to also add an author search too.

    if option == "5":
        print("Updating a book...\n")
        # TODO - Update a book