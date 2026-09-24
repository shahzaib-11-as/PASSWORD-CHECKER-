import getpass 
import re 
import string 
from pathlib import Path 
from colorama import init, Fore, Back, Style 

init(autoreset=True) 

CYAN = Fore.CYAN 
BRIGHT_CYAN = Fore.LIGHTCYAN_EX 
GREEN = Fore.GREEN 
BRIGHT_GREEN = Fore.LIGHTGREEN_EX 
YELLOW = Fore.YELLOW 
BRIGHT_YELLOW = Fore.LIGHTYELLOW_EX 
RED = Fore.RED 
BRIGHT_RED = Fore.LIGHTRED_EX 
BLUE = Fore.BLUE 
BRIGHT_BLUE = Fore.LIGHTBLUE_EX 
MAGENTA = Fore.MAGENTA 
WHITE = Fore.WHITE 
BRIGHT_WHITE = Fore.LIGHTWHITE_EX 
DIM = Style.DIM 
RESET = Style.RESET_ALL 
BOLD = Style.BRIGHT 

def display_logo():
    logo = f"""
{CYAN}
       ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗
       ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
       ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
       ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
       ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
       ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝
{GREEN}
                    ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
                   ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
                   ██║     ███████║█████╗  ██║     █████╔╝
                   ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗
                   ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
                    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
{RESET}
"""
    print(logo)

DATASET_FILE = Path(__file__).parent / "data" / "common_passwords.txt" 

def load_common_passwords(): 
    """Load common passwords from the dataset.""" 
 
    if not DATASET_FILE.exists(): 
        print( 
            f"{YELLOW}Warning:{RESET} " 
            f"common_passwords.txt not found." 
        ) 
        return set() 
    with open(DATASET_FILE, "r", encoding="utf-8") as file: 
        return { 
            line.strip().lower() 
            for line in file 
            if line.strip() 
        } 

COMMON_PASSWORDS = load_common_passwords() 
 
def print_banner(): 
    print() 
    print( 
        f"{BRIGHT_CYAN}{BOLD}" 
        "==========================================================" 
    ) 
    print( 
        f"{BRIGHT_CYAN}{BOLD}" 
        "          PERSONAL CYBERSECURITY AUDIT TOOL" 
    ) 
    print( 
        f"{BRIGHT_CYAN}{BOLD}" 
        "              PASSWORD SECURITY CHECKER" 
    ) 
    print( 
        f"{BRIGHT_CYAN}{BOLD}" 
        "==========================================================" 
    ) 
    print( 
        f"{DIM}{WHITE}" 
        "        Analyze password strength and predictability" 
    ) 
    print( 
        f"{CYAN}" 
        "----------------------------------------------------------" 
    ) 
    print() 

def print_section(title): 
    print() 
    print( 
        f"{BRIGHT_CYAN}{BOLD}" 
        f"[ {title} ]" 
    ) 
    print( 
        f"{CYAN}" 
        "----------------------------------------------------------" 
    ) 

def yes_no(value): 
 
    if value: 
        return f"{BRIGHT_GREEN}{BOLD}YES{RESET}" 
 
    return f"{BRIGHT_RED}{BOLD}NO{RESET}" 

def risk_color(risk): 
 
    if risk == "LOW": 
        return f"{BRIGHT_GREEN}{BOLD}{risk}{RESET}" 
 
    elif risk == "MEDIUM": 
        return f"{BRIGHT_YELLOW}{BOLD}{risk}{RESET}" 
 
    else: 
        return f"{BRIGHT_RED}{BOLD}{risk}{RESET}" 

def score_color(score): 
 
    if score >= 80: 
        return f"{BRIGHT_GREEN}{BOLD}{score}/100{RESET}" 
 
    elif score >= 60: 
        return f"{BRIGHT_YELLOW}{BOLD}{score}/100{RESET}" 
 
    else: 
        return f"{BRIGHT_RED}{BOLD}{score}/100{RESET}" 

