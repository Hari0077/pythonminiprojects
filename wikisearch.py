import wikipedia 
des = input("Enter the heading")
query = wikipedia.page(des)
print(query.summary)
