# Automated Application and Website Opener

This Python script uses `pyautogui` to automate the process of opening applications and websites. The script takes a command as input, randomly selects a pre-defined opening dialogue, and then utilizes keyboard shortcuts and typing to open the specified application or website.

## Prerequisites

Ensure you have the required libraries installed before running the script:

```bash
pip install pyautogui
```

## Usage

```python
from your_script_name import open

# Example usages
open("YouTube app")
open("Google website")
```

## Code Explanation

1. **Dependencies:**
   - `pyautogui`: Library for automating keyboard and mouse actions.

2. **Functions:**
   - `opend(text)`: Opens the specified application or website.
      - Randomly selects an opening dialogue from the pre-defined options.
      - Uses `pyautogui` to simulate keypresses for opening the application or website.

   - `open(text)`: Main function for opening applications or websites based on the provided text command.
      - If the command contains "website," it appends ".com" to the text and opens it as a website.
      - If the command contains "app," it opens the application directly.
      - If neither "website" nor "app" is specified, it opens the application or website with a default dialogue.

3. **Data:**
   - `open_dld`: List of pre-defined opening dialogues for a personalized touch.

## Note

Ensure that the command you provide is clear and matches the expected format. For example:
- "YouTube app" will open the YouTube application.
- "Google website" will open the Google website.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
