import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bdd_pipe"
)

cursor = conn.cursor()

def fetchstudent():
    cursor.execute("SELECT * FROM etudiants")
    etudiants_all_dict = []
    for etudiant in cursor:
        etudiants_dict = {
            "prenom": etudiant[1],
            "nom": etudiant[2],
        }
        etudiants_all_dict.append(etudiants_dict)
    return etudiants_all_dict

def fetchenseignant():
    cursor.execute("SELECT * FROM enseignants")
    enseignants_all_dict = []
    for enseignant in cursor:
        enseignant_dict = {
            "prenom": enseignant[1],
            "nom": enseignant[2],
        }
        enseignants_all_dict.append(enseignant_dict)
    return enseignants_all_dict

def displayeleves():
    cursor.execute("SELECT student_id, prenom, nom, numero_classe FROM etudiants")
    etudiants = cursor.fetchall()
    for row in etudiants:
        print("Etudiant: ", row)

def displayenseignants():
    cursor.execute("SELECT teacher_id, prenom, nom, numero_classe FROM enseignants")
    enseignants = cursor.fetchall()
    for row in enseignants:
        print("Enseignant: ", row)

def jointure_count(enseignants):
    cursor.execute("""SELECT enseignants.prenom, COUNT(*) as student_count FROM etudiants 
                      JOIN enseignants ON etudiants.numero_classe = enseignants.numero_classe 
                      GROUP BY enseignants.prenom""")
    
    jointure = cursor.fetchall()
    
    student_count_dict = {row[0]: row[1] for row in jointure}
    
    for enseignant in enseignants:
        prenom = enseignant.get("prenom")
        num_students = student_count_dict.get(prenom, 0)
        print(f"Enseignant {prenom} a {num_students} élèves.")
    
    return student_count_dict

def init():
    students = fetchstudent()
    enseignants = fetchenseignant()
    displayeleves()
    displayenseignants()
    jointure_count(enseignants)

if __name__ == "__main__":
    init()
