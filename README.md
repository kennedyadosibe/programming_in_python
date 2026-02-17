# Personal Info Summary Assistant v2.0

An enhanced command-line tool that collects personal details from users and displays customized summaries. This tool demonstrates modern Python programming principles with a focus on user experience, data persistence, and code quality.

## 🎯 Features

### Core Functionality
- **Interactive Questionnaire**: Collects user information through a series of questions
  - Required fields: Name, Age
  - Optional fields (randomly selected): Favorite color, food, city, school, soccer team, hobby, music genre, and favorite movie
- **Smart Input Validation**: 
  - Age validation (numeric, 0-150 range)
  - Non-empty field validation
  - Error handling with helpful feedback
- **Colorful Terminal Output**: Uses ANSI color codes for better visual experience
- **Personalized Summaries**: Displays customized, context-aware summaries

### Data Management
- **Multiple Export Formats**:
  - Text files (.txt) with formatted output
  - JSON files (.json) with structured data
- **View Saved Summaries**: Browse all previously saved user profiles
- **Statistics Dashboard**: View aggregated statistics including:
  - Total users
  - Average rating
  - Average age

### User Experience
- **Menu-Driven Interface**: Easy navigation with numbered options
- **Rating System**: 1-5 star rating with visual feedback
- **Randomized Questions**: Different experience each session
- **Professional UI**: Formatted headers, colors, and emoji support

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/kennedyadosibe/programming_in_python.git
cd programming_in_python
```

2. Ensure you have Python 3.7 or higher:
```bash
python --version
```

3. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

No external dependencies are required! The application uses only Python standard library.

## 📖 Usage

### Running the Application

Run the improved version:
```bash
python personal_assistance.py
```

Or run the original version:
```bash
python "personal assistance.py"
```

### Example Session

```
╔═══════════════════════════════════════╗
║  Personal Info Summary Assistant v2.0 ║
╔═══════════════════════════════════════╗

=== Main Menu ===
1. Start new session
2. View saved summaries
3. View statistics
4. Exit

Enter your choice (1-4): 1

=== Personal Information Assistant ===

What is your name? John Doe
How old are you? 25
What is your favorite color? Blue
What is your favorite food? Pizza
What is your favorite hobby? Reading

--- Personalized Summary ---
Hello, John Doe!
You are 25 years old, love the color Blue, and enjoy eating Pizza.
You love spending time on Reading.

Do you want to save this summary? (yes/no): yes
Please rate this assistant (1 to 5): 5
Summary saved to John_Doe.txt
Would you like to export to JSON? (yes/no): yes
Data saved to John_Doe.json
```

## 🧪 Testing

Run the test suite:
```bash
python -m unittest test_personal_assistance.py
```

Run with verbose output:
```bash
python -m unittest test_personal_assistance.py -v
```

## 📁 Project Structure

```
programming_in_python/
├── README.md                       # This file
├── personal_assistance.py          # Enhanced version (v2.0)
├── personal assistance.py          # Original version
├── test_personal_assistance.py     # Comprehensive test suite
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── [user-generated files]          # *.txt and *.json files (not tracked)
```

## 🎨 What's New in v2.0

### Code Quality Improvements
- ✅ Fixed indentation errors
- ✅ Added comprehensive docstrings
- ✅ Added type hints for better code clarity
- ✅ Improved error handling
- ✅ Better code organization with proper function separation
- ✅ Module-level documentation

### New Features
- ✅ Menu-driven interface
- ✅ JSON export functionality
- ✅ View saved summaries feature
- ✅ Statistics dashboard
- ✅ Colorful terminal output (ANSI colors)
- ✅ Enhanced input validation
- ✅ More question variety (hobbies, music, movies)
- ✅ Timestamp tracking
- ✅ Professional formatting

### Testing & Documentation
- ✅ Comprehensive unit test suite (15 tests)
- ✅ Integration tests
- ✅ Updated README with examples
- ✅ requirements.txt file
- ✅ .gitignore to exclude user-generated files

## 🛠️ Technical Details

### Programming Concepts Demonstrated
- **User Input & Validation**: Robust input handling with validation
- **String Formatting**: F-strings and formatted output
- **File I/O**: Reading/writing both text and JSON files
- **Control Flow**: Loops, conditionals, menu systems
- **Error Handling**: Try-except blocks with user-friendly messages
- **Randomization**: Random question selection
- **Type Hints**: Modern Python type annotations
- **Object-Oriented Concepts**: Classes for organization (Colors)
- **Data Structures**: Dictionaries, lists, tuples
- **Standard Library**: datetime, json, os, typing modules

### Code Style
- Follows PEP 8 style guidelines
- Consistent naming conventions
- Clear function separation and single responsibility
- Comprehensive documentation

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is part of a programming assignment and is available for educational purposes.

## 👨‍💻 Author

Kennedy Adosibe

---

**Version History**
- v2.0 (2024): Major enhancement with menu system, JSON export, statistics, testing
- v1.0 (Original): Basic questionnaire with text file export

