# Cryptographic Password Generator

A terminal-based tool to generate, analyze, and securely store randomized passwords.


## Features

- Cryptographically strong password generation
- Configurable length & character sets
- Strength analysis via `zxcvbn`
- Save & retrieve history in JSON file
- ASCII art banner (pyfiglet)


## Project Structure

The application is built using object-oriented programming principles with two main classes:
- `PasswordGenerator`: Handles password generation and strength analysis
- `PasswordStorage`: Manages password storage, retrieval, and encryption


## Input/Output Operations

The application implements multiple types of input/output:
- Command-line interface for user interaction
- File I/O for password storage
- Terminal output with colored ASCII art and formatted results


## Setup / Installation

1. Clone the repo

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```


## Usage

Users invoke the tool entirely via the terminal:

```bash
$ python main.py [OPTIONS]
```

| Flag                 | Description                                                              | Default    |
| -------------------- | ------------------------------------------------------------------------ | ---------- |
| `-h`, `--help`       | Show usage instructions                                                  | N/A        |
| `-l`, `--length`     | Desired password length                                                  | **12**     |
| `-L`, `--no-lower`   | Exclude lowercase letters                                                | Include    |
| `-U`, `--no-upper`   | Exclude uppercase letters                                                | Include    |
| `-D`, `--no-digits`  | Exclude digits                                                           | Include    |
| `-S`, `--no-symbols` | Exclude symbols (e.g. `!@#$%`)                                           | Include    |
| `-s`, `--save`       | Append the generated password to `passwords.json`                        | Don't save |
| `-n`, `--name TEXT`  | Assign a label to the password                                           | None       |
| `--strength`         | (If `zxcvbn` is installed) Print entropy score and note                  | Off        |
| `--search TEXT`      | Print saved password that includes TEXT                                  | None       |

**Notes:**
- `--save` and `--name` must be used together
- Use quotes for multi-word names: `-s -n "my bank"`
- When using `--search`, other flags are ignored
- Duplicate names will prompt for overwrite confirmation

## Examples:
```bash
  # Generate a 16-character password
  python main.py -l 16

  # Generate password with only letters and numbers
  python main.py -S

  # Save a password with a name
  python main.py -s -n "email"

  # Check password strength
  python main.py --strength

  # Search for a saved password
  python main.py --search "email"
```


## Requirements

- Python 3.6+
- Virtual environment (recommended)
- Required packages (see requirements.txt)


## Third-Party Packages

| Package  | Version | License    | Impact                          |
| -------- | ------- | ---------- | ------------------------------- |
| pyfiglet | ^0.8.1  | MIT        | Permissive, minimal obligations |
| zxcvbn   | ^4.4.28 | BSD-3      | Permissive                      |
| colorama | ^0.4.6  | BSD-3      | Permissive                      |

### License Information

- **MIT License** (pyfiglet): Permits commercial use, modification, distribution, and private use. Requires license and copyright notice.
- **BSD-3** (zxcvbn): Permits commercial use, modification, distribution, and private use. Requires license and copyright notice.

All licenses are permissive and suitable for both personal and commercial use. The main obligations are maintaining copyright notices and license information in the code.


## Error Handling

The application implements comprehensive error handling:
- Invalid user input validation
- File I/O error handling
- Password generation constraints
- Fallbacks for missing dependencies