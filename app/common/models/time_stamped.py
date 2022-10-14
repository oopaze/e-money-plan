from datetime import datetime

from flask_sqlalchemy.model import sa


class TimeStampedModel:
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)
