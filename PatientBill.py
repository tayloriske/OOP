import PatientClass as pat
import ProcedureClass as pro

def main():

    ID = 1
    Name = "Matt Jones"
    Address = "123 Main st, Waco TX 76706"
    Phone = "254-555-7415"
    Veteran_status = True

    patient = pat.Patient(ID, Name, Address, Phone, Veteran_status)

    patient.get_ID()
    patient.get_name()
    patient.get_address()
    patient.get_phone()
    patient.get_veteran_status()

    name = "Physical Exam"
    date = "2/15/2022"
    practioner = "Dr. Irvine"
    charge = 250
    patient_id = 1

    procedure = pro.Procedure(name, date, practioner, charge, patient_id)

    procedure.get_Procedure()
    procedure.get_Date()
    procedure.get_Practitioner()
    procedure.get_Charges()
    procedure.get_PatientID()

    name = "MRI"
    date = "2/15/2022"
    practioner = "Dr. Hamilton"
    charge = 1500
    patient_id = 1

    procedure2 = pro.Procedure(name, date, practioner, charge, patient_id)

    procedure2.get_Procedure()
    procedure2.get_Date()
    procedure2.get_Practitioner()
    procedure2.get_Charges()
    procedure2.get_PatientID()

    name = "CT Scan"
    date = "2/17/2022"
    practioner = "Dr. Drey"
    charge = 1200
    patient_id = 2

    procedure3 = pro.Procedure(name, date, practioner, charge, patient_id)

    procedure3.get_Procedure()
    procedure3.get_Date()
    procedure3.get_Practitioner()
    procedure3.get_Charges()
    procedure3.get_PatientID()

    print("*** Patient Bill ***" )
    print("Name:", patient.get_name())
    print("Address:", patient.get_address())
    print("Phone:", patient.get_phone())
    print()

    total = 0

    if patient.get_ID() == procedure.get_PatientID():
        print ("Procedure:", procedure.get_Procedure())
        print ("Date:", procedure.get_Date())
        print ("Practioner:", procedure.get_Practitioner())
        print ("Charge:", "${:.2f}".format(procedure.get_Charges()))
        print()
        total += procedure.get_Charges()

    if patient.get_ID() == procedure2.get_PatientID():
        print ("Procedure:", procedure2.get_Procedure())
        print ("Date:", procedure2.get_Date())
        print ("Practioner:", procedure2.get_Practitioner())
        print ("Charge:", "${:.2f}".format(procedure.get_Charges()))
        print()
        total += procedure2.get_Charges()   

    if patient.get_ID() == procedure3.get_PatientID():
        print ("Procedure:", procedure3.get_Procedure())
        print ("Date:", procedure3.get_Date())
        print ("Practioner:", procedure3.get_Practitioner())
        print ("Charge:", "${:.2f}".format(procedure.get_Charges()))
        print()
        total += procedure3.get_Charges() 

    if patient.get_veteran_status() == True:
        total = total*0.60

    else:
        total

    print("Total Charges:","${:.2f}".format(total))

main()