import random
import string
from zxcvbn import zxcvbn
class PasswordGenerator:
    def __init__(self):
      # Define character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
    def generate_password(self, length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
      """Generate a random password with specified characteristics."""
      
      lowercase = self.lowercase if use_lower else ""
      uppercase = self.uppercase if use_upper else ""
      digits = self.digits if use_digits else ""
      symbols = self.symbols if use_symbols else ""
    
      all_chars = lowercase + uppercase + digits + symbols # Combine all sets
    
      if all_chars == "": # Ensure at least one character set is selected
        raise ValueError("At least one character set must be selected")
    
      # Generate password
      password = ''.join(random.choice(all_chars) for _ in range(length))
      return password
    
    def check_strength(self, password):
        return zxcvbn(password) # checks the strength of the password