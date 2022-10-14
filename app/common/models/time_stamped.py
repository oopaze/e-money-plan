from datetime import datetime

from flask_sqlalchemy.model import sa


class TimeStampedModel:
    created_at = sa.Column(sa.Datetime, default=datetime.now)
    updated_at = sa.Column(sa.Datetime, default=datetime.now, onupdate=datetime.now)
