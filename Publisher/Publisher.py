from typing import List

from Database.Database import Database
from Database.Models.EntityModel import EntityModel


def publish(db: Database, args):
    entities: List[EntityModel] = db.session.query(EntityModel).filter(EntityModel.FMP_score > 0).all()
    low_threshold = float(args.publish[0])
    medium_threshold = float(args.publish[1])
    high_threshold = float(args.publish[2])

    low_entities: List[EntityModel] = list(filter(lambda x: low_threshold <= x.FMP_score < medium_threshold, entities))
    medium_entities: List[EntityModel] = list(filter(lambda x: medium_threshold <= x.FMP_score < high_threshold, entities))
    high_entities: List[EntityModel] = list(filter(lambda x: high_threshold <= x.FMP_score, entities))

    make_publish_file(low_entities, "low.txt")
    make_publish_file(medium_entities, "medium.txt")
    make_publish_file(high_entities, "high.txt")


def make_publish_file(entities: List[EntityModel], publish_file_name: str):
    low_file = open(publish_file_name, "w")
    low_file.write("\n".join(map(lambda x: x.identification, entities)))
    low_file.close()
