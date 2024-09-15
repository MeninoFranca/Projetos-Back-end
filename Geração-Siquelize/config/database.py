from sqlalchemy import create_engine, MetaData

def get_table(connection_url):
    engine = create_engine(connection_url)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata.tables
