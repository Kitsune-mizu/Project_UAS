# main.py
from data import Student
from process import StudentProcessor
from view import StudentView

def main():
    students = []  # Daftar siswa
    while True:
        try:
            # Input data siswa
            name = input("Masukkan nama mahasiswa: ").strip()
            grades_input = input("Masukkan nilai (pisahkan dengan koma): ").split(',')
            grades = StudentProcessor.validate_grades(grades_input)

            # Tambah siswa ke daftar
            students.append(Student(name, grades))

            # Tampilkan data
            StudentView.display_students(students)

            # Apakah ingin menambah siswa lagi?
            if input("Tambah siswa lagi? (y/n): ").lower() != 'y':
                break
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
