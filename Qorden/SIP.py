from pyVoIP.VoIP import VoIPPhone, InvalidStateError


def answer(call):
    try:
        call.answer()
        call.hangup()
    except InvalidStateError:
        pass


if __name__ == "__main__":
    phone = VoIPPhone('192.168.1.207', 4433, 168, 1234, myIP ='192.168.11.113', rtpPortLow=49152, rtpPortHigh=64512)
    phone.start()
    input('Press enter to disable the phone')
    phone.stop()