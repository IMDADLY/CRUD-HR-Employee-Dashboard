import pymysql


class Database:
    def connect(self):
        # return pymysql.connect("employee-mysql", "dev", "dev", "crud_flask")

        return pymysql.connect(host="localhost", user="root", password="root", database="crud_flask", charset='utf8mb4')

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM employee")
            else:
                cursor.execute(
                    "SELECT * FROM employee where id = %s", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            print(data['performance_score'])
            print(type(data['performance_score']))
            cursor.execute("INSERT INTO employee(id,name,gender,salary,address, performance_score,remarks) VALUES( %s, %s, %s, %s, %s, %s, %s)",
                           (data['id'],data['name'], data['gender'], int(data['salary']),data['address'],float(data['performance_score']),data['remarks']))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE employee set name = %s, gender = %s, salary = %s, address = %s, performance_score = %s, remarks =%s where id = %s",
                           (data['name'], data['gender'], int(data['salary']), data['address'], float(data['performance_score']), data['remarks'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM employee where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def export(self):
        con = Database.connect(self)
        cursor=con.cursor()
        cursor.execute('SELECT * from employee')
