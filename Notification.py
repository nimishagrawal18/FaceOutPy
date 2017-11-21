from pyfcm import FCMNotification

class Notify:
    def __init__(self, head, body=None, col=None):
        self.head = head
        self.body = body
        self.col = col


    def sendnotif(self):
        push_service = FCMNotification(api_key='AAAAMLtwGK0:APA91bEqXYrlOa3f4Cgn-pEInxWzrEsVQr4pCnCCOMsXuyjqU1zpJyzIzyl1R6vY41Yd3qW71CBKahpk259jCxZlHi7Vidj_UDxOHQCp3l3VNBS65vwKs5nK3YbyHutl52p53_rn4kLe')
        try:
            result = push_service.notify_topic_subscribers(topic_name='global', message_body=self.body, message_title=self.head, color=self.col)
            print("Sent to %d Locations Sucessfully, %d Failed.." % (result['success'], result['failure']))
        except:
            print("Error while sending Notification!")

# no=Notify("Test Function","Testing through a class!!","blue")
# no.sendnotif()