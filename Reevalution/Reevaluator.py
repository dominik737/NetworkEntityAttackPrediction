import datetime
from typing import List

from Database import Database
from EntityModel import EntityModel
from Evaluation import Classifier


def run(db: Database, args):
    filter_date = datetime.datetime.now() - datetime.timedelta(hours=args.reevaluation)
    entities: List[EntityModel] = db.session.query(EntityModel).filter(EntityModel.last_updated_date_time < filter_date).all() # možnost filtrovat i fmp > 0
    for entity in entities:
        new_fmp = Classifier.calculate_entity_fmp(entity, args)
        entity.FMP_score = new_fmp
        entity.last_updated_date_time = datetime.datetime.now()
    db.session.commit()
