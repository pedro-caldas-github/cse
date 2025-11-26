LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Check if word exists in file with optional case sensitivity"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if line_word == word:
                        return True
                else:
                    if line_word.lower() == word.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return False

def word_has_character(word, character_list):
    """Check if any character in word exists in character_list"""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Calculate complexity score based on character types used"""
    complexity_score = 0
    if word_has_character(word, LOWER):
        complexity_score += 1
    if word_has_character(word, UPPER):
        complexity_score += 1
    if word_has_character(word, DIGITS):
        complexity_score += 1
    if word_has_character(word, SPECIAL):
        complexity_score += 1
    return complexity_score

def password_strength(password, min_length=10, strong_length=16):
    """Evaluate password strength and return score 0-5"""
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def main():
    """Main user interface for password strength checking"""
    print("=== Password Strength Checker ===")
    print("Enter a password to check its strength (enter 'q' or 'Q' to quit)")
    
    while True:
        password = input("\nEnter password: ")
        
        if password.lower() == "q":
            print("Thank you for using the Password Strength Checker!")
            break
        
        strength = password_strength(password)
        print(f"Password strength: {strength}/5")

if __name__ == "__main__":
    main()