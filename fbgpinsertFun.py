import pyodbc
def fbdbi(gpn,link,anon):
    conn=pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=main-server-nych.database.windows.net;DATABASE=ElTime;UID=CloudSA66f830c2;PWD=Levis2009')
    anon=str(anon)
    cursor=conn.cursor()

    cursor.execute("INSERT INTO FaceBookGroups(GroupName,Link,AnonPost) VALUES(N'"+gpn+"','"+link+"','"+anon+"')")
    conn.commit()
    cursor.close()
    conn.close()