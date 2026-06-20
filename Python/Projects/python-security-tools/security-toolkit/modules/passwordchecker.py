from getpass import getpass

COMMON_PASSWORDS = [
    "password",
    "123456",
    "qwerty",
    "admin",
    "letmein",
    "welcome"
]

class PasswordAnalyzer:

    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 12
    
    def check_uppercase(self):

        for char in self.password:

            if char.isupper():
                return True
        
        return False
    
    def check_lowercase(self):

        for char in self.password:

            if char.islower():
                return True
        
        return False
    
    def check_numbers(self):

        for char in self.password:

            if char.isdigit():
                return True
            
        return False
    
    def check_special(self):

        specials = "!@#$%^&*()_+-=[]{}"

        for char in self.password:

            if char in specials:
                return True
        
        return False
    
    def is_common_password(self):

        return (
            self.password.lower()
            in COMMON_PASSWORDS
        )
    
    def score_password(self):

        score = 0
        feedback = []

        if self.check_length():
            score += 1
        else:
            feedback.append(
                "Use at least 12 characters"
            )

        if self.check_uppercase():
            score += 1
        else:
            feedback.append(
                "Use at least one uppercase character"
            )

        if self.check_lowercase():
            score += 1
        else:
            feedback.append(
                "Use at least one lowercase character"
            )
        
        if self.check_numbers():
            score += 1
        else:
            feedback.append(
                "Use at least one number"
            )

        if self.check_special():
            score += 1
        else:
            feedback.append(
                "Use at least one special character"
            )
        
        if self.is_common_password():
            score -= 2
            feedback.append(
                "Your password is a common password"
            )
        
        return score, feedback
    
    def classify_strength(self, score):
        if score <= 2:
            return "Weak"
        
        elif score == 3:
            return "Medium"
        
        elif score == 4:
            return "Strong"
        
        else:
            return "Very Strong"
        
    def generate_report(self, strength, feedback):

        report = ""

        report += "PASSWORD ANALYSIS REPORT\n"
        report += "=" * 40 + "\n\n"

        report += f"Strength: {strength}\n\n"

        report += "Recommendations:\n"

        if not feedback:
                report += "- No recommendations. Excellent password.\n"
        else:
            for item in feedback:
                report += f"- {item}\n"

        return report
    
    def save_report(self, report):

        with open(
            "reports/password_report.txt", "w") as file:
            
            file.write(report)
    

def run_password_check():
    
    password = getpass("Enter password: ")
    
    analyzer = PasswordAnalyzer(password)
    
    score, feedback = analyzer.score_password()
    
    strength = analyzer.classify_strength(score)
    
    report = analyzer.generate_report(strength, feedback)
    
    return report