from enum import Enum


class SecurityEventSubType(Enum):
    # BITTORRENT
    # DIRINET
    # HIGHTRANSF
    # HONEYPOT
    # NATDET
    # TEAMVIEWER
    # TOR
    # UPLOAD
    # VOIP
    # SSHDICT
    General = 0
    # BLACKLIST
    Host = 21
    Service = 22
    Web = 23
    Domain = 24
    JA3 = 25
    # BPATTERNS
    AndroidMalware = 31
    BlackOasis = 32
    CryptoMalware = 33
    CryptocurrencyMining = 34
    CryptocurrencyTheft = 35
    DDEExploit = 36
    DNSHijackMacOS = 37
    DarkTequila = 38
    DarkwebViaTor2Web = 39
    DroidclubBotnet = 310
    EdgeChromeExtension = 311
    EmailCampaignThreats = 312
    EternalRocks = 313
    ExploitKit = 314
    FatBoy = 315
    FlashPlayerExploit = 316
    FormbookInfostealer = 317
    Gazer = 318
    GoldDragon = 319
    HackedCCleaner = 320
    InformationStealers = 321
    IoTMalware = 322
    KeyLoggerCryptoMine = 323
    LeviathanFinSpy = 324
    LockyFakeGlobe = 325
    MonetizerCampaign = 326
    PandaMalware = 327
    PegasusSpyware = 328
    Petya = 329
    QakBot = 330
    RamnitTrojan = 331
    Ransomware = 332
    RemcosRAT = 333
    RetefeTrojan = 334
    SIGRed = 335
    DNSServers = 336
    SmbTraffic = 337
    TransferThreshold = 338
    RatioTolerance = 339
    SpionageCampaigns = 340
    SyncCrypt = 341
    TORMalware = 342
    TSSCampaign = 343
    ToriiBotnet = 344
    URSNIFBankingTrojan = 345
    wplogin = 346
    WPMinAttempts = 347
    WPDetectAdmin = 348
    EncryptedDNS = 349
    # DICTATTACK
    SMTPProtocol = 51
    SambaProtocol = 52
    VNCProtocol = 53
    IMAPProtocol = 54
    POP3Protocol = 55
    FTPProtocol = 56
    SSHProtocol = 57
    TelnetProtocol = 58
    RDPProtocol = 59
    HTTPProtocol = 510
    # DIVCOM
    VariousCommunication = 61
    # REFLECTDOS
    Amplification = 71
    # HTTPDICT
    SameSize = 101
    # IPV6TUNNEL
    TeredoTunnel = 111
    _6in4Tunnel = 112
    # L3ANOMALY
    IPSpoof = 121
    SourceMulticast = 122
    SameIPs = 123
    # MULTICAST
    MulticastDetection = 131
    # SCANS
    TCPSYN = 151
    TCPFIN = 152
    TCPNull = 153
    TCPXmas = 154
    UDP = 155
    ARP = 156
    PortBased = 157  # ALSO TELNET
    # SRVNA
    TCPService = 161
    TCPServiceReset = 162
    UDPService = 163
    # VPN
    OpenVPN = 221
    BehavioralDetection = 222
    MSPPTP = 223
    IPSec = 224
    InternetTunnel = 225
    Hamachi = 226
    # WEBSHARE
    SiteVisit = 231
    SiteTransfer = 232
    # COUNTRY
    IncreasedCommunication = 251
    # ALIENDEV
    IPBased = 261
    MACBased = 262
    # DNSANOMALY
    UnusualServer = 271
    TCPHighTraffic = 272
    # SMTPANOMALY
    UndefinedServer = 281
    SpammingClient = 282
    # DNSQUERY
    QueriesCount = 291
    # ANOMALY
    ReceivedBytes = 301
    SentBytes = 302
    ReceivedPackets = 303
    SentPackets = 304
    ProvidedServices = 305
    TCPFlow = 306
    Responses = 307
    UsedServices = 308
    Requests = 309
    ReceivedFlows = 3110
    SentFlows = 3111
    UDPFlow = 3112
    CountUnpaired = 3113
    ActiveDevices = 3114
    PercentUnpaired = 3115
    OtherFlow = 3116
    Peers = 3117
    # ICMPANOM
    PingFlood = 3101
    DestinationUnreachNetwork = 3102
    ICMPScan = 3103
    DestinationUnreachIP = 3104
    # PEERS
    PeersIncrease = 3201
    # DOS
    Volumetric = 3301
    # DHCPANOM
    OversendingClientIP = 3401
    OversendingClientNetwork = 3402
