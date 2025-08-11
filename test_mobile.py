import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = UiAutomator2Options()
options.platformName = "Android"
options.platformVersion = "11"
options.deviceName = "R28M70PNJ3F"
options.appPackage = "com.arcone.arcone"
options.appActivity = "com.arcone.arcone.MainActivity"
options.automationName = "UiAutomator2"
options.noReset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 20)

try:
    # ====== Attendance Report Search ======
    hr_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="HR"]')))
    hr_element.click()
    time.sleep(1)

    my_attendance_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="My Attendance"]')))
    my_attendance_element.click()
    time.sleep(1)

    from_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="01/07/2025"]')))
    from_date.click()
    time.sleep(0.5)

    to_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="31/07/2025"]')))
    to_date.click()
    time.sleep(0.5)

    image_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.ImageView')))
    image_element.click()
    time.sleep(2)

    results_container = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//android.widget.HorizontalScrollView/android.view.ViewGroup')
    ))
    children = results_container.find_elements(By.XPATH, "./*")

    if len(children) > 0:
        print(f"Search results appeared with {len(children)} items.")
        driver.save_screenshot("search_results.png")
    else:
        print("Search results container is present but no data found.")
        driver.save_screenshot("empty_search_results.png")

    # ====== Check-IN Process ======
    hr_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="HR"]')))
    hr_element.click()
    time.sleep(1)

    checkin_menu = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Check-IN"]')))
    checkin_menu.click()
    time.sleep(2)

    camera_preview = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//android.view.ViewGroup[@resource-id="com.sec.android.app.camera:id/intelligent_view"]')
    ))
    camera_preview.click()
    time.sleep(1)

    ok_button_camera = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@content-desc="OK"]')))
    ok_button_camera.click()
    time.sleep(1)

    ok_button_checkin = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.ViewGroup[@content-desc="OK"]')))
    ok_button_checkin.click()
    time.sleep(1)

    # ====== Leave Application ======
    hr_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="HR"]')))
    hr_element.click()
    time.sleep(1)

    leave_app_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Leave Application"]')))
    leave_app_element.click()
    time.sleep(1)

    new_app_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.ViewGroup[@content-desc="+, Application"]')))
    new_app_btn.click()
    time.sleep(1)

    leave_type = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Leave Type*"]')))
    leave_type.click()
    annual_leave_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Annual Leave"]')))
    annual_leave_option.click()
    time.sleep(0.5)

    leave_cat = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Select Leave Category*"]')))
    leave_cat.click()
    casual_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Casual"]')))
    casual_option.click()
    time.sleep(0.5)

    from_date_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="From Date*"]')))
    from_date_label.click()
    from_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="11/08/2025"]')))
    from_date.click()
    time.sleep(0.5)

    to_date_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="To Date*"]')))
    to_date_label.click()
    to_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="13/08/2025"]')))
    to_date.click()
    time.sleep(0.5)

    reason_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.EditText[@text="Tour"]')))
    reason_input.clear()
    reason_input.send_keys("Tour")
    time.sleep(0.5)

    apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Apply"]')))
    apply_btn.click()
    time.sleep(2)

except Exception as e:
    print("Error during automation:", e)
    driver.save_screenshot("error_screenshot.png")

finally:
    driver.quit()
