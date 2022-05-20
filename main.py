import datetime
from argparse import ArgumentParser
from typing import List

from Database.Database import Database
from Plotting import Plotter
from Publisher import Publisher
from Reevalution import Reevaluator
from Database.Models.SecurityEventModel import SecurityEventModel
from Server import Server

PORT = 1235
CONNECTION_STRING = "sqlite:///reputation.db"
DATABASE = Database(CONNECTION_STRING)


# TODO: Smazat
def time_warp(hours):
    events: List[SecurityEventModel] = DATABASE.session.query(SecurityEventModel).all()
    for event in events:
        event.detection_date_time = event.detection_date_time - datetime.timedelta(hours=hours)
    DATABASE.session.commit()


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument("-s", "--short-window", type=int, required=False, default=24,
                            help="Short term window in hours, default value is 24")
    arg_parser.add_argument("-l", "--long-window", type=int, required=False, default=168,
                            help="Long term window in hours, default value is 168")
    arg_parser.add_argument("-r", "--reevaluation", type=float, metavar="LAST_UPDATED", required=False,
                            help="Run reevaluation for entities updated more than LAST_UPDATED hour(s) ago")
    arg_parser.add_argument("-p", "--plot", required=False, action="store_true", help="Plot FMP histogram")
    arg_parser.add_argument("-u", "--publish", required=False, nargs=3, metavar=("LOW_FMP_THRESHOLD", "MEDIUM_FMP_THRESHOLD", "HIGH_FMP_THRESHOLD"), help="Publish categorized offenders to the files.")
    args = arg_parser.parse_args()

    if args.reevaluation:
        Reevaluator.run(DATABASE, args)
    elif args.plot:
        Plotter.plot(DATABASE)
    elif args.publish:
        Publisher.publish(DATABASE, args)
    else:
        server = Server(DATABASE, args)
        server.start(PORT)
