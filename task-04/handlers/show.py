from decorator.input_error import input_error


@input_error
def show_phone(args, contacts):
    for key, value in contacts.items():
        if key == args[0]:
            print(f"Result \n>>> {key}: {value}")
            break
        return f"There's no phone number {args[0]} in contacts"
