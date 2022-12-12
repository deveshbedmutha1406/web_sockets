import threading
from channels.layers import get_channel_layer
from .models import *
from faker import Faker
import  random
fake = Faker()

class CreateStudentsThread(threading.Thread):

    def __init__(self):
        self.total = total
        threading.Thread.__init__(self)


    def run(self):
        try:
            print("Thread Exec Started")
            channel_layer = get_channel_layer()
            current_total = 0
            for i in range(self.total):
                current_total += 1
                student_obj = Student.objects.create(
                    student_name = fake.name()
                    student_email = fake.email()
                    address = fake.address()
                    age = random.randint(10, 50)

                )
        except Exception as e:
            print(e)
