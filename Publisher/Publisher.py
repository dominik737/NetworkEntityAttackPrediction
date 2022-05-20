from typing import List

from Database.Database import Database
from Database.Models.EntityModel import EntityModel


def publish(db: Database, args):
    entities: List[EntityModel] = db.session.query(EntityModel).filter(EntityModel.FMP_score > 0).all()
    low_entities: List[EntityModel] = list(filter(lambda x: x.FMP_score > float(args.publish[0]), entities))
    medium_entities: List[EntityModel] = list(filter(lambda x: x.FMP_score > float(args.publish[1]), entities))
    high_entities: List[EntityModel] = list(filter(lambda x: x.FMP_score > float(args.publish[2]), entities))

    make_publish_file(low_entities, "low.txt")
    make_publish_file(medium_entities, "medium.txt")
    make_publish_file(high_entities, "high.txt")


def make_publish_file(entities: List[EntityModel], publish_file_name: str):
    low_file = open(publish_file_name, "w")
    low_file.write("\n".join(map(lambda x: x.identification, entities)))
    low_file.close()
