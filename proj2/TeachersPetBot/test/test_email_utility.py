import os
import pytest
from utils import EmailUtility
from dotenv import load_dotenv

load_dotenv()


async def test_send_email_utility_valid():
    recipient = [os.getenv("TEST_RECIPIENT_EMAIL")]
    email_util = EmailUtility()
    email_util.send_email(recipient=recipient)
    assert email_util.output_message == "successfully sent the mail to " + ''.join(recipient)

    with open('data/test_email_utility.pdf', 'r', encoding='latin-1') as test_file:
        email_util = EmailUtility()
        subject = 'THIS IS A TEACHERS PET BOT TEST EVENT'
        email_util.send_email(recipient=recipient, subject=subject, attachment=test_file.read(),
                              filename='test_email_utility.pdf')
        assert email_util.output_message == "successfully sent the mail to " + ''.join(recipient)


# def test_send_email_utility_invalid():
#     with pytest.raises(Exception):
#         recipient = os.getenv("TEST_RECIPIENT_EMAIL_DUMMY")
#         email_util = EmailUtility()
#         email_util.send_email(recipient=recipient)
#         assert email_util.output_message == "successfully sent the mail to " + recipient


async def test():
    await test_send_email_utility_valid()
    # test_send_email_utility_invalid()
