from datetime import datetime

class EpochTime(object):
    def __init__(self):
        pass

    def value(self):
        return str(datetime.now().replace(microsecond=0).timestamp())
