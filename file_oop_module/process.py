# process.py
class StudentProcessor:
    @staticmethod
    def validate_grades(grades):
        """Validasi input nilai, harus berupa angka 0-100"""
        try:
            grades = [int(grade) for grade in grades]  # Ubah ke angka
            for grade in grades:
                if grade < 0 or grade > 100:
                    raise ValueError("Nilai harus berada dalam rentang 0-100.")
            return grades
        except ValueError:
            raise ValueError("Input nilai harus berupa angka valid.")

    @staticmethod
    def calculate_average(grades):
        """Menghitung rata-rata nilai"""
        return sum(grades) / len(grades) if grades else 0
