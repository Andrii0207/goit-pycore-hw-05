from decorator.input_error import input_error


@input_error
def change_contact(args, contacts):

    for key, value in contacts.items():
        if key == args[0]:
            print(f"WARNING! You are going to change phone {args[0]}?")
            user_answer = input(
                "for change press Y or N for cancel: ").strip().lower()

            if user_answer == "y":
                contacts[args[0]] = args[1]
                return "Contact updated."

            return f"You refused to update {args[0]} number"
