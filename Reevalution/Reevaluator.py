import datetime
from typing import List

from Database.Database import Database
from Database.Models.EntityModel import EntityModel
from Evaluation import Classifier


def run(db: Database, args):
    filter_date = datetime.datetime.now() - datetime.timedelta(hours=args.reevaluation)
    entities: List[EntityModel] = db.session.query(EntityModel).filter(EntityModel.last_updated_date_time < filter_date).all() # možnost filtrovat i fmp > 0
    for entity in entities:
        new_fmp = Classifier.calculate_entity_fmp(entity, args)
        entity.FMP_score = new_fmp
        entity.last_updated_date_time = datetime.datetime.now()
    delete_harmless_entities(db)
    db.session.commit()

def delete_harmless_entities(db: Database):
    db.session.query(EntityModel).filter(EntityModel.FMP_score == 0 or EntityModel.FMP_score == None).delete()