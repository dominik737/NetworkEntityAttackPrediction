from typing import List

from Database import Database
from EntityModel import EntityModel


# TODO: Vylepšit
def publish(db: Database, args):
    entities: List[EntityModel] = db.session.query(EntityModel).filter(EntityModel.FMP_score > 0).all()
    low_entities: List[EntityModel] = list(filter(lambda x: x.FMP_score > float(args.publish[0]), entities))
    medium_entities: List[EntityModel] = list(filter(lambda x: x.FMP_score > float(args.publish[1]), entities))
    high_entities: List[EntityModel] = list(filter(lambda x: x.FMP_score > float(args.publish[2]), entities))
    low_file = open("low.txt", "w")
    low_file.write("\n".join(map(lambda x: x.identification, low_entities)))
    low_file.close()

    medium_file = open("medium.txt", "w")
    medium_file.write("\n".join(map(lambda x: x.identification, medium_entities)))
    medium_file.close()

    high_file = open("high.txt", "w")
    high_file.write("\n".join(map(lambda x: x.identification, high_entities)))
    high_file.close()
