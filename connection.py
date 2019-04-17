import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='ec2-79-125-2-142.eu-west-1.compute.amazonaws.com',
                             user='xgvpdxrprnobgr',
                             password='8f711db400cfd3dbd56ab96f29ce28f6ad0e091df39c315bce18ee0c54be7159',
                             database='d7qq0o8c2kmkrq',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "CREATE TABLE users(name varchar(32), user varchar(32), passw varchar(32))"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit() 

    #with connection.cursor() as cursor:
    #    # Read a single record
    #    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #    cursor.execute(sql, ('webmaster@python.org',))
    #    result = cursor.fetchone()
    #    print(result)
finally:
    connection.close()