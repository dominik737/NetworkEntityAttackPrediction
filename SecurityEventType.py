from enum import Enum


class SecurityEventType(Enum):
    BITTORRENT = 1
    BLACKLIST = 2
    BPATTERNS = 3
    DIRINET = 4
    DICTATTACK = 5
    DIVCOM = 6
    REFLECTDOS = 7
    HIGHTRANSF = 8
    HONEYPOT = 9
    HTTPDICT = 10
    IPV6TUNNEL = 11
    L3ANOMALY = 12
    MULTICAST = 13
    NATDET = 14
    SCANS = 15
    SRVNA = 16
    TEAMVIEWER = 17
    TELNET = 18
    TOR = 19
    UPLOAD = 20
    VOIP = 21
    VPN = 22
    WEBSHARE = 23
    SSHDICT = 24
    COUNTRY = 25
    ALIENDEV = 26
    DNSANOMALY = 27
    SMTPANOMALY = 28
    DNSQUERY = 29
    ANOMALY = 30
    ICMPANOM = 31
    PEERS = 32
    DOS = 33
    DHCPANOM = 34
