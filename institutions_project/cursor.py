import sqlite3

def fill_database(database_name,csv_file_name):
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        with open(csv_file_name,'r') as institutions:
            transaction_number = 0
            for i in institutions:
                cursor.execute("INSERT INTO institutions_app_institution VALUES (?,?,?) ",i.split(','))
                conn.commit()
                transaction_number += 1
        conn.close()
        return True 
    except:
        return False

result = fill_database('db.sqlite3','institution_data.csv')
print(result)