def check_predictability(password): 
 
    problems = [] 
    lower_password = password.lower() 
 
    number_sequences = [ 
        "0123", 
        "1234", 
        "2345", 
        "3456", 
        "4567", 
        "5678", 
        "6789" 
    ] 
 
    for sequence in number_sequences: 
 
        if sequence in lower_password: 
 
            problems.append( 
                f"Sequential number pattern detected: {sequence}" 
            ) 
            break 
 
    letter_sequences = [ 
        "abcd", 
        "bcde", 
        "cdef", 
        "defg", 
        "efgh", 
        "fghi", 
        "ghij", 
        "wxyz" 
    ] 
    for sequence in letter_sequences: 
 
        if sequence in lower_password: 
 
            problems.append( 
                f"Sequential letter pattern detected: {sequence}" 
            ) 
 
            break 
 
    if re.search(r"(.)\1\1", password): 
 
        problems.append( 
            "Repeated character pattern detected." 
        ) 
    keyboard_patterns = [ 
        "qwerty", 
        "asdf", 
        "zxcv", 
        "qaz", 
        "wsx" 
    ] 
 
    for pattern in keyboard_patterns: 
 
        if pattern in lower_password: 
 
            problems.append( 
                f"Keyboard pattern detected: {pattern}" 
            ) 
 
            break 
 
    common_words = [ 
        "password", 
        "admin", 
        "welcome", 
        "login", 
        "user", 
        "letmein", 
        "monkey", 
        "dragon" 
    ] 
    for word in common_words: 
 
        if word in lower_password: 
 
            problems.append( 
                f"Predictable word detected: {word}" 
            ) 
 
            break 
 
    return problems 
 
def check_password(password): 
 
    feedback = [] 
 
    length = len(password) 
 
    has_lowercase = any( 
        char.islower() for char in password 
    ) 
 
    has_uppercase = any( 
        char.isupper() for char in password 
    ) 
 
    has_number = any( 
        char.isdigit() for char in password 
    ) 
 
    has_special = any( 
        char in string.punctuation 
        for char in password 
    ) 
 
    if length >= 16: 
 
        length_score = 40 
 
    elif length >= 12: 
 
        length_score = 30 
 
        feedback.append( 
            "Use at least 16 characters for stronger protection." 
        ) 
 
    elif length >= 8: 
 
        length_score = 20 
 
        feedback.append( 
            "Use at least 12 characters; 16 or more is recommended." 
        ) 
 
    else: 
 
        length_score = 10 
 
        feedback.append( 
            "Password is too short. Use at least 12 characters." 
        ) 
    variety_score = 0 
    if has_lowercase: 
        variety_score += 10 
    else: 
        feedback.append( 
            "Add lowercase letters." 
        ) 
    if has_uppercase: 
        variety_score += 10 
    else: 
        feedback.append( 
            "Add uppercase letters." 
        ) 
    if has_number: 
        variety_score += 10 
    else: 
        feedback.append( 
            "Add numbers." 
        ) 
    if has_special: 
        variety_score += 10 
    else: 
        feedback.append( 
            "Add special characters such as !, @, #, or $." 
        ) 
 
    is_common = password.lower() in COMMON_PASSWORDS 
    if is_common: 
        common_score = 0 
        feedback.append( 
            "This password appears in the common-password " 
            "dataset. Replace it with a unique password." 
        ) 
    else: 
        common_score = 10 
    predictability_problems = check_predictability( 
        password 
    ) 
 
    predictability_score = 10 
 
    if predictability_problems: 
 
        penalty = len(predictability_problems) * 5 
 
        predictability_score = max( 
            0, 
            predictability_score - penalty 
        ) 
 
        for problem in predictability_problems: 
 
            if "Sequential number" in problem: 
 
                feedback.append( 
                    "Avoid sequential numbers such as 1234." 
                ) 
 
            elif "Sequential letter" in problem: 
 
                feedback.append( 
                    "Avoid sequential letters such as abcd." 
                ) 
 
            elif "Repeated character" in problem: 
 
                feedback.append( 
                    "Avoid repeating the same character " 
                    "three or more times." 
                ) 
 
            elif "Keyboard pattern" in problem: 
 
                feedback.append( 
                    "Avoid predictable keyboard patterns." 
                ) 
 
            elif "Predictable word" in problem: 
 
                feedback.append( 
                    "Avoid common or predictable words." 
                ) 
 
    score = ( 
        length_score 
        + variety_score 
        + common_score 
        + predictability_score 
    ) 
 
    score = max(0, min(score, 100)) 
 
    if score >= 80: 
 
        risk = "LOW" 
 
    elif score >= 60: 
 
        risk = "MEDIUM" 
 
    else: 
 
        risk = "HIGH" 
 
    # Common password = HIGH risk 
 
    if is_common: 
 
        risk = "HIGH" 
 
    return { 
        "score": score, 
        "risk": risk, 
        "length": length, 
        "lowercase": has_lowercase, 
        "uppercase": has_uppercase, 
        "number": has_number, 
        "special": has_special, 
        "common": is_common, 
        "predictability": predictability_problems, 
        "feedback": feedback 
    } 

