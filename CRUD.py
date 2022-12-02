import mysql.connector

def isContinue():
    res = input("Continue[y/n]? ")
    if (res=="y" or res=="Y"):
        return True
    else:
        print("Program closed.")
        return False

    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="newdb",
    port="3307"
    )

    mycursor = mydb.cursor()
    
    repeat = True
    while(repeat):
     print("SELECTIONS OF CODE?;")
     print("1 - Insert Name")
     print("2 - Display name")
     print("3 - Edit a name")
     print("4 - Delete a name")
     print("5 - Exit")
     selection = input("Enter selection: ")
    
    # The following condition performs Insert to
    # the database
    if (selection == "1"):
     name = input("Enter name to insert: ")
     sql = "INSERT INTO demoTable (id, 'name') VALUES (%s,%s)"
     val = (0,name)
     mycursor.execute(sql, val)
     mydb.commit()
     print(name, " was successfully inserted.")
     print("=================================")
     print("=================================")
     repeat = isContinue()
    
    # The following condition displays all the name from
    # the database
    elif (selection=="2"):
     mycursor.execute("SELECT * FROM demoTable")
     myresult = mycursor.fetchall()
     for x in myresult:
      print(x[0], x[1])
     print("================================")
     print("================================")
     repeat = isContinue()
    
    # The following condition performs Editto
    # the selected name from the database
    elif (selection=="3"):
     idName = input("Enter the ID to edit: ")
     name = input("Enter edited name: ")
     sql = "UPDATE demoTable SET 'name' = '" + name + "'"
     sql = sql + " WHERE id = " + idName
     mycursor.execute(sql)
     mydb.commit()
     print(idName, " was successfully edited.")
     print("================================")
     print("================================")
     repeat = isContinue()
    
    # The following condition performs Delete
    # from the database
    elif (selection=="4"):
     name = input("Enter the name to delete: ")
     sql = "DELETE FROM demoTable WHERE 'name' = '" + name + "'"
     mycursor.execute(sql)
     mydb.commit()
     print(name, " was successfully deleted.")
     print("=================================")
     print("=================================")
     repeat = isContinue()
    else:
     repeat = False
     print("=================================")
     print("=================================")

