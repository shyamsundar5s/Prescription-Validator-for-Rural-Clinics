from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

engine = create_engine("sqlite:///prescription_validator.db")
meta = MetaData()

drug_interactions = Table(
    'drug_interactions', meta,
    Column('id', Integer, primary_key=True),
    Column('drug_a', String),
    Column('drug_b', String),
    Column('interaction', String),
)

symptom_mapping = Table(
    'symptom_mapping', meta,
    Column('id', Integer, primary_key=True),
    Column('symptom', String),
    Column('medicine', String),
    Column('dosage', String),
)

meta.create_all(engine)
