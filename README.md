# Cryptographic Password Generator

A terminal-based tool to generate, analyze, and securely store randomized passwords.

## Features

- Cryptographically strong password generation
- Configurable length & character sets
- Strength analysis via `zxcvbn`
- Save & retrieve history in encrypted file
- ASCII art banner (pyfiglet)

## Project Structure

The application is built using object-oriented programming principles with two main classes:
- `PasswordGenerator`: Handles password generation and strength analysis
- `PasswordStorage`: Manages password storage, retrieval, and encryption

## Input/Output Operations

The application implements multiple types of input/output:
- Command-line interface for user interaction
- File I/O for password storage (encrypted JSON)
- Terminal output with colored ASCII art and formatted results

## Setup / Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourname/password_generator.git
   cd password_generator
   ```

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
| `--strength`         | (If `zxcvbn` is installed) Print entropy score and "weak/ok/strong" note | Off        |
| `-n`, `--name TEXT`  | Assign a human-readable name/label to the password (e.g. "work email")   | None       |
| `--search TEXT`      | Lookup and display all saved entries whose name or password contains TEXT| None       |

## Third-Party Packages

| Package  | Version | License    | Impact                          |
| -------- | ------- | ---------- | ------------------------------- |
| pyfiglet | ^0.8.1  | MIT        | Permissive, minimal obligations |
| zxcvbn   | ^4.4.28 | BSD-3      | Permissive                      |

### License Information

- **MIT License** (pyfiglet): Permits commercial use, modification, distribution, and private use. Requires license and copyright notice.
- **BSD-3** (zxcvbn): Permits commercial use, modification, distribution, and private use. Requires license and copyright notice.

All licenses are permissive and suitable for both personal and commercial use. The main obligations are maintaining copyright notices and license information in the code.

## Error Handling

The application implements comprehensive error handling:
- Invalid user input validation
- File I/O error handling
- Password generation constraints
- Graceful fallbacks for missing dependencies