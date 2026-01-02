import os
import shutil
import subprocess
import sys

ALLURE_RESULTS = "reports/allure-results"
ALLURE_REPORT = "reports/allure-report"


def clean_allure():
    if os.path.exists(ALLURE_RESULTS):
        shutil.rmtree(ALLURE_RESULTS)
    if os.path.exists(ALLURE_REPORT):
        shutil.rmtree(ALLURE_REPORT)


def run_behave():
    result = subprocess.run(["behave"])
    if result.returncode != 0:
        print("❌ Behave execution failed")
        sys.exit(result.returncode)


def generate_and_open_allure():
    try:
        subprocess.run(
            f"allure generate {ALLURE_RESULTS} -o {ALLURE_REPORT} --clean",
            shell=True,
            check=True
        )

        subprocess.run(
            f"allure open {ALLURE_REPORT}",
            shell=True
        )

    except KeyboardInterrupt:
        print("\nAllure server stopped by user (Ctrl+C).")


if __name__ == "__main__":
    exit_code = subprocess.call(["behave"])
    generate_and_open_allure()
    sys.exit(exit_code)
