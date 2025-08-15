# Web Workflow Automation

**Web Workflow Automation** is a Python-based Selenium bot that automates repetitive multi-step web tasks. It intelligently detects interactive elements such as “Mark as Completed” buttons, navigates sequential pages, and logs progress—dramatically reducing manual effort and saving time.

---

## Features

- Automates sequential web tasks with minimal supervision  
- Detects dynamic buttons and links, handling slight changes in page structure  
- Robust error handling for stale elements, click interruptions, and timing issues  
- Logs progress and actions for easy monitoring  
- Scalable design adaptable to other multi-step web workflows  

---

## Tech Stack

- Python 3  
- Selenium WebDriver  
- Chrome Browser  

---

## Installation, Setup & Usage (All-in-One)

Run all the following in sequence for a complete setup and launch:

```bash
git clone <your-repo-url>
cd WebWorkflowAutomation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
google-chrome --remote-debugging-port=9222 --user-data-dir="$HOME/selenium-profile"
```

Then, in `kodacy_bot.py`, make sure this line exists (edit if needed):

```python
DEBUGGER_ADDRESS = "127.0.0.1:9222"
```

Finally, start the automation:

```bash
python3 kodacy.py
```

---

## How It Works

- Connects to your Chrome session using the debugger address.
- Detects and clicks “Mark as Completed” buttons if available.
- Clicks the “Next” or “Next Item” button to progress through tasks.
- Uses explicit waits to ensure page elements are fully loaded before interacting.
- Logs progress and handles errors to avoid crashes.

---

## Use Cases

- Automating online course completion workflows
- Testing web applications
- Repetitive task automation on dynamic websites

---

## License

This project is open-source and free to use under the MIT License.

---
