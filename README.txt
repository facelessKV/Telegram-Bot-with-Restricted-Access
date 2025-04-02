🔐 Telegram Bot with Restricted Access

Need to control who can use your bot? This bot ensures restricted access, allowing only authorized users to interact with it!
With this bot, you can secure sensitive features, limit access to specific users, and prevent unauthorized usage.

✅ What does it do?

 • 🔑 Grants access only to approved users based on their Telegram ID
 • 🛑 Blocks unauthorized users from using the bot
 • 📋 Maintains a whitelist of allowed users, editable anytime
 • 📢 Option to send admin notifications when access is attempted

🔧 Features

✅ Secure access control via user ID verification
✅ Admin commands to manage the whitelist easily
✅ Prevents spam and unauthorized usage

📩 Need a secure Telegram bot with restricted access?

Contact me on Telegram, and I’ll help you set up this bot to ensure only the right people can use it! 🚀

========================================================
INSTRUCTIONS FOR INSTALLING AND LAUNCHING A TELEGRAM BOT
========================================================

This guide will help you install and run a Telegram bot, even if you've never done it before.


== PART 1: INSTALLING AND RUNNING ON WINDOWS ==

1. INSTALL PYTHON:
- Download Python version 3.9.13 from the link: https://www.python.org/downloads/release/python-3913 /
- Scroll down and select "Windows installer (64-bit)"
- Run the downloaded file
   - IMPORTANT: Check the box "Add Python 3.9 to PATH" at the bottom of the installer window!
   - Click "Install Now" and wait for the installation to complete

2. CHECKING THE INSTALLATION:
   - Press Win+R on your keyboard, type "cmd" and press Enter
   - In the command prompt that opens, type:
     python --version
   - You should see "Python 3.9.13" or similar text.

3. DOWNLOAD AND CONFIGURE THE BOT:
- Create a folder for the bot, for example C:\TelegramBot
   - Copy the main files.py and config.py to this folder
   - Open the config file.py via Notepad (right click -> Open with -> Notepad)
   - Replace "YOUR_BOT_TOKEN_HERE" with the token received from @BotFather in Telegram
- Replace the numbers in the ALLOWED_USERS list with the user IDs who need access
- Save the file (Ctrl+S)

4. INSTALLATION OF NECESSARY LIBRARIES:
   - Open the command prompt (Win+R, type "cmd", press Enter)
   - Enter the following command to go to the bot folder:
cd C:\TelegramBot
   - Install the aiogram library using pip:
pip install aiogram==3.0.0

5. LAUNCHING THE BOT:
- At the command prompt, while in the folder with the bot, type:
     python main.py
   - If everything is configured correctly, you will see messages about the launch of the bot
- The bot will work while the command prompt is running. To stop the bot,
press Ctrl+C at the command prompt


== PART 2: INSTALLING AND RUNNING ON LINUX ==

1. INSTALL PYTHON:
- Open a terminal (usually Ctrl+Alt+T)
- Run the following commands one at a time:
     sudo apt-get update
     sudo apt-get install python3.9 python3.9-venv python3-pip

2. CHECKING THE INSTALLATION:
   - In the terminal, enter:
     python3.9 --version
   - It should display "Python 3.9.x"

3. CREATE A FOLDER AND CONFIGURE THE BOT:
   - Create a folder for the bot:
     mkdir ~/telegrambot
   - Go to this folder:
cd ~/telegrambot
   - Create a virtual environment:
     python3.9 -m venv venv
   - Activate the virtual environment:
     source venv/bin/activate

4. INSTALLATION OF NECESSARY LIBRARIES:
   - While in a virtual environment (there should be (venv) at the beginning of the line), run:
     pip install aiogram==3.0.0

5. CREATE BOT FILES:
- Create a file in the same folder config.py :
nano config.py
- Copy the contents of the file config.py from the archive
   - Replace "YOUR_BOT_TOKEN_HERE" with a token from @BotFather
   - Replace the numbers in ALLOWED_USERS with the IDs of the required users
   - Save the file: Ctrl+O, then Enter, then Ctrl+X
- Create a file main.py :
nano main.py
- Copy the contents of the file main.py from the archive
   - Save: Ctrl+O, then Enter, then Ctrl+X

6. LAUNCHING THE BOT:
- Make sure that the virtual environment is activated (there should be (venv) at the beginning of the line)
- Launch the bot:
     python main.py
- The bot will work while the terminal is running. To stop, press Ctrl+C


== PART 3: HOW TO GET A TOKEN AND USER ID ==

1. GETTING A BOT TOKEN:
   - Find @BotFather in Telegram
   - Write to him /newbot
   - Follow the instructions, enter a name for the bot
- After creating the bot, @BotFather will send you a token like:
     123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
- Copy this token to a file config.py

2. GETTING THE USER ID:
- In Telegram, find the bot @userinfobot
   - Write him anything or /start
   - He will reply with a message containing your ID
. This ID must be added to the ALLOWED_USERS list in the file. config.py


== PART 4: TROUBLESHOOTING POSSIBLE ISSUES ==

1. "Python not found" or "pip not found":
   - Windows: Make sure to check the box "Add Python to PATH" during installation
   - Linux: Try using python3 and pip3 instead of python and pip

2. "ModuleNotFoundError: No module named 'aiogram'":
- Make sure that you have installed the aiogram library correctly
- Windows: pip install aiogram==3.0.0
- Linux: pip install aiogram==3.0.0 (in an activated virtual environment)

3. "The bot is not responding in Telegram":
- Check if the token is specified correctly in config.py
- Make sure that the bot is running (there should be logs in the command line/terminal)
   - If you have just created a bot, write to it /start

4. "No access":
- Make sure that your ID is added to the ALLOWED_USERS list in the file config.py
- Restart the bot after changing the user list

5. "PermissionError" at startup:
- Windows: Run the command prompt as administrator
- Linux: Check the folder access rights, use sudo if necessary

If you have other problems that are not described here, try searching
the Internet for a solution by specifying the error text from the terminal/command line.
