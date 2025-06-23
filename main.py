import argparse
from banner import print_banner
from password_generator import PasswordGenerator
from password_storage import PasswordStorage


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate secure, random passwords with various options."
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="Desired password length (default: 12)",
    )

    parser.add_argument(
        "-L", "--no-lower", action="store_true", help="Exclude lowercase letters"
    )
    parser.add_argument(
        "-U", "--no-upper", action="store_true", help="Exclude uppercase letters"
    )
    parser.add_argument("-D", "--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument(
        "-S", "--no-symbols", action="store_true", help="Exclude symbols"
    )

    # Save and metadata options
    parser.add_argument(
        "-s",
        "--save",
        action="store_true",
        help="Append the generated password to passwords.json (Requires --name)",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Assign a human-readable label to the password. Must be singular. (Required with --save)",
    )

    # Analysis and search options
    parser.add_argument(
        "--strength", action="store_true", help="Print entropy score and strength note"
    )
    parser.add_argument(
        "--search",
        type=str,
        help="Lookup and display saved entries containing the search text",
    )

    return parser.parse_known_args()


def main():
    print_banner()
    args, unknown = parse_arguments()
    if unknown:  # handle the case where user enters unknown arguments
        print(f"Unknown arguments: {', '.join(unknown)}")
        if args.name:
            print(
                "Error: name must be singular as whitespace causes failure. For e.g.: two_words = singular, two words = error."
            )
            print("Password will not be saved.\n")
        return

    if (
        args.search
    ):  # checks for other arguments that make no sense while using --search
        if (
            args.length != 12
            or args.no_lower
            or args.no_upper
            or args.no_digits
            or args.no_symbols
            or args.save
            or args.name
            or args.strength
        ):
            print("Note: Other arguments are ignored when using --search.\n")

        try:
            passwords = PasswordStorage("passwords.json").read_passwords()
            for entry in passwords:
                if entry["name"] == args.search:
                    print(f"Name: {entry['name']}")
                    print(f"Password: {entry['password']}\n")
                    break  # just end the program here to prevent generating another password
            else:
                print("No matching entries found.\n")
        except IOError as e:
            print(f"Error reading passwords: {e}\n")
        return

    try:
        generator = PasswordGenerator()
        password = generator.generate_password(
            length=args.length,
            use_lower=(args.no_lower == False),
            use_upper=(args.no_upper == False),
            use_digits=(args.no_digits == False),
            use_symbols=(args.no_symbols == False),
        )
        print(f"Your password is: {password}\n")

        # strength check
        if args.strength:
            strength_results = generator.check_strength(password)
            score = strength_results["score"]
            print(
                f"Password strength is determined by a number between 0 and 4. The higher the number, the stronger your password is.\nPassword strength: {score}\n"
            )

        # saving to file
        if args.save == True and args.name == None:
            print(
                "Error: You must provide a name with --save using the --name flag.\nPassword will not be saved.\n"
            )
            return
        if args.name != None and args.save == False:
            print(
                "Error: The --name flag only works with --save. Use both together.\nPassword will not be saved.\n"
            )
            return
          
        # ... after generating the password and before saving
        if args.save == True and args.name != None:
          storage = PasswordStorage("passwords.json")
          passwords = storage.read_passwords()

          # Duplication check and user prompt
          duplicate = None
          for entry in passwords:
            if isinstance(entry, dict) and "name" in entry and entry["name"] == args.name:
              duplicate = entry
              break
            
          if duplicate is not None:
            while True: # handling user input
              response = input("Password with this name exists, overwrite? (y/n): ").strip().lower()
              if response == "y":
                passwords = [entry for entry in passwords if entry["name"] != args.name]
                passwords.append({"name": args.name, "password": password})
                storage.write_passwords(passwords)
                print("Password overwritten.\n")
                break # finish if password is overwritten
              elif response == "n":
                print("Password will not be saved.\n")
                return  # Exit the program after declining
              else:
                print("Please enter 'y' or 'n'.") # keep looping
          else:
            passwords.append({"name": args.name, "password": password})
            storage.write_passwords(passwords)
            print("Password saved.\n")

    # final error catching
    except ValueError as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("\nOperation cancelled by user. Exiting...\n")
