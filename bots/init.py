def check_db_connection():
    from django.db import connection

    if connection.connection:
        if not connection.is_usable():
            connection.close()
