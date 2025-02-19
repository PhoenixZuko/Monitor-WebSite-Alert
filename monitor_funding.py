import logging
import time
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

# 🔹 Configure logging
logging.basicConfig(
    filename="alerts.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# 🔹 Read settings from settings.ini
config = configparser.ConfigParser()
config.read("settings.ini")

URL = config.get("Settings", "url")
CHECK_INTERVAL = config.getint("Settings", "check_interval")

TWILIO_SID = config.get("Twilio", "twilio_sid")
TWILIO_AUTH_TOKEN = config.get("Twilio", "twilio_auth_token")
TWILIO_WHATSAPP_NUMBER = config.get("Twilio", "twilio_whatsapp_number")
RECIPIENT_WHATSAPP_NUMBER = config.get("Twilio", "recipient_whatsapp_number")

# 🔹 Store previous funding amounts
last_funding_data = {}
first_run = True  # 🔹 Evită trimiterea mesajelor la prima rulare


def get_funding_data(url):
    """Extracts funding amounts using Selenium."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Allow JavaScript to load

    deals = driver.find_elements(By.XPATH, "//div[contains(text(), 'Funding Available')]")

    funding_data = {}
    for i, deal in enumerate(deals, start=1):
        try:
            amount_label = deal.find_element(By.XPATH, "./following-sibling::label")
            amount = amount_label.text.strip()

            # 🔹 Ignorăm sumele de $0.00 ca să nu trimitem mesaje inutile
            if amount == "$0.00":
                continue  

            funding_data[f"Deal {i}"] = amount
            print(f"💰 Found funding amount: {amount}")
            logging.info(f"✅ Found 'Funding Available' for Deal {i}: {amount}")
        except:
            print(f"⚠️ No amount found for Deal {i}!")
            logging.warning(f"⚠️ No amount found for Deal {i}!")

    driver.quit()
    return funding_data


def send_whatsapp_notification(message):
    """Sends a WhatsApp notification for a funding change."""
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    msg = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=RECIPIENT_WHATSAPP_NUMBER
    )
    logging.info(f"📩 WhatsApp notification sent: {message} (SID: {msg.sid})")
    print(f"📩 WhatsApp notification sent: {msg.sid}")


def monitor_funding():
    """Monitors the webpage and sends notifications for funding changes."""
    global last_funding_data, first_run
    logging.info(f"🔍 Monitoring started: Checking {URL} every {CHECK_INTERVAL} seconds...")
    print(f"🔍 Monitoring {URL} every {CHECK_INTERVAL} seconds...")

    while True:
        current_funding_data = get_funding_data(URL)

        if first_run:
            last_funding_data = current_funding_data  # 🔹 Salvăm datele fără notificare
            first_run = False  # 🔹 După prima rulare, activăm notificările
            print("✅ First run: Saved initial data. No notifications sent.")
            logging.info("✅ First run: Saved initial data. No notifications sent.")
        else:
            changes_detected = []
            for deal, amount in current_funding_data.items():
                if deal in last_funding_data and last_funding_data[deal] != amount:
                    changes_detected.append(f"{deal}: {last_funding_data[deal]} ➝ {amount}")

            # 🔹 Trimitem un singur mesaj cu TOATE modificările detectate
            if changes_detected:
                message = "🔔 Funding Changes:\n" + "\n".join(changes_detected)
                logging.info(message)
                send_whatsapp_notification(message)
                print(message)

            last_funding_data = current_funding_data  # 🔹 Actualizăm datele pentru următoarea verificare

        time.sleep(CHECK_INTERVAL)


# 🔹 Start monitoring
monitor_funding()
