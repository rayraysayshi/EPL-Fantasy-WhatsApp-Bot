# FPL WhatsApp Bot

A Python bot that fetches the latest Fantasy Premier League (FPL) gameweek's bottom performers, generates a funny, savage British-style recap using Google Gemini AI, and sends it to a specified WhatsApp group.

## Features

* Fetches FPL league standings and individual manager scores for the latest completed gameweek.
* Identifies the 4 managers with the lowest scores in the gameweek.
* Leverages the Google Gemini API to generate humorous banter about their performance.
* Automates sending the generated message to a WhatsApp group via WhatsApp Web (using Selenium).

## Prerequisites

Before running the bot, ensure you have the following:

1.  **Python 3.9+**:
    * Download from [python.org](https://www.python.org/downloads/).
2.  **Google Chrome Browser**:
    * The bot uses Selenium to control Chrome for WhatsApp Web. Download from [google.com/chrome](https://www.google.com/chrome/).
3.  **ChromeDriver**:
    * A WebDriver for Chrome that Selenium uses. **It must match your installed Chrome browser version.**
    * Download the correct version from [Google Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
    * Place the `chromedriver` executable in a directory that is in your system's PATH, or update the `webdriver.Chrome()` call in `whatsapp_sender.py` with the full path to `chromedriver`.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
    cd your-repo-name
    ```
    (Replace `YOUR_USERNAME` and `your-repo-name` with your actual GitHub username and repository name).

2.  **Create and activate a Python Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    The bot requires your Google Gemini API key to be set as an environment variable for security reasons.

    * **Get your Google Gemini API Key:** Obtain your API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).
    * **Set the environment variable:**
        * **Temporary (for current terminal session):**
            ```bash
            export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
            ```
        * **Permanent (for macOS/Linux - add to `~/.bash_profile` or `~/.zshrc`):**
            Open your shell's profile file (e.g., `~/.bash_profile`, `~/.zshrc`) in a text editor and add the line:
            ```bash
            export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
            ```
            Then, save the file and run `source ~/.bash_profile` (or `source ~/.zshrc`) or restart your terminal.
        * **Permanent (for Windows):**
            1.  Search for "Environment Variables" in the Windows search bar and open "Edit the system environment variables".
            2.  Click "Environment Variables..."
            3.  Under "User variables for [Your Username]", click "New...".
            4.  For "Variable name", enter `GEMINI_API_KEY`.
            5.  For "Variable value", enter your actual Gemini API key.
            6.  Click "OK" on all open windows.

5.  **Configure `config.py`:**
    Open `config.py` and update the following values:

    ```python
    # FPL League ID - Replace with your FPL Classic League ID
    LEAGUE_ID = <leagueIdHere>

    # WhatsApp Group Name (case-sensitive) - The exact name of your WhatsApp group
    WHATSAPP_GROUP_NAME = "<leagueNameHere>"

    # Timezone offset in hours from UTC (e.g., -5 for CST) - Adjust as needed
    TIMEZONE_OFFSET = <timezoneOffset>
    ```

## Usage

Run the bot from your terminal:

```bash
python3 fpl_bot.py