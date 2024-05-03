import tkinter as tk
from tkinter import messagebox
import pickle
import os

# All classes added with neccsary functions and attributes
class Company:
    def __init__(self, companyId, company_name, address, contactDetails):
        self.companyId = companyId
        self.company_name = company_name
        self.address = address
        self.contactDetails = contactDetails
        self.events = [] # Composition with Event class.

    def getCompanyId(self):
        return self.companyId

    def setCompanyId(self, companyId):
        self.companyId = companyId

    def getCompanyName(self):
        return self.company_name

    def setCompanyName(self, companyName):
        self.company_name = companyName

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getContactDetails(self):
        return self.contactDetails

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails

class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    def employee_info(self):
        return f"Name: {self.name}, employee_id: {self.employee_id}, Department: {self.department}, Job Title: {self.job_title}, Basic Salary: {self.basic_salary}, Age: {self.age}, Date of Birth: {self.date_of_birth}, Passport Details: {self.passport_details}"

class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers, invoice):
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list # Aggregation with Guest class.
        self.suppliers = suppliers  # Aggregation with Supplier class.
        self.venue = Venue()   # Composition with Venue class.
        self.invoice = Invoice()  # Composition with Invoice class.

class Supplier:
    def __init__(self, supplier_id, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number):
        self.supplier_id = supplier_id
        self.supp_name = supp_name
        self.supp_address = supp_address
        self.supp_contactDetails = supp_contactDetails
        self.booking_availability = booking_availability
        self.staff_number = staff_number

class Caterer(Supplier):
    def __init__(self, supplierId, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number, menu, foodLicense, DietaryOptions):
        super().__init__(supplierId, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number)
        self.menu = menu
        self.foodLicense = foodLicense
        self.DietaryOptions = DietaryOptions

    def displayCatererInfo(self):
        caterer_info = f"Supplier ID: {self.supplierId}, Name: {self.supp_name}, Address: {self.supp_address}, Contact Details: {self.supp_contactDetails}, Booking Availability: {self.booking_availability}, Staff Number: {self.staff_number}, Menu: {self.menu}, Food License: {self.foodLicense}, Dietary Options: {self.DietaryOptions}"
        return caterer_info

class FurnitureSupplier(Supplier):
    def __init__(self, supplierId, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number, furnitureCatalog, decorationCatalog, decoration_Packages, furnitureAssemblyOptions):
        super().__init__(supplierId, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number)
        self.furnitureCatalog = furnitureCatalog
        self.decorationCatalog = decorationCatalog
        self.decoration_Packages = decoration_Packages
        self.furnitureAssemblyOptions = furnitureAssemblyOptions

    def displayFurnitureSupplier_info(self):
        furniture_supplier_info = f"Supplier ID: {self.supplierId}, Name: {self.supp_name}, Address: {self.supp_address}, Contact Details: {self.supp_contactDetails}, Booking Availability: {self.booking_availability}, Staff Number: {self.staff_number}, Furniture Catalog: {self.furnitureCatalog}, Decoration Catalog: {self.decorationCatalog}, Decoration Packages: {self.decoration_Packages}, Furniture Assembly Options: {self.furnitureAssemblyOptions}"
        return furniture_supplier_info

class CleaningSupplier(Supplier):
    def __init__(self, supplierId, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number, cleaningServices, certifications, cleaningEquipment):
        super().__init__(supplierId, supp_name, supp_address, supp_contactDetails, booking_availability, staff_number)
        self.cleaningServices = cleaningServices
        self.certifications = certifications
        self.cleaningEquipment = cleaningEquipment

    def displayCleaningSupplier_info(self):
        cleaning_supplier_info = f"Supplier ID: {self.supplierId}, Name: {self.supp_name}, Address: {self.supp_address}, Contact Details: {self.supp_contactDetails}, Booking Availability: {self.booking_availability}, Staff Number: {self.staff_number}, Cleaning Services: {self.cleaningServices}, Certifications: {self.certifications}, Cleaning Equipment: {self.cleaningEquipment}"
        return cleaning_supplier_info

class Invoice:
    def __init__(self, invoiceId=None, eventID=None, clientId=None, date=None):
        self.invoiceId = invoiceId
        self.eventID = eventID
        self.clientId = clientId
        self.date = date

    def displayInvoice_info(self):
        invoice_info = f"Invoice ID: {self.invoiceId}, Event ID: {self.eventID}, Client ID: {self.clientId}, Date: {self.date}"
        return invoice_info

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def addGuest(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}"

    def deleteGuest(self):
        self.guest_id = None
        self.name = None
        self.address = None
        self.contact_details = None
        return "Guest details have been deleted."

    def modifyGuest(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        return "Guest details have been modified."

    def displayGuest(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}"

class Venue:
    def __init__(self, venue_id=None, name=None, address=None,contact=None, min_guests=None, max_guests=None):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests


class DataLayer:
    """Class to handle read and write operations for data."""
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'rb') as file:
                data = pickle.load(file)
                return data

    def write_data(self, data):
        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

