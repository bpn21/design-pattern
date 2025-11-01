# # Without impelementing observer design pattern
# class Notification:
#     def __init__(self, signals, users):
#         self.signals = signals
#         self.users = users

#     def send_user_notificatoin(self):
#         pass

#     def send_email(self):
#         pass

#     def send_push_notification():
#         pass

#     def send_notifi(self):
#         self.send_user_notificatoin()
#         self.send_email()
#         self.send_push_notification()

# users = []
# signals = []
# noti = Notification(signals,users)
# noti.send_notifi()
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send_notification():
        raise NotImplementedError('Send Notification must be defined')


class PushNotification(Notification):
    def send_notification(self, signals):
        print('Notification Sent')

class UserNotification(Notification):
    def send_notification(self, signals):
        pass

class EmailNotify(Notification):
    def send_notification(self, signals):
        pass


class SignalGenerator():
    def __init__(self, observers, signals):
        self.observers = observers
        self.signals = signals
    
    def attach(self, observer):
        self.observers.append(observer)
    
    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.send_notification(self.signals)


signal_generator = SignalGenerator(observers=[],signals=[])
signal_generator.attach(PushNotification)
signal_generator.notify()