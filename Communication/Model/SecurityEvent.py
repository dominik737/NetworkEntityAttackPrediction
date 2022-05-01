from datetime import datetime

JSON_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class SecurityEvent:

    def __init__(self, event):
        self.detail: str = event["detail"]
        self.type: str = event["type"]
        self.subType: str = self.get_or_none(event, "subType")
        self.probability = event["probability"]
        self.victimPort = self.get_or_none(event, "victimPort")
        self.attackerIP = event["attackerIP"]
        self.victimIP = self.get_or_none(event, "victimIP")
        self.detectionTime = self.get_date_or_none(event, "detectionTime")
        self.reporterId = event["reporterId"]


    def get_or_none(self, event, key: str):
        try:
            return event[key]
        except:
            return None


    def get_date_or_none(self, event, key: str):
        try:
            return datetime.strptime(event[key], JSON_DATE_FORMAT)
        except:
            return None

