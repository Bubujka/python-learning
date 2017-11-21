#!/usr/bin/env python3
"""Запрос в мускуле"""

from dotenv import load_dotenv, find_dotenv
import pymysql.cursors
import os

load_dotenv(find_dotenv())

connection = pymysql.connect(host=os.environ['MYSQL_HOST'],
                             user=os.environ['MYSQL_USER'],
                             password=os.environ['MYSQL_PASSWORD'],
                             db=os.environ['MYSQL_DATABASE'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        cursor.execute('show databases')
        print(cursor.fetchall())
   #with connection.cursor() as cursor:
   #    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
   #    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
   #connection.commit()

   #with connection.cursor() as cursor:
   #    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
   #    cursor.execute(sql, ('webmaster@python.org',))
   #    result = cursor.fetchone()
   #    print(result)
finally:
    connection.close()
