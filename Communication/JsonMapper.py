import json

from Communication.Model.Packet import Packet


class JsonMapper:

    @staticmethod
    def get_packet(json_packet) -> Packet:
        packet = json.loads(json_packet)
        return Packet(packet["securityEvents"])
