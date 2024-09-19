from datetime import date
import inflect
import sys

p = inflect.engine()

def get_user_dob():
    try:
        dob_input = input("Please enter your date of birth as YYYY-MM-DD: ")
        dob = date.fromisoformat(dob_input)
    except ValueError:
        print("Invalid date format. Exiting the program.")
        sys.exit(1)
    return dob

def calculate_minutes_lived(dob):
    today = date.today()
    delta = today - dob
    minutes = delta.days * 24 * 60
    return minutes

def convert_minutes_to_words(minutes):
    return p.number_to_words(minutes, andword='').capitalize()

def main():
    dob = get_user_dob()
    minutes = calculate_minutes_lived(dob)
    minutes_in_words = convert_minutes_to_words(minutes)
    print(f"{minutes_in_words} minutes")

if __name__ == '__main__':
    main()