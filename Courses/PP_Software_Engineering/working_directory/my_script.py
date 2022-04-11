import my_package

message = my_package.secret_message(clearance=False)


# Creating first instance of Document

string = "Howdy my name is Servin"
doc_one = my_package.Document(text="Howdy")
doc_two = my_package.Document(text=string)
print(doc_two.tokens)
