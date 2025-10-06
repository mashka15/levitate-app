from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

sqlite_engine = create_engine('sqlite:///C:/Users/karpo/PycharmProjects/reference/instance/site.db')
sqlite_metadata = MetaData()
sqlite_metadata.reflect(bind=sqlite_engine)

pg_engine = create_engine('postgresql+psycopg2://mashakarpova1511:marukarp123@amvera-karpova-masha1-cnpg-levitate-phm-rw:5000/levitate')
pg_metadata = MetaData()
pg_metadata.reflect(bind=pg_engine)

SQLiteSession = sessionmaker(bind=sqlite_engine)
sqlite_session = SQLiteSession()

PGSession = sessionmaker(bind=pg_engine)
pg_session = PGSession()

for table_name in sqlite_metadata.tables.keys():
    sqlite_table = Table(table_name, sqlite_metadata, autoload_with=sqlite_engine)
    pg_table = Table(table_name, pg_metadata, autoload_with=pg_engine)

    rows = sqlite_session.execute(sqlite_table.select()).fetchall()
    print(f"Переносим {len(rows)} строк из таблицы {table_name}")

    if rows:
        pg_session.execute(pg_table.insert(), [dict(row) for row in rows])
        pg_session.commit()

sqlite_session.close()
pg_session.close()

print("Данные успешно перенесены из SQLite в PostgreSQL")
