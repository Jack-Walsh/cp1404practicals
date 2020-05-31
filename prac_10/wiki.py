import wikipedia

user_search = input("Enter your search word here: ")
if user_search == "":
    print("Search has ended. Try again!")
else:
    try:
        user_search = wikipedia.page(user_search)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    print(user_search.title)
    print(user_search.summary)
    print(user_search.url)