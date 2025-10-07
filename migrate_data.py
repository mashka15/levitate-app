from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, Session

sqlite_engine = create_engine('sqlite:///C:/Users/karpo/PycharmProjects/reference/instance/site.db')
sqlite_metadata = MetaData()
sqlite_metadata.reflect(bind=sqlite_engine)

pg_engine = create_engine('postgresql+psycopg2://mashakarpova1511:marukarp123@localhost:5432/levitate')
pg_metadata = MetaData()
pg_metadata.reflect(bind=pg_engine)

SQLiteSession: sessionmaker[Session] = sessionmaker(bind=sqlite_engine)
sqlite_session = SQLiteSession()

PGSession = sessionmaker(bind=pg_engine)
pg_session = PGSession()

for table_name in sqlite_metadata.tables.keys():
    sqlite_table = Table(table_name, sqlite_metadata, autoload_with=sqlite_engine)

    if table_name not in pg_metadata.tables:
        print(f"Таблица {table_name} отсутствует в PostgreSQL, пропускаем")
        continue

    pg_table = Table(table_name, pg_metadata, autoload_with=pg_engine)

    rows = sqlite_session.execute(sqlite_table.select()).mappings().all()
    print(f"Переносим {len(rows)} строк из таблицы {table_name}")

    if rows:
        try:
            pg_session.execute(pg_table.insert(), rows)
            pg_session.commit()
        except Exception as e:
            pg_session.rollback()
            print(f"Ошибка при переносе таблицы {table_name}: {e}")

