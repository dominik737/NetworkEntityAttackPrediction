from Communication.Model.SecurityEvent import SecurityEvent


class Packet:

    def __init__(self, security_events):
        self.securityEvents = []
        for event in security_events:
            self.securityEvents.append(SecurityEvent(event))
