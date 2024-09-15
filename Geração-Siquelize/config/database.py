from sqlalchemy import create_engine, MetaData

def get_table(url):
    engine = create_engine(url)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata.tables
