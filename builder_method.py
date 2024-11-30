# Using Factory Method Design Pattern

# Abstract class defining a common interface for all notification types
class Notification:
    def send(self):
        raise NotImplementedError("Subclasses should implement this method")

# Concrete class for email notifications
class EmailNotification(Notification):
    def send(self):
        print("Sending email notification...")

# Concrete class for SMS notifications
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification...")

# Concrete class for push notifications
class PushNotification(Notification):
    def send(self):
        print("Sending Push notification...")

# Factory class responsible for creating instances of different notification types
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        """
        This factory method is responsible for creating the appropriate
        notification object based on the provided type.
        This helps in keeping the creation logic separate from the client code,
        and it can easily be extended to handle new types of notifications.
        """
        if notification_type == "email":
            return EmailNotification()  # Create and return EmailNotification instance
        elif notification_type == "sms":
            return SMSNotification()  # Create and return SMSNotification instance
        elif notification_type == "push":
            return PushNotification()  # Create and return PushNotification instance
        else:
            raise ValueError("Unknown notification type")  # Handle invalid types

# Client code
# Instead of directly creating notification objects in the client code,
# we use the NotificationFactory to create them.

email_service = NotificationFactory.create_notification("email")
email_service.send()  # Sending email notification...

sms_service = NotificationFactory.create_notification("sms")
sms_service.send()  # Sending SMS notification...

push_service = NotificationFactory.create_notification("push")
push_service.send()  # Sending Push notification...

