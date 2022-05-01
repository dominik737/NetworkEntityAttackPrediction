import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import select

from Database import Database
from EntityModel import EntityModel


def plot(db: Database):
    s = select(EntityModel.FMP_score).where(EntityModel.FMP_score != None)
    res = list(db.session.execute(s))
    plottable_data = list(map(lambda x: round(x[0], 3), res))
    plt.figure(figsize=(8, 8))
    plt.margins(x=0, y=0)
    plt.hist(plottable_data, range=[0, 1], bins=10)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.yticks(np.arange(0, 950, step=50))
    plt.show()
