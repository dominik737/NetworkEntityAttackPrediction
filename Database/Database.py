import datetime
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Database.Enum.EntityIdentificationType import EntityIdentificationType
from Database.Models.EntityModel import EntityModel
from Database.Models.SecurityEventModel import SecurityEventModel
from Database.DeclarativeBase import BASE
from Communication.Model.Packet import Packet
from Evaluation import Classifier
from Exceptions.UnknownFormatException import UnknownFormatException
from Exceptions.UnsharableTypeException import UnsharableTypeException
from Exceptions.MissingConfigEntry import MissingConfigEntry
from Exceptions.DuplicitConfigEntry import DuplicitConfigEntry


class Database:

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        BASE.metadata.create_all(self.engine)
        session_factory = sessionmaker(bind=self.engine)
        self.session = session_factory()
        self.unsharable = []
        self.unsupported = []
        self.key_error = []
        self.missing_config = []
        self.duplicit_config = []

    def store_alert(self, packet: Packet, args):
        for security_event in packet.securityEvents:
            entity = self.get_existing_or_new_entity_by_ip(security_event.attackerIP)
            try:
                security_event_model = SecurityEventModel(security_event)
            except KeyError as error:
                sys.stderr.write("Entity type or sub type missing for security event")
                sys.stderr.write("attackerIP: " + security_event.attackerIP + " detail: " + security_event.detail + "subtype: " + security_event.subType)
                sys.stderr.write(str(error))
                self.key_error.append(security_event)  # TODO: Smazat po testování
                continue
            except UnknownFormatException as error:
                sys.stderr.write("Security event")
                sys.stderr.write(str(error))
                sys.stderr.write("attackerIP: " + security_event.attackerIP + " detail: " + security_event.detail)
                self.unsupported.append(security_event)  # TODO: Smazat po testování
                continue
            except UnsharableTypeException as error:
                sys.stderr.write("Type is not set to be shared")
                sys.stderr.write(str(error))
                self.unsharable.append(security_event)  # TODO: Smazat po testování
                continue
            except MissingConfigEntry as error:
                sys.stderr.write(str(error))
                self.missing_config.append(security_event)  # TODO: Smazat po testování
                continue
            except DuplicitConfigEntry as error:
                sys.stderr.write(str(error))
                self.duplicit_config.append(security_event)  # TODO: Smazat po testování
                continue
            entity.security_events.append(security_event_model)
            entity.FMP_score = Classifier.calculate_entity_fmp(entity, args)
            entity.last_attack_date_time = datetime.datetime.now()
            entity.last_updated_date_time = datetime.datetime.now()
            self.session.commit()

    def get_existing_or_new_entity_by_ip(self, ip):
        entity = self.session.query(EntityModel).filter(EntityModel.identification == ip).first()
        if entity is None:
            entity = EntityModel()
            entity.identification = ip
            entity.identification_type = EntityIdentificationType.IP.value
            self.session.add(entity)
        return entity
