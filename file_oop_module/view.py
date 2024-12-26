# view.py
from tabulate import tabulate

class StudentView:
    @staticmethod
    def display_students(students):
        """Menampilkan daftar siswa dalam tabel"""
        table = [[s.name, s.grades, round(sum(s.grades) / len(s.grades), 2)] for s in students]
        print(tabulate(table, headers=["Nama", "Nilai", "Rata-rata"], tablefmt="grid"))
