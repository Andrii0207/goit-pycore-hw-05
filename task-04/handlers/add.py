from decorator.input_error import input_error


# def input_error(func):
#     def inner(*args, **kwargs):

#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."

#     return inner


@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts.keys():
        return (f"ERROR: Contact {name} is already exist ")

    if phone in contacts.values():
        return (f"ERROR: Phone {phone} has another contact ")

    contacts[name] = phone
    return "Contact added."
