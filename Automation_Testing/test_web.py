from playwright.sync_api import sync_playwright, Page, expect
import time

BASE_URL = "https://sachalverse.github.io/ai_crop_disease_detection/"

# -------------------- RESULTS STORAGE --------------------
results = []

def log_result(test_name, passed, duration):
    results.append({"test": test_name, "passed": passed, "duration": duration})

def step(msg, wait=2.0):
    """Print the step and wait for better visibility and stability"""
    print(f"[STEP] {msg}")
    time.sleep(wait)

# -------------------- TEST CASES --------------------

def test_homepage_loads(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Waiting for page to fully load", 2)
        step("Checking if 'Crop Doctor' is visible", 1)
        expect(page.locator("body")).to_contain_text("Crop Doctor", timeout=10000)
        log_result("Homepage Loads", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Homepage Loads", False, time.time() - start)

def test_chat_open_close(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Opening chat interface", 2)
        page.locator("#chat-toggle").click()
        step("Waiting for chat input to be visible", 2)
        expect(page.get_by_placeholder("Ask about crops...")).to_be_visible(timeout=10000)
        step("Closing chat interface", 2)
        page.locator("#close-chat").click()
        step("Chat closed successfully", 1)
        log_result("Chat Open/Close", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Chat Open/Close", False, time.time() - start)

def test_chat_send_message(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Opening chat interface", 2)
        page.locator("#chat-toggle").click()
        step("Waiting for chat to be ready", 2)
        
        step("Typing 'hello' in chat input", 2)
        chat_input = page.get_by_placeholder("Ask about crops...")
        chat_input.fill("hello")
        step("Message typed, preparing to send", 1)
        
        step("Clicking send button", 2)
        page.locator("#send-chat").click()
        step("Message sent, waiting for user message to appear", 2)
        
        # Wait for user message to appear
        expect(page.locator(".message.user")).to_have_text("hello", timeout=10000)
        step("User message displayed successfully", 2)
        
        step("Waiting 7 seconds for chatbot API response...", 7)
        # Wait for the latest bot response to appear (use .last to avoid strict mode violation)
        bot_messages = page.locator(".message.bot").last
        expect(bot_messages).to_be_visible(timeout=15000)
        
        # Get the bot response text
        bot_response = bot_messages.text_content()
        print(f"[BOT RESPONSE] {bot_response}")
        step("Chatbot response received and displayed!", 2)
        
        log_result("Chat Send Message", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Chat Send Message", False, time.time() - start)

def test_navigate_crop_doctor(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Clicking Crop Doctor link", 2)
        page.get_by_role("link", name="Crop Doctor").click()
        step("Waiting for page to load", 3)
        step("Checking for Crop AI Assistant text", 1)
        expect(page.locator("body")).to_contain_text("Crop AI Assistant", timeout=10000)
        step("Crop Doctor page loaded successfully", 1)
        log_result("Navigate Crop Doctor", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Navigate Crop Doctor", False, time.time() - start)

def test_navigate_live_feed(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Clicking Live Feed link", 2)
        page.get_by_role("link", name="Live Feed").click()
        step("Waiting for Live Feed page to load", 3)
        step("Checking for ESP32-CAM text", 1)
        expect(page.locator("body")).to_contain_text("ESP32-CAM", timeout=10000)
        step("Live Feed page loaded successfully", 1)
        log_result("Navigate Live Feed", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Navigate Live Feed", False, time.time() - start)

def test_refresh_capture_button(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Navigating to Live Feed", 2)
        page.get_by_role("link", name="Live Feed").click()
        step("Waiting for page to load", 3)
        step("Clicking Refresh Capture button", 2)
        page.get_by_role("button", name="Refresh Capture").click()
        step("Waiting for image to refresh", 3)
        step("Checking for Analyze This Capture button", 1)
        expect(page.get_by_role("button", name="Analyze This Capture")).to_be_visible(timeout=10000)
        step("Capture refreshed successfully", 1)
        log_result("Refresh Capture Button", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Refresh Capture Button", False, time.time() - start)

def test_analyze_capture_button(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Navigating to Live Feed", 2)
        page.get_by_role("link", name="Live Feed").click()
        step("Waiting for page to load", 3)
        step("Clicking Analyze This Capture button", 2)
        page.get_by_role("button", name="Analyze This Capture").click()
        step("Waiting for analysis to complete (7 seconds)", 7)
        step("Checking for Result text", 1)
        expect(page.locator("body")).to_contain_text("Result", timeout=15000)
        step("Analysis completed successfully", 1)
        log_result("Analyze Capture Button", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Analyze Capture Button", False, time.time() - start)

def test_switch_to_urdu(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Switching language to Urdu", 2)
        page.get_by_role("button", name="اردو").click()
        step("Waiting for language switch", 2)
        step("Checking for EN button", 1)
        expect(page.get_by_role("button", name="EN")).to_be_visible(timeout=10000)
        step("Language switched to Urdu successfully", 1)
        log_result("Switch to Urdu", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Switch to Urdu", False, time.time() - start)

def test_switch_back_to_english(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Switching to Urdu first", 2)
        page.get_by_role("button", name="اردو").click()
        step("Waiting for language switch", 2)
        step("Switching back to English", 2)
        page.get_by_role("button", name="EN").click()
        step("Waiting for language switch", 2)
        step("Checking for Crop Doctor link in English", 1)
        expect(page.get_by_role("link", name="Crop Doctor")).to_be_visible(timeout=10000)
        step("Language switched to English successfully", 1)
        log_result("Switch Back to English", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Switch Back to English", False, time.time() - start)

def test_chat_then_navigation(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Opening chat interface", 2)
        page.locator("#chat-toggle").click()
        step("Typing message in chat", 2)
        page.get_by_placeholder("Ask about crops...").fill("hello")
        step("Sending message", 2)
        page.locator("#send-chat").click()
        step("Waiting for response (7 seconds)", 7)
        step("Closing chat", 2)
        page.locator("#close-chat").click()
        step("Navigating to Crop Doctor", 2)
        page.get_by_role("link", name="Crop Doctor").click()
        step("Waiting for page to load", 3)
        step("Checking for Crop AI Assistant text", 1)
        expect(page.locator("body")).to_contain_text("Crop AI Assistant", timeout=10000)
        step("Chat and navigation test completed", 1)
        log_result("Chat Then Navigation", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Chat Then Navigation", False, time.time() - start)

def test_main_buttons_visible(page: Page):
    start = time.time()
    try:
        step("Navigating to Homepage", 3)
        page.goto(BASE_URL, wait_until="networkidle")
        step("Checking main buttons visibility", 2)
        expect(page.get_by_role("link", name="Crop Doctor")).to_be_visible(timeout=10000)
        expect(page.get_by_role("link", name="Live Feed")).to_be_visible(timeout=10000)
        expect(page.get_by_role("button", name="اردو")).to_be_visible(timeout=10000)
        step("All main buttons are visible", 1)
        log_result("Main Buttons Visible", True, time.time() - start)
    except Exception as e:
        print(f"[ERROR] {e}")
        log_result("Main Buttons Visible", False, time.time() - start)

# -------------------- REPORT --------------------

def print_report():
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    failed = total - passed
    avg_time = sum(r["duration"] for r in results) / total if total > 0 else 0
    print("\n" + "="*50)
    print("           TEST EXECUTION REPORT")
    print("="*50)
    print(f"Total Tests  : {total}")
    print(f"Passed       : {passed} ✓")
    print(f"Failed       : {failed} ✗")
    print(f"Pass Rate    : {passed/total*100:.2f}%")
    print(f"Avg Duration : {avg_time:.2f}s")
    print("\n" + "-"*50)
    print("Individual Test Results:")
    print("-"*50)
    for r in results:
        status = "✓ PASS" if r["passed"] else "✗ FAIL"
        print(f"{r['test']:<30} : {status:>7} ({r['duration']:.2f}s)")
    print("="*50 + "\n")

# -------------------- RUN ALL TESTS --------------------

def run_all_tests():
    with sync_playwright() as p:
        print("\n🚀 Starting Browser Automation Tests...\n")
        browser = p.chromium.launch(
            headless=False, 
            slow_mo=1500  # 1.5s delay between actions for better stability
        )
        page = browser.new_page()
        
        # Set longer default timeout
        page.set_default_timeout(30000)  # 30 seconds

        test_homepage_loads(page)
        test_chat_open_close(page)
        test_chat_send_message(page)
        test_navigate_crop_doctor(page)
        test_navigate_live_feed(page)
        test_refresh_capture_button(page)
        test_analyze_capture_button(page)
        test_switch_to_urdu(page)
        test_switch_back_to_english(page)
        test_chat_then_navigation(page)
        test_main_buttons_visible(page)

        print("\n✅ All tests completed. Closing browser...\n")
        time.sleep(2)
        browser.close()

    print_report()

# Run tests if executed directly
if __name__ == "__main__":
    run_all_tests()