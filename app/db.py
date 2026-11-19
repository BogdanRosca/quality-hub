from collections.abc import Iterator

from psycopg import Connection
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from app.config import settings

pool = ConnectionPool(
    settings.database_url,
    open=False,
    kwargs={"row_factory": dict_row},
)


def get_conn() -> Iterator[Connection]:
    with pool.connection() as conn:
        yield conn
