"""
Personal Info Summary Assistant

A command-line tool that collects personal details from users and displays
customized summaries. Features include data export, rating system, and
interactive questions.

Author: Kennedy Adosibe
Version: 2.0
"""

import random
import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class Colors:
    """ANSI color codes for terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_user_data() -> Dict[str, str]:
    """
    Collect user information through interactive questions.
    
    Returns:
        Dict[str, str]: Dictionary containing user responses.
    """
    required_questions = [
        ("name", "What is your name? "),
        ("age", "How old are you? ")
    ]

    optional_questions = [
        ("color", "What is your favorite color? "),
        ("food", "What is your favorite food? "),
        ("city", "Which city do you live in? "),
        ("school", "Which SHS did you attend? "),
        ("team", "What is your favorite soccer team? "),
        ("hobby", "What is your favorite hobby? "),
        ("music", "What is your favorite music genre? "),
        ("movie", "What is your favorite movie? ")
    ]

    # Randomly select 3-5 optional questions for variety
    selected_optional = random.sample(optional_questions, k=random.randint(3, 5))

    all_questions = required_questions + selected_optional
    responses = {}

    print(f"\n{Colors.HEADER}{Colors.BOLD}=== Personal Information Assistant ==={Colors.ENDC}\n")
    
    for key, prompt in all_questions:
        while True:
            response = input(f"{Colors.OKCYAN}{prompt}{Colors.ENDC}").strip()
            
            # Validate age input
            if key == "age":
                try:
                    age = int(response)
                    if age < 0 or age > 150:
                        print(f"{Colors.WARNING}Please enter a valid age (0-150).{Colors.ENDC}")
                        continue
                    responses[key] = response
                    break
                except ValueError:
                    print(f"{Colors.WARNING}Please enter a valid number for age.{Colors.ENDC}")
                    continue
            
            # Validate non-empty responses
            if response:
                responses[key] = response
                break
            else:
                print(f"{Colors.WARNING}This field cannot be empty. Please try again.{Colors.ENDC}")

    return responses


def display_summary(responses: Dict[str, str]) -> None:
    """
    Display a formatted summary of user information.
    
    Args:
        responses: Dictionary containing user data.
    """
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}--- Personalized Summary ---{Colors.ENDC}")
    print(f"{Colors.OKBLUE}Hello, {responses.get('name', 'Friend')}!{Colors.ENDC}")

    summary_parts = []
    
    if 'age' in responses:
        summary_parts.append(f"You are {responses['age']} years old")
    if 'color' in responses:
        summary_parts.append(f"love the color {responses['color']}")
    if 'food' in responses:
        summary_parts.append(f"enjoy eating {responses['food']}")
    
    if summary_parts:
        print(f"{', '.join(summary_parts[:-1])}{', and ' if len(summary_parts) > 1 else ''}{summary_parts[-1] if summary_parts else ''}.")
    
    if 'city' in responses:
        print(f"Life must be awesome in {responses['city']}!")
    if 'school' in responses:
        print(f"You went to {responses['school']} SHS.")
    if 'team' in responses:
        print(f"Go {responses['team']}! ⚽")
    if 'hobby' in responses:
        print(f"You love spending time on {responses['hobby']}.")
    if 'music' in responses:
        print(f"You enjoy listening to {responses['music']} music.")
    if 'movie' in responses:
        print(f"Your favorite movie is {responses['movie']}.")


def save_to_file(responses: Dict[str, str], rating: int) -> None:
    """
    Save user summary to a text file.
    
    Args:
        responses: Dictionary containing user data.
        rating: User rating (1-5).
    """
    filename = f"{responses.get('name', 'user').replace(' ', '_')}.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 40 + "\n")
        f.write("User Summary\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated: {timestamp}\n\n")
        for key, value in responses.items():
            f.write(f"{key.capitalize()}: {value}\n")
        f.write(f"\nRating: {'⭐' * rating} ({rating}/5)\n")
        f.write("=" * 40 + "\n")
    
    print(f"{Colors.OKGREEN}Summary saved to {filename}{Colors.ENDC}")


def save_to_json(responses: Dict[str, str], rating: int) -> None:
    """
    Save user summary to a JSON file.
    
    Args:
        responses: Dictionary containing user data.
        rating: User rating (1-5).
    """
    filename = f"{responses.get('name', 'user').replace(' ', '_')}.json"
    data = {
        "timestamp": datetime.now().isoformat(),
        "user_data": responses,
        "rating": rating
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"{Colors.OKGREEN}Data saved to {filename}{Colors.ENDC}")


def view_saved_summaries() -> None:
    """Display a list of all saved user summaries."""
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'README.txt']
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    
    if not txt_files and not json_files:
        print(f"{Colors.WARNING}No saved summaries found.{Colors.ENDC}")
        return
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== Saved Summaries ==={Colors.ENDC}")
    
    if txt_files:
        print(f"\n{Colors.OKCYAN}Text Files:{Colors.ENDC}")
        for i, filename in enumerate(txt_files, 1):
            print(f"  {i}. {filename}")
    
    if json_files:
        print(f"\n{Colors.OKCYAN}JSON Files:{Colors.ENDC}")
        for i, filename in enumerate(json_files, 1):
            print(f"  {i}. {filename}")


def display_statistics() -> None:
    """Display statistics about all saved user data."""
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    
    if not json_files:
        print(f"{Colors.WARNING}No data available for statistics.{Colors.ENDC}")
        return
    
    total_users = len(json_files)
    ratings = []
    ages = []
    
    for filename in json_files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'rating' in data:
                    ratings.append(data['rating'])
                if 'user_data' in data and 'age' in data['user_data']:
                    try:
                        ages.append(int(data['user_data']['age']))
                    except ValueError:
                        pass
        except (json.JSONDecodeError, IOError):
            continue
    
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== Statistics ==={Colors.ENDC}")
    print(f"{Colors.OKBLUE}Total Users: {total_users}{Colors.ENDC}")
    
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        print(f"{Colors.OKBLUE}Average Rating: {avg_rating:.2f}/5 {'⭐' * int(round(avg_rating))}{Colors.ENDC}")
        print(f"{Colors.OKBLUE}Total Ratings: {len(ratings)}{Colors.ENDC}")
    
    if ages:
        avg_age = sum(ages) / len(ages)
        print(f"{Colors.OKBLUE}Average Age: {avg_age:.1f} years{Colors.ENDC}")


def get_rating() -> int:
    """
    Get user rating with validation.
    
    Returns:
        int: Rating value between 1 and 5.
    """
    while True:
        try:
            rating = int(input(f"{Colors.OKCYAN}Please rate this assistant (1 to 5): {Colors.ENDC}"))
            if 1 <= rating <= 5:
                return rating
            else:
                print(f"{Colors.WARNING}Rating must be between 1 and 5.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.WARNING}Please enter a valid number.{Colors.ENDC}")


def show_menu() -> str:
    """
    Display main menu and get user choice.
    
    Returns:
        str: User's menu choice.
    """
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== Main Menu ==={Colors.ENDC}")
    print(f"{Colors.OKCYAN}1. Start new session{Colors.ENDC}")
    print(f"{Colors.OKCYAN}2. View saved summaries{Colors.ENDC}")
    print(f"{Colors.OKCYAN}3. View statistics{Colors.ENDC}")
    print(f"{Colors.OKCYAN}4. Exit{Colors.ENDC}")
    
    choice = input(f"\n{Colors.OKCYAN}Enter your choice (1-4): {Colors.ENDC}").strip()
    return choice


def main() -> None:
    """Main application loop."""
    print(f"{Colors.BOLD}{Colors.HEADER}")
    print("╔═══════════════════════════════════════╗")
    print("║  Personal Info Summary Assistant v2.0 ║")
    print("╔═══════════════════════════════════════╗")
    print(f"{Colors.ENDC}")
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            # Start new session
            responses = get_user_data()
            display_summary(responses)

            save = input(f"\n{Colors.OKCYAN}Do you want to save this summary? (yes/no): {Colors.ENDC}").strip().lower()
            if save == "yes":
                rating = get_rating()
                save_to_file(responses, rating)
                
                # Also offer JSON export
                json_export = input(f"{Colors.OKCYAN}Would you like to export to JSON? (yes/no): {Colors.ENDC}").strip().lower()
                if json_export == "yes":
                    save_to_json(responses, rating)
        
        elif choice == '2':
            # View saved summaries
            view_saved_summaries()
        
        elif choice == '3':
            # View statistics
            display_statistics()
        
        elif choice == '4':
            # Exit
            print(f"\n{Colors.OKGREEN}Thank you for using Personal Info Summary Assistant!{Colors.ENDC}")
            print(f"{Colors.OKGREEN}Goodbye! 👋{Colors.ENDC}\n")
            break
        
        else:
            print(f"{Colors.WARNING}Invalid choice. Please select 1-4.{Colors.ENDC}")


if __name__ == "__main__":
    main()
