import mysql.connector    

# Connect to db
def DBConnect(hostName, Username, Password, DBName):
    conn = mysql.connector.connect( 
    host = hostName,
    username = Username,
    password = Password,
    database = DBName)
    if conn.is_connected():
        print("Connected!")
    else :
        print('Not connected!')
    return conn

# Insert data into db
def InsertData(conn, id, numIn, numOut, doorstatus):
    cur = conn.cursor()
    sql = "INSERT INTO CamInfo (idCam, numIn, numOut, doorStatus) VALUES (%s, %s, %s, %s)"         
    value = (id, int(numIn) , int(numOut), int(doorstatus))
    cur.execute(sql, value)
    conn.commit()

# Update data to db
def UpdateData(conn , id, numIn, numOut,doorstatus):
    cur = conn.cursor()
    sql  = "UPDATE CamInfo SET numIn = %s, numOut = %s,  doorStatus = %s WHERE idCam = %s"
    val = (int(numIn), int(numOut),  int(doorstatus), id)
    cur.execute(sql, val)
    conn.commit()
    
#Update Camera status
def UpdateCamStatus(conn, id, camStatus):
    cur = conn.cursor()
    sql  = "UPDATE CamInfo SET camStatus = %s WHERE idCam = %s"
    val = (int(camStatus), id)
    cur.execute(sql, val)
    conn.commit()
    
# Get data by id
def getDataByID(conn, id):
    cur = conn.cursor()
    sql = "SELECT * FROM CamInfo WHERE idCam = " + id
    cur.execute(sql)
    data = cur.fetchall()
    return data

# Print data 
def PrintData(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM CamInfo")
    data = cur.fetchall()
    return data
