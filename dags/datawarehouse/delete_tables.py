# reset_yt_api_tables.py
from airflow.providers.postgres.hooks.postgres import PostgresHook

DROP_SQL = """
BEGIN;
DROP TABLE IF EXISTS staging.yt_api CASCADE;
DROP TABLE IF EXISTS core.yt_api CASCADE;
COMMIT;
"""

def main():
    hook = PostgresHook(postgres_conn_id="postgres_db_yt_elt", database="elt_db")
    with hook.get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(DROP_SQL)
        conn.commit()

if __name__ == "__main__":
    main()