import mysql.connector
global cnx

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="13906@Mysql",
    database="medicaladdvice"
)




def get_test(test):
    try:
        print(test)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT test_details FROM medicaltest WHERE test_name= %s "
        values = (test,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        print("successfully")
        return result
    except mysql.connector.Error as err:
        print("Error retrieving movie info: {}".format(err))
        return None
    except Exception as e:
        print("An error Occurred: {}".format(e))
        return None






