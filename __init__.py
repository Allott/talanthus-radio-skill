from mycroft import MycroftSkill, intent_file_handler
from mycroft_bus_client import MessageBusClient, Message

class TalanthusRadio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.talanthus.intent')
    def handle_radio_talanthus(self, message):
        print('Setting up client to connect to a local mycroft instance')
        client = MessageBusClient()
        client.run_in_thread()

        print('Sending speak message...')
        client.emit(Message('play', data={'utterance': '+ Talanthus Radio +'}))
        
def create_skill():
    return TalanthusRadio()

