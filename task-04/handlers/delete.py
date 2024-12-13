from decorator.input_error import input_error


@input_error
def delete_contact(args, contacts):
    name, _ = args

    if not name in contacts.keys():
        return (f"Warning! {name} is not exist in contacts")

    del contacts[name]
    return f"Contact '{name}' has been deleted."
