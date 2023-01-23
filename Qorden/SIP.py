from pyVoIP.VoIP import VoIPPhone, InvalidStateError


def answer(call):
    try:
        call.answer()
        call.hangup()
    except InvalidStateError:
        pass


if __name__ == "__main__":
    phone = VoIPPhone('192.168.1.207', 4433, '133', '1234', myIP ='83.110.2.255')
    phone.start()
