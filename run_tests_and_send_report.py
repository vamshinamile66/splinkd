import subprocess
import logging
import smtplib
import os
from email.message import EmailMessage

# Configure logging
logging.basicConfig(
    filename="run_tests_and_send_report.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_tests_and_generate_html_report():
    logging.info("Starting test execution...")
    result = subprocess.run(
        [
            "pytest",
            # "tests/test_signup.py",
            # "tests/test_forgotpassword.py",
            # "tests/test_academy_registration.py",
            "tests/test_login.py",
            "tests/test_programs.py",
            "tests/test_batch.py",
            # "tests/test_athletes.py",
            # "tests/test_coach.py",
            # "tests/test_assign_athletes_to_batch.py",
            # "tests/test_assign_coach_to_batch.py",
            # "tests/test_academy_schedules.py",
            # "tests/test_academy_overview.py",
            # "tests/test_my_team.py",
            # "tests/test_individual_coach.py",
            # "tests/test_individual_athlete.py",
            "--html=report.html",
            "--self-contained-html",
            "--alluredir=allure-results"
            # "--alluredir=allure-results"

            

        ]
    )
    if result.returncode == 0:
        logging.info("Tests executed and HTML report generated successfully.")
    else:
        logging.warning(f"Tests finished with failures. Exit code: {result.returncode}")

def get_html_report_path(report_filename="report.html"):
    return report_filename

def send_email_with_attachment(subject, body, to_email, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "vamshinamile22@gmail.com"
    msg["To"] = to_email
    msg.set_content(body)

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(attachment_path)
    msg.add_attachment(file_data, maintype="application", subtype="zip", filename=file_name)

    # Update SMTP details as needed
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("vamshinamile22@gmail.com", "poio wnpb iczh bngg")
        smtp.send_message(msg)
    logging.info(f"Report sent to {to_email}")

if __name__ == "__main__":
    run_tests_and_generate_html_report()
    html_report = get_html_report_path()
    send_email_with_attachment(
        subject="Splink Automation Test Report",
      body = """
Dear Team,

Please find attached the automated test report for the Splink test cases, 

Generated as part of the latest Continuous Integration (CI) execution.

Best regards,
Vamshi Namile,
Test Engineer.
""",
        to_email="test@gmail.com",
        attachment_path=html_report
    )
