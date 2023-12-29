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
def InsertData(conn, id, numIn, numOut, date, status):
    cur = conn.cursor()
    sql = "INSERT INTO Bus (idBUS, numIn, numOut, timeBus, statusBus) VALUES (%s, %s, %s, %s, %s)"         
    value = (id,int(numIn) , int(numOut), date, int(status))
    cur.execute(sql, value)
    conn.commit()

# Update data to db
def UpdateData(conn , id, numIn, numOut, date, status):
    cur = conn.cursor()
    sql  = "UPDATE Bus SET numIn = %s, numOut = %s, timeBus = %s, statusBus = %s WHERE idBUS = %s"
    val = (int(numIn), int(numOut), date, int(status), id)
    cur.execute(sql, val)
    conn.commit()
    
# Get data by id
def getDataByID(conn, id):
    cur = conn.cursor()
    sql = "SELECT * FROM Bus WHERE idBUS = " + id
    cur.execute(sql)
    data = cur.fetchall()
    return data

# Print data 
def PrintData(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Bus")
    data = cur.fetchall()
    return data


    