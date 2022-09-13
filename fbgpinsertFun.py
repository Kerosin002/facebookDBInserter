import pyodbc
#from fbgpinsert import entryGL, entryGN, anonCh
def fbdbi(gpn,link,anon):
    conn=pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=DESKTOP-INVIIFQ;DATABASE=El_Time_FaceBook;Trusted_Connection=yes')
    anon=str(anon)
    cursor=conn.cursor()

    cursor.execute("INSERT INTO FBGPtest(GPname,Link,AnonPost) VALUES('"+gpn+"','"+link+"',"+anon+")")
    conn.commit()
    cursor.close()
    conn.close()