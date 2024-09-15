import pymysql

def get_db_connection():
    return pymysql.connect(
        host = "193.203.175.84",
        user = "u721539099_sigeps",
        password = "/XVQ+y6T[y4",
        database = "u721539099_SIGEPS"
    )
