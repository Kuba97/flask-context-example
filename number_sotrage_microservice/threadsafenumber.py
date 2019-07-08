import threading


class ThreadSafeNumber:
    def __init__(self):
        self.number = 0
        self.lock = threading.Lock()

    def increment_number(self):
        try:
            if self.lock.acquire():
                self.number += 1
        finally:
            if self.lock.locked():
                self.lock.release()

    def decrement_number(self):
        try:
            if self.lock.acquire():
                self.number -= 1
        finally:
            if self.lock.locked():
                self.lock.release()

    def get_number(self):
        number = None
        try:
            if self.lock.acquire():
                number = self.number
        finally:
            if self.lock.locked():
                self.lock.release()
        return number

    def set_number(self, new_number):
        try:
            if self.lock.acquire():
                self.number = new_number
        finally:
            if self.lock.locked():
                self.lock.release()
