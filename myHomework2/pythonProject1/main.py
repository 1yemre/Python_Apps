
from notifypy import Notify
'''
notification = Notify()
notification.title = "Hi!"
notification.message = "Welcome Emre :)"
notification.send()
'''

#with icon
notification = Notify()
notification.title = "Hi!"
notification.message = "Welcome Emre :)"
notification.icon = "images.png"
notification.send()