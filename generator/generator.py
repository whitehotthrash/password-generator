#!/usr/bin/env python3

import string
import random
from zxcvbn import zxcvbn

class PasswordGenerator:
    """
    A simple password generator that can:
    - Create random passwords
    - Check how strong they are
    """
    
    def __init__(self):
        # These are the characters we can use to make passwords
        self.lowercase = string.ascii_lowercase  # a-z
        self.uppercase = string.ascii_uppercase  # A-Z
        self.digits = string.digits             # 0-9
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Special characters

    def generate(self, length=12, use_lower=True, use_upper=True, 
                use_digits=True, use_symbols=True):
        """
        Make a new random password.
        
        Args:
            length: How long the password should be
            use_lower: Should we use lowercase letters? (a-z)
            use_upper: Should we use uppercase letters? (A-Z)
            use_digits: Should we use numbers? (0-9)
            use_symbols: Should we use special characters? (!@#$ etc)
        """
        # TODO: You need to:
        # 1. Create a list of all the characters we can use
        # 2. Use random.choice() to pick random characters
        # 3. Join them together to make the password
        pass

    def analyze_strength(self, password):
        """
        Check how strong a password is.
        
        Args:
            password: The password to check
        """
        # TODO: You need to:
        # 1. Use zxcvbn to check the password
        # 2. Return how strong it is (weak/ok/strong)
        pass