def main(): 
 
    display_logo()
    print_banner() 
 
    print( 
        f"{BRIGHT_WHITE}" 
        "Enter a password to perform a local security assessment." 
    ) 
 
    print( 
        f"{DIM}{WHITE}" 
        "Your password will not be displayed while typing." 
    ) 
 
    print() 
 
    password = getpass.getpass( 
        f"{BRIGHT_CYAN}Password: {RESET}" 
    ) 
 
    if not password: 
 
        print() 
 
        print( 
            f"{BRIGHT_RED}{BOLD}" 
            "ERROR: Password cannot be empty." 
            f"{RESET}" 
        ) 
 
        return 
 
    result = check_password(password) 
 
    print_section("PASSWORD SECURITY ASSESSMENT") 
 
    print( 
        f"{WHITE}Password length          : " 
        f"{BRIGHT_WHITE}{result['length']}" 
    ) 
 
    print( 
        f"{WHITE}Lowercase letters        : " 
        f"{yes_no(result['lowercase'])}" 
    ) 
 
    print( 
        f"{WHITE}Uppercase letters        : " 
        f"{yes_no(result['uppercase'])}" 
    ) 
 
    print( 
        f"{WHITE}Numbers                  : " 
        f"{yes_no(result['number'])}" 
    ) 
 
    print( 
        f"{WHITE}Special characters       : " 
        f"{yes_no(result['special'])}" 
    ) 
 
    print( 
        f"{WHITE}Common password          : " 
        f"{yes_no(result['common'])}" 
    ) 
 
    print( 
        f"{WHITE}Predictability issues    : " 
        f"{BRIGHT_YELLOW}{len(result['predictability'])}{RESET}" 
    ) 
 
    print_section("SECURITY RESULT") 
 
    print( 
        f"{WHITE}Security Score           : " 
        f"{score_color(result['score'])}" 
    ) 
 
    print( 
        f"{WHITE}Risk Level               : " 
        f"{risk_color(result['risk'])}" 
    ) 
 
    if result["predictability"]: 
 
        print_section("PREDICTABILITY FINDINGS") 
 
        for problem in result["predictability"]: 
 
            print( 
                f"{BRIGHT_RED}  [!] {WHITE}{problem}" 
            ) 
 
    print_section("ACTIONABLE FEEDBACK") 
 
    if result["feedback"]: 
 
        for item in result["feedback"]: 
 
            print( 
                f"{BRIGHT_YELLOW}  [+] " 
                f"{WHITE}{item}" 
            ) 
 
    else: 
 
        print( 
            f"{BRIGHT_GREEN}" 
            "  [OK] No major improvements detected." 
        ) 
 
    print() 
 
    print( 
        f"{CYAN}" 
        "----------------------------------------------------------" 
    ) 
 
    print( 
        f"{DIM}{WHITE}" 
        "  Privacy: Password is processed locally and is not saved." 
    ) 
 
    print( 
        f"{CYAN}" 
        "----------------------------------------------------------" 
    ) 
 
    print() 
 
    print( 
        f"{BRIGHT_CYAN}{BOLD}" 
        "             SECURITY CHECK COMPLETE" 
    ) 
 
    print() 
 
if __name__ == "__main__": 
    main()