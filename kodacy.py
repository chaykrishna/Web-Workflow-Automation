from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException

# ===== CONFIG =====
DEBUGGER_ADDRESS = "127.0.0.1:9222"   # match Chrome remote debugging port
MAX_ITEMS = 1000                      # safety stop
WAIT = 1                               # page ready wait
TIMEOUT_BTN = 0.3                      # ultra-fast button wait

MARK_SELECTORS = [
    (By.XPATH, "//button[contains(., 'Mark as Completed')]"),
    (By.XPATH, "//button[contains(., 'Mark as complete')]"),
    (By.XPATH, "//button[contains(., 'Complete') and not(contains(., 'Continue'))]"),
    (By.CSS_SELECTOR, "button[aria-label*='Complete' i]"),
    (By.CSS_SELECTOR, "button[data-testid*='complete' i]"),
]

NEXT_SELECTORS = [
    (By.XPATH, "//a[contains(., 'Next Item')]"),
    (By.XPATH, "//button[contains(., 'Next Item')]"),
    (By.XPATH, "//a[contains(., 'Next')]"),
    (By.XPATH, "//button[contains(., 'Next')]"),
    (By.XPATH, "//a[contains(., 'Continue')]"),
    (By.XPATH, "//button[contains(., 'Continue')]"),
    (By.CSS_SELECTOR, "a[rel='next'], button[rel='next']"),
]

def connect_driver():
    opts = Options()
    opts.debugger_address = DEBUGGER_ADDRESS
    return webdriver.Chrome(options=opts)

def click_if_found(driver, selectors):
    for loc in selectors:
        try:
            el = WebDriverWait(driver, TIMEOUT_BTN).until(EC.presence_of_element_located(loc))
            driver.execute_script("arguments[0].click();", el)  # instant JS click
            return True
        except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException):
            continue
    return False

def wait_page_ready(driver):
    try:
        WebDriverWait(driver, WAIT).until(lambda d: d.execute_script("return document.readyState") == "complete")
    except TimeoutException:
        pass  # skip if too slow — keep moving

def main():
    driver = connect_driver()
    prev_url = driver.current_url
    same_page_count = 0

    for i in range(1, MAX_ITEMS + 1):
        wait_page_ready(driver)
        print(f"[{i}] {driver.current_url}")

        if click_if_found(driver, MARK_SELECTORS):
            print(" [+] Marked complete.")

        if not click_if_found(driver, NEXT_SELECTORS):
            print(" [✓] No next button — probably done.")
            break

        try:
            WebDriverWait(driver, 0.5).until(lambda d: d.current_url != prev_url)
        except TimeoutException:
            same_page_count += 1
            if same_page_count >= 2:
                print(" [!] Stuck — stopping.")
                break
        else:
            same_page_count = 0

        prev_url = driver.current_url

    print("[Done] Turbo run finished.")

if __name__ == "__main__":
    main()
