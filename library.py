library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George R. R. Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J. R. R. Tolkien",
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

# I am defining various traversal functions up top so I can reference them later.
# The first part of the code to call on this function is "option 2"; scroll down to see notes on what I'm doing with the code.
# I'm considering just turning every option into a function call for consistency's sake, but for the time being,
# I've only defined functions for the more complex operations and left the simple stuff in the main body of the code.

no_changes_made = "The library has not been modified. Returning to the main menu.\n"
# This is purely so I can repeatedly print this message in different scenarios without hardcoding it in repeatedly for no real reason.

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
    book_results = []
    if title_results != []:
        print("\nThe following title matches were found:\n")
        for title_result in title_results:
            # print(title_result)
            # ... prints only the titles, not the authors, so I want to search the original dictionary for the search results instead
            # to locate the matched title's list index, then print the values of both keys (author and title) from the sub-dictionaries,
            # as I did with the "list all" response (option 1).
            # Luckily, the list comprehension meant that my title results were kept stored as exact matches to the original titles
            # held in each book's subdictionary, so I can do an "if" statement to check if the titles in the result list match those.
            for book in library["books"]:
                if title_result == book["title"]:
                    print(book["title"], "by", book["author"])
                    book_results.append(book)
        print() # This just prints a blank line outside of the for loop for better spacing in the terminal output.
    else:
        print("\nSorry, it doesn't look like we have that at the moment. Our selection is updated periodically, so please check back later!\n")
    return book_results

def remove_book():
    search_results = title_search()
    # I want to make sure that only the specific book the user wants rid of is deleted, so I want to check if the search results
    # exceed one book (since we're deleting only one book from the library).
    if len(search_results) > 1:
        print("More than one book matches your search query. Please try a more specific query.\n")
        print(no_changes_made)
    # If there is precisely one result, then the user can go ahead and remove it, with confirmation of course:
    elif len(search_results) == 1:
        confirm_match = input("Is this what you'd like to remove? Type \"DELETE\" to confirm deletion, or anything else to go back to the main menu.\n")
        for search_result in search_results:
            if confirm_match == "DELETE":
                index_to_remove = library["books"].index(search_result)
                removed_book = library["books"].pop(index_to_remove)
                print("\n" + removed_book["title"], "by", removed_book["author"], "has been removed from the library.\n")
            else:
                print("\nDeletion cancelled.\n")
                print(no_changes_made)
    # The only other possibility is that there are no results, in which case a message will be printed from within the search function
    # to acknowledge this, followed by an additional message confirming that the library hasn't been altered:
    else:
        print(no_changes_made)
    return

def edit_book():
    # This is very similar to my deletion function except it's replacing a subdictionary by string matching,
    # rather than removing it by index (I had to get the index before to use ".pop()" but that isn't needed for replacement).
    search_results = title_search()
    if len(search_results) > 1:
        print("More than one book matches your search query. Please try a more specific query.\n")
        print(no_changes_made)
    elif len(search_results) == 1:
        confirm_match = input("Is this the book you'd like to update? Type \"EDIT\" to confirm, or anything else to go back to the main menu.\n")
        for search_result in search_results:
            if confirm_match == "EDIT":
                edit_author = input("Please enter the author as it should appear in the library:\n")
                edit_title = input("Please enter the title as it should appear in the library:\n")
                updated_book = {
                    "author": edit_author,
                    "title": edit_title
                }
                new_booklist = [updated_book if book == search_result else book for book in library["books"]]
                library["books"] = new_booklist
                print("\n" + updated_book["title"], "by", updated_book["author"], "has been updated successfully.\n")
            else:
                print("\nEdit cancelled.\n")
                print(no_changes_made)
    else:
        print(no_changes_made)
    return

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
        # Instead, I'll just print the "books" sublist (of dictionaries) as is:
        for book in library["books"]:
            print(book["title"], "by", book["author"])
        print() # This just prints a blank line outside of the for loop for better spacing in the terminal output.

    if option == "2":
        print("Searching for a book by title...\n")
        # TODO - Search for a book by title
        # See the comments on the function definition near the top of the code for notes on how I approached this.
        title_search()

    if option == "3":
        print("Adding a book...\n")
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
        # We could just do this by index directly, but that'd be kind of a crap implementation in a real-world application.
        # It's probably better to use the search function from before.
        # This is the main reason I have defined the search code as a function rather than leaving it hardcoded to option 2:
        # otherwise, I'd have to repeat the search code again below.
        # I made the book deletion code a function as well.
        remove_book()

        # In case the user couldn't remember the book title but knew the author, I would ideally like to also add an author search too.
        # However, I should probably stop working on this and do something else for a while!

    if option == "5":
        print("Updating a book...\n")
        # TODO - Update a book
        edit_book()