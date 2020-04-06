from mycroft import MycroftSkill, intent_file_handler


class TalanthusRadio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.talanthus.intent')
    def handle_radio_talanthus(self, message):
        self.speak_dialog('radio.talanthus')


def create_skill():
    return TalanthusRadio()