class GUI:
    """Class to represent the GUI."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event Management System")
        self.root.geometry("400x300")

        self.employee_button = tk.Button(self.root, text="Manage Employees", command=self.manage_employees)
        self.employee_button.pack(pady=10)

        self.event_button = tk.Button(self.root, text="Manage Events", command=self.manage_events)
        self.event_button.pack(pady=10)

        self.client_button = tk.Button(self.root, text="Manage Clients", command=self.manage_clients)
        self.client_button.pack(pady=10)

        self.guest_button = tk.Button(self.root, text="Manage Guests", command=self.manage_guests)
        self.guest_button.pack(pady=10)

        self.supplier_button = tk.Button(self.root, text="Manage Suppliers", command=self.manage_suppliers)
        self.supplier_button.pack(pady=10)

        self.venue_button = tk.Button(self.root, text="Manage Venues", command=self.manage_venues)
        self.venue_button.pack(pady=10)

        self.data_layer = DataLayer("event_management_data.pkl")

    def manage_employees(self):
        employee_management = EmployeeManagement()

    def manage_events(self):
       event_management = EventManagement()

    def manage_clients(self):
        client_management = ClientManagement()

    def manage_guests(self):
        guest_management = GuestManagement()

    def manage_suppliers(self):
        supplier_management = SupplierManagement()

    def manage_venues(self):
        venue_management = VenueManagement()

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def run(self):
     self.root.mainloop()



class EmployeeManagement(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.display_button = None
        self.modify_button = None
        self.employees = None
        self.delete_button = None
        self.add_button = None
        self.employee_listbox = None
        self.name_entry = None
        self.id_entry = None
        self.department_entry = None
        self.job_title_entry = None
        self.basic_salary_entry = None
        self.age_entry = None
        self.date_of_birth_entry = None
        self.passport_details_entry = None
        self.title("Employee Management System")
        self.geometry("800x600")
        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.employees = []
        if os.path.exists("employees.pkl"):
            with open("employees.pkl", "rb") as file:
                self.employees = pickle.load(file)

    def save_data(self):
        with open("employees.pkl", "wb") as file:
            pickle.dump(self.employees, file)

    def create_widgets(self):
        self.employee_listbox = tk.Listbox(self, width=100, height=20)
        self.employee_listbox.pack()

        self.add_button = tk.Button(self, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack()

        self.modify_button = tk.Button(self, text="Modify Employee", command=self.modify_employee)
        self.modify_button.pack()

        self.display_button = tk.Button(self, text="Display Employees", command=self.display_employees)
        self.display_button.pack()
        self.search_button = tk.Button(self, text="Search Employee", command=self.search_employee)
        self.search_button.pack()

    def add_employee(self):
        add_employee_window = tk.Toplevel(self)
        add_employee_window.title("Add Employee")

        tk.Label(add_employee_window, text="Name").grid(row=0)
        tk.Label(add_employee_window, text="Employee ID").grid(row=1)
        tk.Label(add_employee_window, text="Department").grid(row=2)
        tk.Label(add_employee_window, text="Job Title").grid(row=3)
        tk.Label(add_employee_window, text="Basic Salary").grid(row=4)
        tk.Label(add_employee_window, text="Age").grid(row=5)
        tk.Label(add_employee_window, text="Date of Birth").grid(row=6)
        tk.Label(add_employee_window, text="Passport Details").grid(row=7)

        self.name_entry = tk.Entry(add_employee_window)
        self.id_entry = tk.Entry(add_employee_window)
        self.department_entry = tk.Entry(add_employee_window)
        self.job_title_entry = tk.Entry(add_employee_window)
        self.basic_salary_entry = tk.Entry(add_employee_window)
        self.age_entry = tk.Entry(add_employee_window)
        self.date_of_birth_entry = tk.Entry(add_employee_window)
        self.passport_details_entry = tk.Entry(add_employee_window)

        self.name_entry.grid(row=0, column=1)
        self.id_entry.grid(row=1, column=1)
        self.department_entry.grid(row=2, column=1)
        self.job_title_entry.grid(row=3, column=1)
        self.basic_salary_entry.grid(row=4, column=1)
        self.age_entry.grid(row=5, column=1)
        self.date_of_birth_entry.grid(row=6, column=1)
        self.passport_details_entry.grid(row=7, column=1)

        submit_button = tk.Button(add_employee_window, text="Submit",
                                  command=lambda: self.submit_add_employee(self.name_entry.get(), self.id_entry.get(),
                                                                           self.department_entry.get(),
                                                                           self.job_title_entry.get(),
                                                                           self.basic_salary_entry.get(),
                                                                           self.age_entry.get(),
                                                                           self.date_of_birth_entry.get(),
                                                                           self.passport_details_entry.get()))
        submit_button.grid(row=8, column=0, columnspan=2)

    def submit_add_employee(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth,
                            passport_details):
        employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth,
                            passport_details)
        self.employees.append(employee)
        self.save_data()
        messagebox.showinfo("Success", "Employee added successfully")
        self.clear_fields()

    def delete_employee(self):
        selected_index = self.employee_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.employees[index]
            self.save_data()
            self.display_employees()
            messagebox.showinfo("Success", "Employee deleted successfully")
        else:
            messagebox.showerror("Error", "Please select an employee to delete")

    def modify_employee(self):
        selected_index = self.employee_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            employee = self.employees[index]
            modify_employee_window = tk.Toplevel(self)
            modify_employee_window.title("Modify Employee")

            tk.Label(modify_employee_window, text="Name").grid(row=0)
            tk.Label(modify_employee_window, text="Employee ID").grid(row=1)
            tk.Label(modify_employee_window, text="Department").grid(row=2)
            tk.Label(modify_employee_window, text="Job Title").grid(row=3)
            tk.Label(modify_employee_window, text="Basic Salary").grid(row=4)
            tk.Label(modify_employee_window, text="Age").grid(row=5)
            tk.Label(modify_employee_window, text="Date of Birth").grid(row=6)
            tk.Label(modify_employee_window, text="Passport Details").grid(row=7)

            name_entry = tk.Entry(modify_employee_window, text=employee.name)
            id_entry = tk.Entry(modify_employee_window, text=employee.employee_id)
            department_entry = tk.Entry(modify_employee_window, text=employee.department)
            job_title_entry = tk.Entry(modify_employee_window, text=employee.job_title)
            basic_salary_entry = tk.Entry(modify_employee_window, text=employee.basic_salary)
            age_entry = tk.Entry(modify_employee_window, text=employee.age)
            date_of_birth_entry = tk.Entry(modify_employee_window, text=employee.date_of_birth)
            passport_details_entry = tk.Entry(modify_employee_window, text=employee.passport_details)

            name_entry.grid(row=0, column=1)
            id_entry.grid(row=1, column=1)
            department_entry.grid(row=2, column=1)
            job_title_entry.grid(row=3, column=1)
            basic_salary_entry.grid(row=4, column=1)
            age_entry.grid(row=5, column=1)
            date_of_birth_entry.grid(row=6, column=1)
            passport_details_entry.grid(row=7, column=1)

            submit_button = tk.Button(modify_employee_window, text="Submit",
                                      command=lambda: self.submit_modify_employee(index, name_entry.get(),
                                                                                  id_entry.get(),
                                                                                  department_entry.get(),
                                                                                  job_title_entry.get(),
                                                                                  basic_salary_entry.get(),
                                                                                  age_entry.get(),
                                                                                  date_of_birth_entry.get(),
                                                                                  passport_details_entry.get()))
            submit_button.grid(row=8, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Please select an employee to modify")

    def submit_modify_employee(self, index, name, employee_id, department, job_title, basic_salary, age, date_of_birth,
                               passport_details):
        employee = self.employees[index]
        employee.name = name
        employee.employee_id = employee_id
        employee.department = department
        employee.job_title = job_title
        employee.basic_salary = basic_salary
        employee.age = age
        employee.date_of_birth = date_of_birth
        employee.passport_details = passport_details
        self.save_data()
        messagebox.showinfo("Success", "Employee modified successfully")

    def display_employees(self):
        self.employee_listbox.delete(0, tk.END)
        for employee in self.employees:
            self.employee_listbox.insert(tk.END, employee.employee_info())

    def search_employee(self):
        search_window = tk.Toplevel(self)
        search_window.title("Search Employee")

        tk.Label(search_window, text="Employee ID:").grid(row=0, column=0)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search",
                                  command=lambda: self.display_search_result(id_entry.get()))
        search_button.grid(row=1, column=0, columnspan=2)

    def display_search_result(self, employee_id):
        result_window = tk.Toplevel(self)
        result_window.title("Search Result")

        found = False
        for employee in self.employees:
            if employee.employee_id == employee_id:
                found = True
                tk.Label(result_window, text="Name:").grid(row=0, column=0)
                tk.Label(result_window, text=employee.name).grid(row=0, column=1)
                tk.Label(result_window, text="Employee ID:").grid(row=1, column=0)
                tk.Label(result_window, text=employee.employee_id).grid(row=1, column=1)
                tk.Label(result_window, text="Department:").grid(row=2, column=0)
                tk.Label(result_window, text=employee.department).grid(row=2, column=1)
                tk.Label(result_window, text="Job Title:").grid(row=3, column=0)
                tk.Label(result_window, text=employee.job_title).grid(row=3, column=1)
                tk.Label(result_window, text="Basic Salary:").grid(row=4, column=0)
                tk.Label(result_window, text=employee.basic_salary).grid(row=4, column=1)
                tk.Label(result_window, text="Age:").grid(row=5, column=0)
                tk.Label(result_window, text=employee.age).grid(row=5, column=1)
                tk.Label(result_window, text="Date of Birth:").grid(row=6, column=0)
                tk.Label(result_window, text=employee.date_of_birth).grid(row=6, column=1)
                tk.Label(result_window, text="Passport Details:").grid(row=7, column=0)
                tk.Label(result_window, text=employee.passport_details).grid(row=7, column=1)
                break

        if not found:
            tk.Label(result_window, text="Employee not found").pack()

    def clear_fields(self):
        # Clear entry fields
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.job_title_entry.delete(0, tk.END)
        self.basic_salary_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.date_of_birth_entry.delete(0, tk.END)
        self.passport_details_entry.delete(0, tk.END)

def search_employee(self):
    search_window = tk.Toplevel(self)
    search_window.title("Search Employee")

    tk.Label(search_window, text="Employee ID:").grid(row=0, column=0)
    id_entry = tk.Entry(search_window)
    id_entry.grid(row=0, column=1)

    search_button = tk.Button(search_window, text="Search",
                              command=lambda: self.display_search_result(id_entry.get()))
    search_button.grid(row=1, column=0, columnspan=2)

def display_search_result(self, employee_id):
    result_window = tk.Toplevel(self)
    result_window.title("Search Result")

    found = False
    for employee in self.employees:
        if employee.employee_id == employee_id:
            found = True
            tk.Label(result_window, text="Name:").grid(row=0, column=0)
            tk.Label(result_window, text=employee.name).grid(row=0, column=1)
            tk.Label(result_window, text="Employee ID:").grid(row=1, column=0)
            tk.Label(result_window, text=employee.employee_id).grid(row=1, column=1)
            tk.Label(result_window, text="Department:").grid(row=2, column=0)
            tk.Label(result_window, text=employee.department).grid(row=2, column=1)
            tk.Label(result_window, text="Job Title:").grid(row=3, column=0)
            tk.Label(result_window, text=employee.job_title).grid(row=3, column=1)
            tk.Label(result_window, text="Basic Salary:").grid(row=4, column=0)
            tk.Label(result_window, text=employee.basic_salary).grid(row=4, column=1)
            tk.Label(result_window, text="Age:").grid(row=5, column=0)
            tk.Label(result_window, text=employee.age).grid(row=5, column=1)
            tk.Label(result_window, text="Date of Birth:").grid(row=6, column=0)
            tk.Label(result_window, text=employee.date_of_birth).grid(row=6, column=1)
            tk.Label(result_window, text="Passport Details:").grid(row=7, column=0)
            tk.Label(result_window, text=employee.passport_details).grid(row=7, column=1)
            break

    if not found:
        tk.Label(result_window, text="Employee not found").pack()

class EventManagement(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.display_button = None
        self.modify_button = None
        self.events = None
        self.delete_button = None
        self.add_button = None
        self.event_listbox = None
        self.title("Event Management System")
        self.geometry("800x600")
        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.events = []
        if os.path.exists("events.pkl"):
            with open("events.pkl", "rb") as file:
                self.events = pickle.load(file)

    def save_data(self):
        with open("events.pkl", "wb") as file:
            pickle.dump(self.events, file)

    def create_widgets(self):
        self.event_listbox = tk.Listbox(self, width=100, height=20)
        self.event_listbox.pack()

        self.add_button = tk.Button(self, text="Add Event", command=self.add_event)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Event", command=self.delete_event)
        self.delete_button.pack()

        self.modify_button = tk.Button(self, text="Modify Event", command=self.modify_event)
        self.modify_button.pack()

        self.display_button = tk.Button(self, text="Display Events", command=self.display_events)
        self.display_button.pack()
        self.search_button = tk.Button(self, text="Search Event", command=self.search_event)
        self.search_button.pack()

    def add_event(self):
        add_event_window = tk.Toplevel(self)
        add_event_window.title("Add Event")

        # Add labels and entry fields for event attributes

        # Event ID
        tk.Label(add_event_window, text="Event ID:").grid(row=0, column=0)
        event_id_entry = tk.Entry(add_event_window)
        event_id_entry.grid(row=0, column=1)

        # Event Type
        tk.Label(add_event_window, text="Event Type:").grid(row=1, column=0)
        event_type_entry = tk.Entry(add_event_window)
        event_type_entry.grid(row=1, column=1)

        # Theme
        tk.Label(add_event_window, text="Theme:").grid(row=2, column=0)
        theme_entry = tk.Entry(add_event_window)
        theme_entry.grid(row=2, column=1)

        # Date
        tk.Label(add_event_window, text="Date:").grid(row=3, column=0)
        date_entry = tk.Entry(add_event_window)
        date_entry.grid(row=3, column=1)

        # Time
        tk.Label(add_event_window, text="Time:").grid(row=4, column=0)
        time_entry = tk.Entry(add_event_window)
        time_entry.grid(row=4, column=1)

        # Duration
        tk.Label(add_event_window, text="Duration:").grid(row=5, column=0)
        duration_entry = tk.Entry(add_event_window)
        duration_entry.grid(row=5, column=1)

        # Venue Address
        tk.Label(add_event_window, text="Venue Address:").grid(row=6, column=0)
        venue_address_entry = tk.Entry(add_event_window)
        venue_address_entry.grid(row=6, column=1)

        # Client ID
        tk.Label(add_event_window, text="Client ID:").grid(row=7, column=0)
        client_id_entry = tk.Entry(add_event_window)
        client_id_entry.grid(row=7, column=1)

        # Guest List
        tk.Label(add_event_window, text="Guest List:").grid(row=8, column=0)
        guest_list_entry = tk.Entry(add_event_window)
        guest_list_entry.grid(row=8, column=1)

        # Suppliers
        tk.Label(add_event_window, text="Suppliers:").grid(row=9, column=0)
        suppliers_entry = tk.Entry(add_event_window)
        suppliers_entry.grid(row=9, column=1)

        # Invoice
        tk.Label(add_event_window, text="Invoice:").grid(row=10, column=0)
        invoice_entry = tk.Entry(add_event_window)
        invoice_entry.grid(row=10, column=1)

        # Submit button
        submit_button = tk.Button(add_event_window, text="Submit",
                                  command=lambda: self.submit_add_event(event_id_entry.get(), event_type_entry.get(),
                                                                       theme_entry.get(), date_entry.get(),
                                                                       time_entry.get(), duration_entry.get(),
                                                                       venue_address_entry.get(), client_id_entry.get(),
                                                                       guest_list_entry.get(), suppliers_entry.get(),
                                                                       invoice_entry.get()))
        submit_button.grid(row=11, column=0, columnspan=2)

    def submit_add_event(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                         suppliers, invoice):
        # Create an Event object and add it to the events list
        event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list,
                      suppliers, invoice)
        self.events.append(event)
        self.save_data()
        self.display_events()

    def delete_event(self):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.events[index]
            self.save_data()
            self.display_events()
            messagebox.showinfo("Success", "Event deleted successfully")
        else:
            messagebox.showerror("Error", "Please select an event to delete")

    def modify_event(self):
        selected_index = self.event_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            event = self.events[index]
            modify_event_window = tk.Toplevel(self)
            modify_event_window.title("Modify Event")

            # Add labels and entry fields pre-filled with existing event attributes

            # Event ID
            tk.Label(modify_event_window, text="Event ID:").grid(row=0, column=0)
            event_id_entry = tk.Entry(modify_event_window)
            event_id_entry.grid(row=0, column=1)
            event_id_entry.insert(0, event.event_id)

            # Event Type
            tk.Label(modify_event_window, text="Event Type:").grid(row=1, column=0)
            event_type_entry = tk.Entry(modify_event_window)
            event_type_entry.grid(row=1, column=1)
            event_type_entry.insert(0, event.event_type)

            # Theme
            tk.Label(modify_event_window, text="Theme:").grid(row=2, column=0)
            theme_entry = tk.Entry(modify_event_window)
            theme_entry.grid(row=2, column=1)
            theme_entry.insert(0, event.theme)

            # Date
            tk.Label(modify_event_window, text="Date:").grid(row=3, column=0)
            date_entry = tk.Entry(modify_event_window)
            date_entry.grid(row=3, column=1)
            date_entry.insert(0, event.date)

            # Time
            tk.Label(modify_event_window, text="Time:").grid(row=4, column=0)
            time_entry = tk.Entry(modify_event_window)
            time_entry.grid(row=4, column=1)
            time_entry.insert(0, event.time)

            # Duration
            tk.Label(modify_event_window, text="Duration:").grid(row=5, column=0)
            duration_entry = tk.Entry(modify_event_window)
            duration_entry.grid(row=5, column=1)
            duration_entry.insert(0, event.duration)

            # Venue Address
            tk.Label(modify_event_window, text="Venue Address:").grid(row=6, column=0)
            venue_address_entry = tk.Entry(modify_event_window)
            venue_address_entry.grid(row=6, column=1)
            venue_address_entry.insert(0, event.venue_address)

            # Client ID
            tk.Label(modify_event_window, text="Client ID:").grid(row=7, column=0)
            client_id_entry = tk.Entry(modify_event_window)
            client_id_entry.grid(row=7, column=1)
            client_id_entry.insert(0, event.client_id)

            # Guest List
            tk.Label(modify_event_window, text="Guest List:").grid(row=8, column=0)
            guest_list_entry = tk.Entry(modify_event_window)
            guest_list_entry.grid(row=8, column=1)
            guest_list_entry.insert(0, event.guest_list)

            # Suppliers
            tk.Label(modify_event_window, text="Suppliers:").grid(row=9, column=0)
            suppliers_entry = tk.Entry(modify_event_window)
            suppliers_entry.grid(row=9, column=1)
            suppliers_entry.insert(0, event.suppliers)

            # Invoice
            tk.Label(modify_event_window, text="Invoice:").grid(row=10, column=0)
            invoice_entry = tk.Entry(modify_event_window)
            invoice_entry.grid(row=10, column=1)
            invoice_entry.insert(0, event.invoice)

            # Submit button
            submit_button = tk.Button(modify_event_window, text="Submit",
                                      command=lambda: self.submit_modify_event(index, event_id_entry.get(),
                                                                              event_type_entry.get(), theme_entry.get(),
                                                                              date_entry.get(), time_entry.get(),
                                                                              duration_entry.get(),
                                                                              venue_address_entry.get(),
                                                                              client_id_entry.get(),
                                                                              guest_list_entry.get(),
                                                                              suppliers_entry.get(), invoice_entry.get()))
            submit_button.grid(row=11, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Please select an event to modify")

    def submit_modify_event(self, index, event_id, event_type, theme, date, time, duration, venue_address, client_id,
                            guest_list, suppliers, invoice):
        event = self.events[index]
        event.event_id = event_id
        event.event_type = event_type
        event.theme = theme
        event.date = date
        event.time = time
        event.duration = duration
        event.venue_address = venue_address
        event.client_id = client_id
        event.guest_list = guest_list
        event.suppliers = suppliers
        event.invoice = invoice
        self.save_data()
        messagebox.showinfo("Success", "Event modified successfully")
        self.display_events()

    def display_events(self):
        self.event_listbox.delete(0, tk.END)
        for event in self.events:
            self.event_listbox.insert(tk.END, f"ID: {event.event_id}, Type: {event.event_type}, Theme: {event.theme}, Date: {event.date}, Time: {event.time}, Duration: {event.duration}, Venue: {event.venue_address}, Client ID: {event.client_id}, Guest List: {event.guest_list}, Suppliers: {event.suppliers}, Invoice: {event.invoice}")

    def search_event(self):
        search_window = tk.Toplevel(self)
        search_window.title("Search Event")

        tk.Label(search_window, text="Event ID:").grid(row=0, column=0)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search",
                                  command=lambda: self.display_search_result(id_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2)

    def display_search_result(self, event_id, search_window):
        result_window = tk.Toplevel(search_window)
        result_window.title("Search Result")

        found = False
        for event in self.events:
            if event.event_id == event_id:
                found = True
                tk.Label(result_window, text="Event ID:").grid(row=0, column=0)
                tk.Label(result_window, text=event.event_id).grid(row=0, column=1)
                tk.Label(result_window, text="Type:").grid(row=1, column=0)
                tk.Label(result_window, text=event.event_type).grid(row=1, column=1)
                tk.Label(result_window, text="Theme:").grid(row=2, column=0)
                tk.Label(result_window, text=event.theme).grid(row=2, column=1)
                tk.Label(result_window, text="Date:").grid(row=3, column=0)
                tk.Label(result_window, text=event.date).grid(row=3, column=1)
                tk.Label(result_window, text="Time:").grid(row=4, column=0)
                tk.Label(result_window, text=event.time).grid(row=4, column=1)
                tk.Label(result_window, text="Duration:").grid(row=5, column=0)
                tk.Label(result_window, text=event.duration).grid(row=5, column=1)
                tk.Label(result_window, text="Venue Address:").grid(row=6, column=0)
                tk.Label(result_window, text=event.venue_address).grid(row=6, column=1)
                tk.Label(result_window, text="Client ID:").grid(row=7, column=0)
                tk.Label(result_window, text=event.client_id).grid(row=7, column=1)
                tk.Label(result_window, text="Guest List:").grid(row=8, column=0)
                tk.Label(result_window, text=", ".join(event.guest_list)).grid(row=8, column=1)
                tk.Label(result_window, text="Suppliers:").grid(row=9, column=0)
                tk.Label(result_window, text=", ".join(event.suppliers)).grid(row=9, column=1)
                tk.Label(result_window, text="Invoice:").grid(row=10, column=0)
                tk.Label(result_window, text=event.invoice).grid(row=10, column=1)
                break

        if not found:
            tk.Label(result_window, text="Event not found").pack()


class ClientManagement(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.display_button = None
        self.modify_button = None
        self.clients = None
        self.delete_button = None
        self.add_button = None
        self.client_listbox = None
        self.title("Client Management System")
        self.geometry("800x600")
        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.clients = []
        if os.path.exists("clients.pkl"):
            with open("clients.pkl", "rb") as file:
                self.clients = pickle.load(file)

    def save_data(self):
        with open("clients.pkl", "wb") as file:
            pickle.dump(self.clients, file)

    def create_widgets(self):
        self.client_listbox = tk.Listbox(self, width=100, height=20)
        self.client_listbox.pack()

        self.add_button = tk.Button(self, text="Add Client", command=self.add_client)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Client", command=self.delete_client)
        self.delete_button.pack()

        self.modify_button = tk.Button(self, text="Modify Client", command=self.modify_client)
        self.modify_button.pack()

        self.display_button = tk.Button(self, text="Display Clients", command=self.display_clients)
        self.display_button.pack()
        self.search_button = tk.Button(self, text="Search Client", command=self.search_client)
        self.search_button.pack()

    def add_client(self):
        add_client_window = tk.Toplevel(self)
        add_client_window.title("Add Client")

        # Add labels and entry fields for client attributes

        # Client ID
        tk.Label(add_client_window, text="Client ID:").grid(row=0, column=0)
        client_id_entry = tk.Entry(add_client_window)
        client_id_entry.grid(row=0, column=1)

        # Name
        tk.Label(add_client_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_client_window)
        name_entry.grid(row=1, column=1)

        # Address
        tk.Label(add_client_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(add_client_window)
        address_entry.grid(row=2, column=1)

        # Contact Details
        tk.Label(add_client_window, text="Contact Details:").grid(row=3, column=0)
        contact_details_entry = tk.Entry(add_client_window)
        contact_details_entry.grid(row=3, column=1)

        # Budget
        tk.Label(add_client_window, text="Budget:").grid(row=4, column=0)
        budget_entry = tk.Entry(add_client_window)
        budget_entry.grid(row=4, column=1)

        # Submit button
        submit_button = tk.Button(add_client_window, text="Submit",
                                  command=lambda: self.submit_add_client(client_id_entry.get(), name_entry.get(),
                                                                        address_entry.get(), contact_details_entry.get(),
                                                                        budget_entry.get()))
        submit_button.grid(row=5, column=0, columnspan=2)

    def submit_add_client(self, client_id, name, address, contact_details, budget):
        # Create a Client object and add it to the clients list
        client = Client(client_id, name, address, contact_details, budget)
        self.clients.append(client)
        self.save_data()
        self.display_clients()

    def delete_client(self):
        selected_index = self.client_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.clients[index]
            self.save_data()
            self.display_clients()
            messagebox.showinfo("Success", "Client deleted successfully")
        else:
            messagebox.showerror("Error", "Please select a client to delete")

    def modify_client(self):
        selected_index = self.client_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            client = self.clients[index]
            modify_client_window = tk.Toplevel(self)
            modify_client_window.title("Modify Client")

            # Add labels and entry fields pre-filled with existing client attributes

            # Client ID
            tk.Label(modify_client_window, text="Client ID:").grid(row=0, column=0)
            client_id_entry = tk.Entry(modify_client_window)
            client_id_entry.grid(row=0, column=1)
            client_id_entry.insert(0, client.client_id)

            # Name
            tk.Label(modify_client_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(modify_client_window)
            name_entry.grid(row=1, column=1)
            name_entry.insert(0, client.name)

            # Address
            tk.Label(modify_client_window, text="Address:").grid(row=2, column=0)
            address_entry = tk.Entry(modify_client_window)
            address_entry.grid(row=2, column=1)
            address_entry.insert(0, client.address)

            # Contact Details
            tk.Label(modify_client_window, text="Contact Details:").grid(row=3, column=0)
            contact_details_entry = tk.Entry(modify_client_window)
            contact_details_entry.grid(row=3, column=1)
            contact_details_entry.insert(0, client.contact_details)

            # Budget
            tk.Label(modify_client_window, text="Budget:").grid(row=4, column=0)
            budget_entry = tk.Entry(modify_client_window)
            budget_entry.grid(row=4, column=1)
            budget_entry.insert(0, client.budget)

            # Submit button
            submit_button = tk.Button(modify_client_window, text="Submit",
                                      command=lambda: self.submit_modify_client(index, client_id_entry.get(),
                                                                              name_entry.get(), address_entry.get(),
                                                                              contact_details_entry.get(), budget_entry.get()))
            submit_button.grid(row=5, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Please select a client to modify")

    def submit_modify_client(self, index, client_id, name, address, contact_details, budget):
        client = self.clients[index]
        client.client_id = client_id
        client.name = name
        client.address = address
        client.contact_details = contact_details
        client.budget = budget
        self.save_data()
        messagebox.showinfo("Success", "Client modified successfully")
        self.display_clients()

    def display_clients(self):
        self.client_listbox.delete(0, tk.END)
        for client in self.clients:
            self.client_listbox.insert(tk.END, f"ID: {client.client_id}, Name: {client.name}, Address: {client.address}, Contact: {client.contact_details}, Budget: {client.budget}")

    def search_client(self):
        search_window = tk.Toplevel(self)
        search_window.title("Search Client")

        tk.Label(search_window, text="Client ID:").grid(row=0, column=0)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search",
                                  command=lambda: self.display_search_result(id_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2)

    def display_search_result(self, client_id, search_window):
        result_window = tk.Toplevel(search_window)
        result_window.title("Search Result")

        found = False
        for client in self.clients:
            if client.client_id == client_id:
                found = True
                tk.Label(result_window, text="Client ID:").grid(row=0, column=0)
                tk.Label(result_window, text=client.client_id).grid(row=0, column=1)
                tk.Label(result_window, text="Name:").grid(row=1, column=0)
                tk.Label(result_window, text=client.name).grid(row=1, column=1)
                tk.Label(result_window, text="Address:").grid(row=2, column=0)
                tk.Label(result_window, text=client.address).grid(row=2, column=1)
                tk.Label(result_window, text="Contact Details:").grid(row=3, column=0)
                tk.Label(result_window, text=client.contact_details).grid(row=3, column=1)
                tk.Label(result_window, text="Budget:").grid(row=4, column=0)
                tk.Label(result_window, text=client.budget).grid(row=4, column=1)
                break

        if not found:
            tk.Label(result_window, text="Client not found").pack()


class GuestManagement(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.display_button = None
        self.modify_button = None
        self.guests = None
        self.delete_button = None
        self.add_button = None
        self.guest_listbox = None
        self.title("Guest Management System")
        self.geometry("800x600")
        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.guests = []
        if os.path.exists("guests.pkl"):
            with open("guests.pkl", "rb") as file:
                self.guests = pickle.load(file)

    def save_data(self):
        with open("guests.pkl", "wb") as file:
            pickle.dump(self.guests, file)

    def create_widgets(self):
        self.guest_listbox = tk.Listbox(self, width=100, height=20)
        self.guest_listbox.pack()

        self.add_button = tk.Button(self, text="Add Guest", command=self.add_guest)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Guest", command=self.delete_guest)
        self.delete_button.pack()

        self.modify_button = tk.Button(self, text="Modify Guest", command=self.modify_guest)
        self.modify_button.pack()

        self.display_button = tk.Button(self, text="Display Guests", command=self.display_guests)
        self.display_button.pack()
        self.search_button = tk.Button(self, text="Search Guest", command=self.search_guest)
        self.search_button.pack()

    def add_guest(self):
        add_guest_window = tk.Toplevel(self)
        add_guest_window.title("Add Guest")

        # Add labels and entry fields for guest attributes

        # Guest ID
        tk.Label(add_guest_window, text="Guest ID:").grid(row=0, column=0)
        guest_id_entry = tk.Entry(add_guest_window)
        guest_id_entry.grid(row=0, column=1)

        # Name
        tk.Label(add_guest_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_guest_window)
        name_entry.grid(row=1, column=1)

        # Address
        tk.Label(add_guest_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(add_guest_window)
        address_entry.grid(row=2, column=1)

        # Contact Details
        tk.Label(add_guest_window, text="Contact Details:").grid(row=3, column=0)
        contact_details_entry = tk.Entry(add_guest_window)
        contact_details_entry.grid(row=3, column=1)

        # Submit button
        submit_button = tk.Button(add_guest_window, text="Submit",
                                  command=lambda: self.submit_add_guest(guest_id_entry.get(), name_entry.get(),
                                                                        address_entry.get(), contact_details_entry.get()))
        submit_button.grid(row=4, column=0, columnspan=2)

    def submit_add_guest(self, guest_id, name, address, contact_details):
        # Create a Guest object and add it to the guests list
        guest = Guest(guest_id, name, address, contact_details)
        self.guests.append(guest)
        self.save_data()
        self.display_guests()

    def delete_guest(self):
        selected_index = self.guest_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.guests[index]
            self.save_data()
            self.display_guests()
            messagebox.showinfo("Success", "Guest deleted successfully")
        else:
            messagebox.showerror("Error", "Please select a guest to delete")

    def modify_guest(self):
        selected_index = self.guest_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            guest = self.guests[index]
            modify_guest_window = tk.Toplevel(self)
            modify_guest_window.title("Modify Guest")

            # Add labels and entry fields pre-filled with existing guest attributes

            # Guest ID
            tk.Label(modify_guest_window, text="Guest ID:").grid(row=0, column=0)
            guest_id_entry = tk.Entry(modify_guest_window)
            guest_id_entry.grid(row=0, column=1)
            guest_id_entry.insert(0, guest.guest_id)

            # Name
            tk.Label(modify_guest_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(modify_guest_window)
            name_entry.grid(row=1, column=1)
            name_entry.insert(0, guest.name)

            # Address
            tk.Label(modify_guest_window, text="Address:").grid(row=2, column=0)
            address_entry = tk.Entry(modify_guest_window)
            address_entry.grid(row=2, column=1)
            address_entry.insert(0, guest.address)

            # Contact Details
            tk.Label(modify_guest_window, text="Contact Details:").grid(row=3, column=0)
            contact_details_entry = tk.Entry(modify_guest_window)
            contact_details_entry.grid(row=3, column=1)
            contact_details_entry.insert(0, guest.contact_details)

            # Submit button
            submit_button = tk.Button(modify_guest_window, text="Submit",
                                      command=lambda: self.submit_modify_guest(index, guest_id_entry.get(),
                                                                              name_entry.get(), address_entry.get(),
                                                                              contact_details_entry.get()))
            submit_button.grid(row=4, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Please select a guest to modify")

    def submit_modify_guest(self, index, guest_id, name, address, contact_details):
        guest = self.guests[index]
        guest.guest_id = guest_id
        guest.name = name
        guest.address = address
        guest.contact_details = contact_details
        self.save_data()
        messagebox.showinfo("Success", "Guest modified successfully")
        self.display_guests()

    def display_guests(self):
        self.guest_listbox.delete(0, tk.END)
        for guest in self.guests:
            self.guest_listbox.insert(tk.END, f"ID: {guest.guest_id}, Name: {guest.name}, Address: {guest.address}, Contact: {guest.contact_details}")

    def search_guest(self):
        search_window = tk.Toplevel(self)
        search_window.title("Search Guest")

        tk.Label(search_window, text="Guest ID:").grid(row=0, column=0)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search",
                                  command=lambda: self.display_search_result(id_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2)

    def display_search_result(self, guest_id, search_window):
        result_window = tk.Toplevel(search_window)
        result_window.title("Search Result")

        found = False
        for guest in self.guests:
            if guest.guest_id == guest_id:
                found = True
                tk.Label(result_window, text="Guest ID:").grid(row=0, column=0)
                tk.Label(result_window, text=guest.guest_id).grid(row=0, column=1)
                tk.Label(result_window, text="Name:").grid(row=1, column=0)
                tk.Label(result_window, text=guest.name).grid(row=1, column=1)
                tk.Label(result_window, text="Address:").grid(row=2, column=0)
                tk.Label(result_window, text=guest.address).grid(row=2, column=1)
                tk.Label(result_window, text="Contact Details:").grid(row=3, column=0)
                tk.Label(result_window, text=guest.contact_details).grid(row=3, column=1)
                break

        if not found:
            tk.Label(result_window, text="Guest not found").pack()


class SupplierManagement(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.display_button = None
        self.modify_button = None
        self.suppliers = None
        self.delete_button = None
        self.add_button = None
        self.supplier_listbox = None
        self.title("Supplier Management System")
        self.geometry("800x600")
        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.suppliers = []
        if os.path.exists("suppliers.pkl"):
            with open("suppliers.pkl", "rb") as file:
                self.suppliers = pickle.load(file)

    def save_data(self):
        with open("suppliers.pkl", "wb") as file:
            pickle.dump(self.suppliers, file)

    def create_widgets(self):
        self.supplier_listbox = tk.Listbox(self, width=100, height=20)
        self.supplier_listbox.pack()

        self.add_button = tk.Button(self, text="Add Supplier", command=self.add_supplier)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Supplier", command=self.delete_supplier)
        self.delete_button.pack()

        self.modify_button = tk.Button(self, text="Modify Supplier", command=self.modify_supplier)
        self.modify_button.pack()

        self.display_button = tk.Button(self, text="Display Suppliers", command=self.display_suppliers)
        self.display_button.pack()
        self.search_button = tk.Button(self, text="Search Supplier", command=self.search_supplier)
        self.search_button.pack()

    def add_supplier(self):
        add_supplier_window = tk.Toplevel(self)
        add_supplier_window.title("Add Supplier")

        # Add labels and entry fields for supplier attributes

        # Supplier ID
        tk.Label(add_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        supplier_id_entry = tk.Entry(add_supplier_window)
        supplier_id_entry.grid(row=0, column=1)

        # Name
        tk.Label(add_supplier_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_supplier_window)
        name_entry.grid(row=1, column=1)

        # Address
        tk.Label(add_supplier_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(add_supplier_window)
        address_entry.grid(row=2, column=1)

        # Contact Details
        tk.Label(add_supplier_window, text="Contact Details:").grid(row=3, column=0)
        contact_details_entry = tk.Entry(add_supplier_window)
        contact_details_entry.grid(row=3, column=1)

        # Booking Availability
        tk.Label(add_supplier_window, text="Booking Availability:").grid(row=4, column=0)
        booking_availability_entry = tk.Entry(add_supplier_window)
        booking_availability_entry.grid(row=4, column=1)

        # Staff Number
        tk.Label(add_supplier_window, text="Staff Number:").grid(row=5, column=0)
        staff_number_entry = tk.Entry(add_supplier_window)
        staff_number_entry.grid(row=5, column=1)

        # Submit button
        submit_button = tk.Button(add_supplier_window, text="Submit",
                                  command=lambda: self.submit_add_supplier(supplier_id_entry.get(), name_entry.get(),
                                                                           address_entry.get(),
                                                                           contact_details_entry.get(),
                                                                           booking_availability_entry.get(),
                                                                           staff_number_entry.get()))
        submit_button.grid(row=6, column=0, columnspan=2)

    def submit_add_supplier(self, supplier_id, name, address, contact_details, booking_availability, staff_number):
        # Create a Supplier object and add it to the suppliers list
        supplier = Supplier(supplier_id, name, address, contact_details, booking_availability, staff_number)
        self.suppliers.append(supplier)
        self.save_data()
        self.display_suppliers()
    def delete_supplier(self):
        selected_index = self.supplier_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.suppliers[index]
            self.save_data()
            self.display_suppliers()
            messagebox.showinfo("Success", "Supplier deleted successfully")
        else:
            messagebox.showerror("Error", "Please select a supplier to delete")

    def modify_supplier(self):
        selected_index = self.supplier_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            supplier = self.suppliers[index]
            modify_supplier_window = tk.Toplevel(self)
            modify_supplier_window.title("Modify Supplier")

            # Add labels and entry fields pre-filled with existing supplier attributes

            # Supplier ID
            tk.Label(modify_supplier_window, text="Supplier ID:").grid(row=0, column=0)
            supplier_id_entry = tk.Entry(modify_supplier_window)
            supplier_id_entry.grid(row=0, column=1)
            supplier_id_entry.insert(0, supplier.supplier_id)

            # Name
            tk.Label(modify_supplier_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(modify_supplier_window)
            name_entry.grid(row=1, column=1)
            name_entry.insert(0, supplier.name)

            # Address
            tk.Label(modify_supplier_window, text="Address:").grid(row=2, column=0)
            address_entry = tk.Entry(modify_supplier_window)
            address_entry.grid(row=2, column=1)
            address_entry.insert(0, supplier.address)

            # Contact Details
            tk.Label(modify_supplier_window, text="Contact Details:").grid(row=3, column=0)
            contact_details_entry = tk.Entry(modify_supplier_window)
            contact_details_entry.grid(row=3, column=1)
            contact_details_entry.insert(0, supplier.contact_details)

            # Submit button
            submit_button = tk.Button(modify_supplier_window, text="Submit",
                                      command=lambda: self.submit_modify_supplier(index, supplier_id_entry.get(),
                                                                              name_entry.get(), address_entry.get(),
                                                                              contact_details_entry.get()))
            submit_button.grid(row=4, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Please select a supplier to modify")

    def submit_modify_supplier(self, index, supplier_id, name, address, contact_details):
        supplier = self.suppliers[index]
        supplier.supplier_id = supplier_id
        supplier.name = name
        supplier.address = address
        supplier.contact_details = contact_details
        self.save_data()
        messagebox.showinfo("Success", "Supplier modified successfully")
        self.display_suppliers()

    def display_suppliers(self):
        self.supplier_listbox.delete(0, tk.END)
        for supplier in self.suppliers:
            self.supplier_listbox.insert(tk.END, f"ID: {supplier.supplier_id}, Name: {supplier.name}, Address: {supplier.address}, Contact: {supplier.contact_details}")

    def search_supplier(self):
        search_window = tk.Toplevel(self)
        search_window.title("Search Supplier")

        tk.Label(search_window, text="Supplier ID:").grid(row=0, column=0)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search",
                                  command=lambda: self.display_search_result(id_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2)

    def display_search_result(self, supplier_id, search_window):
        result_window = tk.Toplevel(search_window)
        result_window.title("Search Result")

        found = False
        for supplier in self.suppliers:
            if supplier.supplier_id == supplier_id:
                found = True
                tk.Label(result_window, text="Supplier ID:").grid(row=0, column=0)
                tk.Label(result_window, text=supplier.supplier_id).grid(row=0, column=1)
                tk.Label(result_window, text="Name:").grid(row=1, column=0)
                tk.Label(result_window, text=supplier.name).grid(row=1, column=1)
                tk.Label(result_window, text="Address:").grid(row=2, column=0)
                tk.Label(result_window, text=supplier.address).grid(row=2, column=1)
                tk.Label(result_window, text="Contact Details:").grid(row=3, column=0)
                tk.Label(result_window, text=supplier.contact_details).grid(row=3, column=1)
                break

        if not found:
            tk.Label(result_window, text="Supplier not found").pack()


class VenueManagement(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.display_button = None
        self.modify_button = None
        self.venues = None
        self.delete_button = None
        self.add_button = None
        self.venue_listbox = None
        self.title("Venue Management System")
        self.geometry("800x600")
        self.load_data()
        self.create_widgets()

    def load_data(self):
        self.venues = []
        if os.path.exists("venues.pkl"):
            with open("venues.pkl", "rb") as file:
                self.venues = pickle.load(file)

    def save_data(self):
        with open("venues.pkl", "wb") as file:
            pickle.dump(self.venues, file)

    def create_widgets(self):
        self.venue_listbox = tk.Listbox(self, width=100, height=20)
        self.venue_listbox.pack()

        self.add_button = tk.Button(self, text="Add Venue", command=self.add_venue)
        self.add_button.pack()

        self.delete_button = tk.Button(self, text="Delete Venue", command=self.delete_venue)
        self.delete_button.pack()

        self.modify_button = tk.Button(self, text="Modify Venue", command=self.modify_venue)
        self.modify_button.pack()

        self.display_button = tk.Button(self, text="Display Venues", command=self.display_venues)
        self.display_button.pack()
        self.search_button = tk.Button(self, text="Search Venue", command=self.search_venue)
        self.search_button.pack()

    def add_venue(self):
        add_venue_window = tk.Toplevel(self)
        add_venue_window.title("Add Venue")

        # Add labels and entry fields for venue attributes

        # Venue ID
        tk.Label(add_venue_window, text="Venue ID:").grid(row=0, column=0)
        venue_id_entry = tk.Entry(add_venue_window)
        venue_id_entry.grid(row=0, column=1)

        # Name
        tk.Label(add_venue_window, text="Name:").grid(row=1, column=0)
        name_entry = tk.Entry(add_venue_window)
        name_entry.grid(row=1, column=1)

        # Address
        tk.Label(add_venue_window, text="Address:").grid(row=2, column=0)
        address_entry = tk.Entry(add_venue_window)
        address_entry.grid(row=2, column=1)

        # Contact
        tk.Label(add_venue_window, text="Contact:").grid(row=3, column=0)
        contact_entry = tk.Entry(add_venue_window)
        contact_entry.grid(row=3, column=1)

        # Minimum Guests
        tk.Label(add_venue_window, text="Minimum Guests:").grid(row=4, column=0)
        min_guests_entry = tk.Entry(add_venue_window)
        min_guests_entry.grid(row=4, column=1)

        # Maximum Guests
        tk.Label(add_venue_window, text="Maximum Guests:").grid(row=5, column=0)
        max_guests_entry = tk.Entry(add_venue_window)
        max_guests_entry.grid(row=5, column=1)

        # Submit button
        submit_button = tk.Button(add_venue_window, text="Submit",
                                  command=lambda: self.submit_add_venue(venue_id_entry.get(), name_entry.get(),
                                                                        address_entry.get(), contact_entry.get(),
                                                                        min_guests_entry.get(), max_guests_entry.get()))
        submit_button.grid(row=6, column=0, columnspan=2)

    def submit_add_venue(self, venue_id, name, address, contact, min_guests, max_guests):
        # Create a Venue object and add it to the venues list
        venue = Venue(venue_id, name, address, contact, min_guests, max_guests)
        self.venues.append(venue)
        self.save_data()
        self.display_venues()

    def delete_venue(self):
        selected_index = self.venue_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.venues[index]
            self.save_data()
            self.display_venues()
            messagebox.showinfo("Success", "Venue deleted successfully")
        else:
            messagebox.showerror("Error", "Please select a venue to delete")

    def modify_venue(self):
        selected_index = self.venue_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            venue = self.venues[index]
            modify_venue_window = tk.Toplevel(self)
            modify_venue_window.title("Modify Venue")

            # Add labels and entry fields pre-filled with existing venue attributes

            # Venue ID
            tk.Label(modify_venue_window, text="Venue ID:").grid(row=0, column=0)
            venue_id_entry = tk.Entry(modify_venue_window)
            venue_id_entry.grid(row=0, column=1)
            venue_id_entry.insert(0, venue.venue_id)

            # Name
            tk.Label(modify_venue_window, text="Name:").grid(row=1, column=0)
            name_entry = tk.Entry(modify_venue_window)
            name_entry.grid(row=1, column=1)
            name_entry.insert(0, venue.name)

            # Address
            tk.Label(modify_venue_window, text="Address:").grid(row=2, column=0)
            address_entry = tk.Entry(modify_venue_window)
            address_entry.grid(row=2, column=1)
            address_entry.insert(0, venue.address)

            # Contact
            tk.Label(modify_venue_window, text="Contact:").grid(row=3, column=0)
            contact_entry = tk.Entry(modify_venue_window)
            contact_entry.grid(row=3, column=1)
            contact_entry.insert(0, venue.contact)

            # Minimum Guests
            tk.Label(modify_venue_window, text="Minimum Guests:").grid(row=4, column=0)
            min_guests_entry = tk.Entry(modify_venue_window)
            min_guests_entry.grid(row=4, column=1)
            min_guests_entry.insert(0, venue.min_guests)

            # Maximum Guests
            tk.Label(modify_venue_window, text="Maximum Guests:").grid(row=5, column=0)
            max_guests_entry = tk.Entry(modify_venue_window)
            max_guests_entry.grid(row=5, column=1)
            max_guests_entry.insert(0, venue.max_guests)

            # Submit button
            submit_button = tk.Button(modify_venue_window, text="Submit",
                                      command=lambda: self.submit_modify_venue(index, venue_id_entry.get(),
                                                                              name_entry.get(), address_entry.get(),
                                                                              contact_entry.get(), min_guests_entry.get(),
                                                                              max_guests_entry.get()))
            submit_button.grid(row=6, column=0, columnspan=2)
        else:
            messagebox.showerror("Error", "Please select a venue to modify")

    def submit_modify_venue(self, index, venue_id, name, address, contact, min_guests, max_guests):
        venue = self.venues[index]
        venue.venue_id = venue_id
        venue.name = name
        venue.address = address
        venue.contact = contact
        venue.min_guests = min_guests
        venue.max_guests = max_guests
        self.save_data()
        messagebox.showinfo("Success", "Venue modified successfully")
        self.display_venues()

    def display_venues(self):
        self.venue_listbox.delete(0, tk.END)
        for venue in self.venues:
            self.venue_listbox.insert(tk.END, f"ID: {venue.venue_id}, Name: {venue.name}, Address: {venue.address}, Contact: {venue.contact}, Min Guests: {venue.min_guests}, Max Guests: {venue.max_guests}")

    def search_venue(self):
        search_window = tk.Toplevel(self)
        search_window.title("Search Venue")

        tk.Label(search_window, text="Venue ID:").grid(row=0, column=0)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1)

        search_button = tk.Button(search_window, text="Search",
                                  command=lambda: self.display_search_result(id_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2)

    def display_search_result(self, venue_id, search_window):
        result_window = tk.Toplevel(search_window)
        result_window.title("Search Result")

        found = False
        for venue in self.venues:
            if venue.venue_id == venue_id:
                found = True
                tk.Label(result_window, text="Venue ID:").grid(row=0, column=0)
                tk.Label(result_window, text=venue.venue_id).grid(row=0, column=1)
                tk.Label(result_window, text="Name:").grid(row=1, column=0)
                tk.Label(result_window, text=venue.name).grid(row=1, column=1)
                tk.Label(result_window, text="Address:").grid(row=2, column=0)
                tk.Label(result_window, text=venue.address).grid(row=2, column=1)
                tk.Label(result_window, text="Contact:").grid(row=3, column=0)
                tk.Label(result_window, text=venue.contact).grid(row=3, column=1)
                tk.Label(result_window, text="Minimum Guests:").grid(row=4, column=0)
                tk.Label(result_window, text=venue.min_guests).grid(row=4, column=1)
                tk.Label(result_window, text="Maximum Guests:").grid(row=5, column=0)
                tk.Label(result_window, text=venue.max_guests).grid(row=5, column=1)
                break

        if not found:
            tk.Label(result_window, text="Venue not found").pack()


if __name__ == "__main__":
    gui = GUI()
    gui.run()