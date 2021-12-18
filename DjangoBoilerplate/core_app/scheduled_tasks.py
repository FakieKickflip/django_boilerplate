import time


def print_me(text):

    #text is a string. Make sure you pass in a string in the django-q schedule.objects.create()

    for i in range(3):
        print(text)
        time.sleep(3)

    print("done")
