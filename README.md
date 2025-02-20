#  Funding Monitor 
A Python script that monitors funding availability on a website and sends WhatsApp alerts using the Twilio API.

##  What does this script do?
This script was developed for a client who wanted to receive WhatsApp notifications whenever funding amounts changed on their website. The website fetches data directly via a secured API, making Selenium the best choice for extracting the necessary information.

##  Features
- Monitors funding availability in real-time.
- Logs all detected changes in `alerts.log`.
- Sends WhatsApp alerts when funding amounts change.
- Configurable via `settings.ini`.
- Successfully tested to work without crashes or blocking.

##  Twilio Account Required  
To send WhatsApp messages, you need a Twilio account. Twilio provides **$5 - $15** in free credits for new accounts, which is enough for testing. You can sign up at [Twilio's website](https://www.twilio.com/).  

##  Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/user/funding-monitor.git
   cd funding-monitor

##  Features
- Scrapes funding data using Selenium.
- Logs funding changes in `alerts.log`.
- Sends real-time WhatsApp alerts via Twilio.
- Configurable via `settings.ini`.

##  Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/user/funding-monitor.git
   cd funding-monitor
Testing Scripts
Before running the main program, you can use the following test scripts to verify that Twilio and Selenium are correctly installed and configured.

  test_Twilio.py
This script checks if your Twilio credentials are correctly set up and if messages can be sent successfully via Twilio WhatsApp.
How to use:
   python3 test_Twilio.py

If everything is working correctly, you should receive a WhatsApp message at the configured phone number.

   test_Selenium.py
This script verifies that Selenium is correctly installed and that the browser automation setup is working.

 How to use:
    python test_Selenium.py

If Selenium is properly configured, the script should open a browser window, navigate to a test website, and close the browser.



   ##  Author
**Andrei Sorin Stefan**  
[GitHub Profile] https://github.com/PhoenixZuko
[LinkedIn] https://www.linkedin.com/in/andrei-sorin-stefan-8b1682318/
[Website] https://vorte.eu/
