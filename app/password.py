import random
import string
import hashlib

class Password:
    def generate_password(self, length):
        """Generate a random password of a given length"""
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for i in range(length))
        return password
    
    def encrypt_password(self, password):
        # Convert the password to bytes before hashing
        password_bytes = password.encode('utf-8')
        # Use the SHA-256 hash function to generate a 64-character hash
        hashed_password = hashlib.sha256(password_bytes).hexdigest()
        return hashed_password
    
    def verify_the_password(self, hashed_password, password):
         # Hash the entered password using the same algorithm and compare to the stored hash
        return self.encrypt_password(password) == hashed_password