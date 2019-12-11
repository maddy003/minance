import q10


def Fetch():
    fetch = int(input("input 1. to fetch all\n"
                      "input 2. to fetch a particular Device data\n"
                      "input 3. to fetch a particular Employee data\n"))
    if fetch == 1:
        conn = q10.create_connection('EmployeeDeviceDetails.db')
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT EMPLOYEE_DETAILS.EMPLOYEE_ID, F_NAME, L_NAME, DEVICE_ID FROM  EMPLOYEE_DETAILS INNER "
                        "JOIN DEVICE_RELATIONSHIP ON DEVICE_RELATIONSHIP.EMPLOYEE_ID=EMPLOYEE_DETAILS.EMPLOYEE_ID")
            # cur.execute("SELECT * FROM EMPLOYEE_DETAILS")
            # conn.commit()
            # print(cur.fetchall())
            # cur.execute("SELECT * FROM DEVICE_RELATIONSHIP")
            conn.commit()
            print(cur.fetchall())

    elif fetch == 2:
        conn = q10.create_connection('EmployeeDeviceDetails.db')
        if conn is not None:
            temp = input("Device id = ")
            cur = conn.cursor()
            cur.execute("SELECT * FROM DEVICE_RELATIONSHIP WHERE DEVICE_ID=?", (temp,))
            conn.commit()
            print(cur.fetchall())
    elif fetch == 3:
        conn = q10.create_connection('EmployeeDeviceDetails.db')
        if conn is not None:
            temp = input("Employee id = ")
            cur = conn.cursor()
            # cur.execute("SELECT * FROM  EMPLOYEE_DETAILS UNION SELECT * FROM  DEVICE_RELATIONSHIP WHERE DEVICE_ID=?",
            #             temp)
            cur.execute("SELECT * FROM EMPLOYEE_DETAILS WHERE EMPLOYEE_ID=?", (temp,))
            conn.commit()
            print(cur.fetchall())


def put_device_relationship():
    temp_d_id = 1
    while temp_d_id != 0:
        temp_d_id = int(input("Input Device_id\n"
                              "enter 0 to terminate\n"))
        if temp_d_id == 0:
            break

        temp_e_id = input("Enter Employee_id")
        conn = q10.create_connection('EmployeeDeviceDetails.db')
        if conn is not None:
            conn.execute("INSERT INTO DEVICE_RELATIONSHIP (EMPLOYEE_ID,DEVICE_ID) \
                  VALUES (?,?)", (temp_e_id, temp_d_id))
            conn.commit()


def put_employee_details():
    temp_e_id = 1

    while temp_e_id != 0:
        temp_e_id = int(input("Enter Employee_id \n"
                              "enter 0 to terminate\n"))
        if temp_e_id == 0:
            break
        temp_Fname = input("Enter First Name")
        temp_Lname = input("Enter Last Name")
        conn = q10.create_connection('EmployeeDeviceDetails.db')
        if conn is not None:
            conn.execute("INSERT INTO EMPLOYEE_DETAILS (EMPLOYEE_ID,F_NAME,L_NAME) \
                  VALUES (?,?,?)", (temp_e_id, temp_Fname, temp_Lname))
            conn.commit()


def update():
    temp = int(input("Update/Delete from\n"
                     "1.Employee\n"
                     "2.Device\n"))
    temp_id = int(input("Input ID: "))
    conn = q10.create_connection('EmployeeDeviceDetails.db')
    if conn is not None:
        if temp == 1:
            conn.execute("DELETE from EMPLOYEE_DETAILS where EMPLOYEE_ID =? ;", (temp_id,))
            conn.commit()
        elif temp == 2:
            conn.execute("DELETE from DEVICE_RELATIONSHIP where DEVICE_ID =? ;", (temp_id,))
            conn.commit()
        else:
            print("Wrong input")


def main():
    q10.main()
    task_user = int(input("Input Accordingly: \n"
                          "1. Inserting the details of a new employee\n"
                          "2. Inserting the device details for a given employee\n"
                          "3. Updating, deleting the details of an employee or device\n"
                          "4. View records\n"))
    if task_user == 1:
        put_employee_details()
    elif task_user == 2:
        put_device_relationship()
    elif task_user == 3:
        update()
    elif task_user == 4:
        Fetch()
    else:
        print("Invalid Input")


main()
