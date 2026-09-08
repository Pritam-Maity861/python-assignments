"""
Assignment 2: Dependency Injection in Python
"""

class EmailService:
    def send(self, message):
        print(f"Sending Email: {message}")


class SMSService:
    def send(self, message):
        print(f"Sending SMS: {message}")


class NotificationSender:
    def __init__(self, service):
        self.service = service

    def send_notification(self, message):
        self.service.send(message)


if __name__ == "__main__":
    email_service = EmailService()
    sender1 = NotificationSender(email_service)
    sender1.send_notification("Welcome to the platform!")

    sms_service = SMSService()
    sender2 = NotificationSender(sms_service)
    sender2.send_notification("Your OTP is 123456")
