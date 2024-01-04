import tkinter as tk
from tkinter import ttk
import mysql.connector


def collect_data():
    patient_name = patient_name_entry.get()
    patient_email = email_entry.get()
    phone_num = int(phone_num_entry.get())
    date = date_appointment_entry.get()
    age = int(age_label_entry.get())
    consultation_charge = float(consultation_entry.get())
        
     # Connect to your MySQL database
    mydb = mysql.connector.connect(
        host="localhost",    
        user="root",
        password="",
        database="clinic_appointment"
    )

# Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()   
    
    if age >= 50:
        discount_percent = 15


    else:
        discount_percent = 10
             
    discount_amount = (discount_percent / 100) * consultation_charge
    discounted_price = consultation_charge - discount_amount
         
    result_label.config(text=f"Discounted Price: RM{discounted_price: .2f}")

# Insert Data to Database
    sql = "INSERT INTO patient_data (patient_name, patient_email, phone_num, date, patient_age, consultation_charge) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (patient_name, patient_email, phone_num, date, age, discounted_price)
    mycursor.execute(sql, values)
    mydb.commit()

    

# Your Main window 
root = tk.Tk()
root.title("Clinic Appointment System")
root.geometry('400x400')
root.configure(bg='tan')

# Create Label
patient_name_label = tk.Label(root, text="Patient Name : ")
email_label = tk.Label(root, text="Patient Email : ")
phone_num_label = tk.Label(root, text="Phone Number : ")
date_appointment_label= tk.Label(root, text="Date (YYYY-MM-DD) : ")
age_label = tk.Label(root, text="Patient Age : ")
consultation_label = tk.Label(root, text="Consultation Charge : ")

patient_name_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
email_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
phone_num_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
date_appointment_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
age_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
consultation_label.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

# Create Entry Widget 
patient_name_entry = tk.Entry(root)
email_entry = tk.Entry(root)
phone_num_entry = tk.Entry(root)
date_appointment_entry = tk.Entry(root)
age_label_entry = tk.Entry(root)
consultation_entry = tk.Entry(root)

patient_name_entry.grid(row=0, column=1, padx=10, pady=5)
email_entry.grid(row=1, column=1, padx=10, pady=5)
phone_num_entry.grid(row=2, column=1, padx=10, pady=5)
date_appointment_entry.grid(row=3, column=1, padx=10, pady=5)
age_label_entry.grid(row=4, column=1, padx=10, pady=5)
consultation_entry.grid (row=5, column=1, padx=10, pady=5)

# Save Button 
save_button = tk.Button(root, text="Calculate Discount", command=collect_data)
save_button.grid(row=6, column=0, columnspan=2, pady=5)

# Output label & result
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2, pady=5)


root.mainloop()