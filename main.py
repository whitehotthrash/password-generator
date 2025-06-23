# TODO: Main program
# - Save to JSON if requested

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
        help="Append the generated password to passwords.json",
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Assign a human-readable name/label to the password",
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
    if unknown:
        print(f"Unknown arguments: {', '.join(unknown)}")
        if args.name:
          print("Error: name must be singular as whitespace causes failure. For e.g.: two_words = singular, two words = error.")
          print("Password will not be saved.")
        return

    if args.search: # checks for other arguments that make no sense while using --search
        if args.length != 12 or args.no_lower or args.no_upper or args.no_digits or args.no_symbols or args.save or args.name or args.strength:
          print("Note: Other arguments are ignored when using --search.")
      
        try:
          passwords = PasswordStorage("passwords.json").read_passwords()
          for entry in passwords:
            if entry["name"] == args.search:
              print(f"Name: {entry['name']}")
              print(f"Password: {entry['password']}")
              break # just end the program here to prevent generating another password
          else:
            print("No matching entries found.")
        except IOError as e:
          print(f"Error reading passwords: {e}")
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
        print(f"\nYour password is: {password}\n")

        if args.strength:
            strength_results = generator.check_strength(password)
            score = strength_results["score"]
            print(
                "\nPassword strength is determined by a number between 0 and 4. The higher the number, the stronger your password is."
            )
            print(f"Password strength: {score}\n")

        if args.save:
            try:
                storage = PasswordStorage("passwords.json")
                write_data = {"name": args.name, "password": password}
                storage.write_passwords(write_data)
                print("Password saved.\n")
            except IOError as e:
                print(f"Error saving password: {e}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
