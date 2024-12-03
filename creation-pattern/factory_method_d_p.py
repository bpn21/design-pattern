from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class Trangle(Shape):
#     def draw(self):
#         print("Drawing Trangle")


# class Circle(Shape):
#     def draw(self):
#         print("Drawing Circle")


# def draw_shape(shape):
#     match shape.lower():
#         case "circle":
#             return Circle()
#         case "trangle":
#             return Trangle()
#         case _:
#             raise ValueError("Unknown Shape Type")


# if __name__ == "__main__":
#     input_shape = input("Enter a shape to draw")
#     object_ = draw_shape(input_shape)
#     object_.draw()

# Without Factory Method
class EmailNotification:
    @abstractmethod
    def send(self):
        print("Sending email notification...")

class SMSNotification:
    def send(self):
        print("Sending SMS notification...")

class PushNotification:
    def send(self):
        print("Sending Push notification...")

class NotificationService:
    def __init__(self, notification_type):
        # This is the place where we are tightly coupling the service
        # to the specific notification types. We should not be hardcoding
        # the instantiation of notification objects here. 
        if notification_type == "email":
            self.notification = EmailNotification()  # Refactor needed here
        elif notification_type == "sms":
            self.notification = SMSNotification()  # Refactor needed here
        elif notification_type == "push":
            self.notification = PushNotification()  # Refactor needed here
        else:
            raise ValueError("Unknown notification type")  # Refactor needed here

    def send_notification(self):
        self.notification.send()

# Client code
email_service = NotificationService("email")
email_service.send_notification()

sms_service = NotificationService("sms")
sms_service.send_notification()

push_service = NotificationService("push")
push_service.send_notification()

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
