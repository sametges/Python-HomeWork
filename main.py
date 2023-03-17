students = ["Samet","Mustafa","Ahmet"]

def student1():
    student2 = input("Öğrenci Adı Giriniz:")
    students.append(student2)
    print(students)
student1()

while(True):
    kaldırılacak = input("Kaldırılacak olan İsmi Giriniz:")
    students.remove((kaldırılacak))
    print(students)
    break

def birdenfazla():
    list= []
    birdenfazla1 = input("İsim ekleme:")
    list.append(birdenfazla1)
    students.extend(list)
    print(students)
birdenfazla()

for student in students:
    print(student)
