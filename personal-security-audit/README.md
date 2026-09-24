# Personal Password Security Checker

A Python-based password security assessment tool developed as part of a personal cybersecurity audit internship project.

The tool evaluates a password locally and provides a security score, risk level, and actionable recommendations.

## Features

The password checker evaluates:

* Password length
* Lowercase characters
* Uppercase characters
* Numbers
* Special characters
* Common-password exposure
* Sequential patterns
* Repeated characters
* Keyboard patterns
* Predictable words
* Overall security score
* Risk classification
* Actionable security recommendations

## Technologies

* Python 3
* Python Standard Library
* `getpass`
* `re`
* `string`
* `pathlib`

No external Python packages are required.

## Project Structure

```text
personal-security-audit/
│
├── password_checker.py
│
├── data/
│   └── common_passwords.txt
│
└── README.md
```

## How to Run

Open Command Prompt and navigate to the project directory:

```cmd
cd %USERPROFILE%\Desktop\personal-security-audit
```

Run the program:

```cmd
python password_checker.py
```

The program will ask:

```text
Enter a password to test:
```

The password is entered using Python's `getpass` module, so it is not displayed on the screen while being typed.

## Important Security Note

Do not enter real passwords that are currently used for important accounts during testing.

Use deliberately created test passwords.

The program processes the password locally and does not send the password to an external service.

## Scoring System

The tool uses a 100-point scoring model.

### 1. Password Length — 40 Points

| Length                  | Points |
| ----------------------- | -----: |
| 16 or more characters   |     40 |
| 12–15 characters        |     30 |
| 8–11 characters         |     20 |
| Fewer than 8 characters |     10 |

Longer passwords generally provide more possible combinations and are therefore an important part of password security.

### 2. Character Variety — 40 Points

The checker awards:

| Character Type     | Points |
| ------------------ | -----: |
| Lowercase letters  |     10 |
| Uppercase letters  |     10 |
| Numbers            |     10 |
| Special characters |     10 |

Maximum character-variety score:

**40 points**

Character variety is considered together with password length and predictability rather than being used as the only measure of password strength.

### 3. Common Password Check — 10 Points

If the password is not found in the local common-password dataset:

**+10 points**

If the password is found:

**0 points**

A password found in the common-password dataset is also classified as:

**HIGH risk**

regardless of its numerical score.

The current dataset is an educational project dataset and should not be considered a complete list of all commonly used or compromised passwords.

### 4. Predictability — 10 Points

The checker begins with:

**10 points**

It can identify patterns including:

* `1234`
* `abcd`
* Repeated characters such as `!!!!!!`
* Keyboard patterns such as `qwerty`
* Predictable words such as `password`
* Other simple patterns implemented in the Python program

Each detected predictability issue removes 5 points, up to the available 10 predictability points.

Therefore:

```text
0 issues → 10 points
1 issue  → 5 points
2+ issues → 0 points
```

### 5. Final Score

The maximum possible score is:

```text
Length             = 40
Character variety  = 40
Common password    = 10
Predictability     = 10
--------------------------------
Maximum            = 100
```

The final score is restricted to the range:

```text
0–100
```

## Risk Classification

The numerical score is converted into three risk levels:

|  Score | Risk   |
| -----: | ------ |
| 80–100 | LOW    |
|  60–79 | MEDIUM |
|   0–59 | HIGH   |

There is one additional rule:

> A password found in the common-password dataset is always classified as HIGH risk.

This prevents a commonly used password from receiving a low-risk classification simply because it contains uppercase letters, numbers, or special characters.

## Example

A test password such as:

```text
T7!qL9@vR2#xP8
```

contains:

* Lowercase letters
* Uppercase letters
* Numbers
* Special characters
* 14 characters
* No detected common-password match
* No detected sequential pattern

The checker can therefore assign it a substantially stronger score than predictable test passwords.

A password such as:

```text
Abcd1234!!!!!!
```

contains multiple character types, but it also contains:

* A sequential letter pattern
* A sequential number pattern
* Repeated characters

The checker therefore reduces its predictability score and provides recommendations.

## Actionable Feedback

The program does not only provide a numerical score.

It provides specific recommendations such as:

```text
- Add uppercase letters.
- Add numbers.
- Add special characters.
- Use at least 16 characters for stronger protection.
- Avoid sequential numbers such as 1234.
- Avoid sequential letters such as abcd.
- Avoid repeating the same character three or more times.
- Avoid common or predictable words.
```

This makes the assessment useful to the person performing the security audit.

## Security Design

The password is collected using:

```python
getpass.getpass()
```

This prevents the password from being displayed on the terminal during input.

The program does not intentionally:

* Save passwords to a file
* Print the entered password
* Send passwords to a server
* Store passwords in a database
* Upload passwords to GitHub

The common-password dataset contains password strings for comparison, but it does not contain passwords supplied by the user during program execution.

## Limitations

This project is an educational cybersecurity audit tool and should not be considered a complete enterprise password-strength assessment system.

Limitations include:

* The common-password dataset is limited.
* Pattern detection is rule-based.
* The scoring system is a project-defined model rather than an industry-standard password-strength score.
* The checker does not perform a real password-cracking test.
* The checker does not determine whether a password has actually appeared in a breach.
* A password can receive a high score while still being unsuitable if it contains information that an attacker could know about the user.

For breach exposure, the internship project will use a separate process rather than sending passwords to a breach-checking service.

## Future Improvements

Possible future improvements include:

* Using a larger reputable common-password dataset
* Adding additional keyboard-pattern detection
* Detecting dates and years
* Detecting names and other predictable personal information
* Improving repeated-pattern detection
* Adding a graphical user interface
* Adding automated test cases
* Adding unit testing
* Integrating a password-strength estimation library
* Adding secure breach-exposure checking for email addresses

## Internship Task Status

### Task 1 — Password Strength Checker

**Status: Completed**

Implemented:

* [x] Password length checking
* [x] Character variety checking
* [x] Common-password detection
* [x] Predictability detection
* [x] Actionable feedback
* [x] Security score
* [x] Risk classification
* [x] Local password processing
* [x] Project documentation

## Responsible Use

This tool is intended for educational and authorized personal security assessment.

Only test passwords that you are authorized to test, and never collect, store, or publish another person's credentials.
