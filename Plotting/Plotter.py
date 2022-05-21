import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import select

from Database.Database import Database
from Database.Models.EntityModel import EntityModel


def plot(db: Database, hours: float):
    s = select(EntityModel.FMP_score).where(EntityModel.FMP_score != None)
    res = list(db.session.execute(s))
    plottable_data = list(map(lambda x: round(x[0], 3), res))
    plt.rcParams.update({'font.size': 17})
    plt.figure(figsize=(8, 8))
    plt.margins(x=0, y=0)
    plt.hist(plottable_data, range=[0, 1], bins=10)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.yticks(np.arange(0, 950, step=50))
    plt.xlabel("FMP Skóre")
    plt.ylabel("Počet síťových entit")
    plt.title(f"Po {hours} hodinách")
    plt.savefig(f"FMP_{get_serial_number(hours)}.png")
    # plt.show()

def get_serial_number(hours: float):
    return str(hours) if hours >= 100 else f"0{str(hours)}" if hours >= 10 else f"00{hours}"