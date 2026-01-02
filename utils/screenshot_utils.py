import os
import re
from datetime import datetime

def take_screenshot(driver, name):
    try:
        os.makedirs("screenshots", exist_ok=True)

        # make filename safe
        safe_name = re.sub(r"[^A-Za-z0-9_]+", "_", name)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{safe_name}_{timestamp}.png"

        driver.save_screenshot(path)
        return path

    except Exception as e:
        # NEVER break the framework because of screenshot
        print(f"[WARN] Screenshot failed: {e}")
        return None
