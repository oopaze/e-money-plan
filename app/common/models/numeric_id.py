from flask_sqlalchemy.model import sa


class NumericIdModel:
    id = sa.Column(sa.Integer, primary_key=True)
