thien_can = ["Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky"]
dia_chi = ["Than", "Dau", "Tuat", "Hoi", "Ty", "Suu", "Dan", "Mao", "Thin", "Ty", "Ngo", "Mui"]

current_year = input("Enter the current year: ")
last_digit = int(current_year[-1])
thien_can_name = thien_can[0]
dia_chi_name = dia_chi[int(current_year)%12]

print(f"{thien_can_name} {dia_chi_name}")