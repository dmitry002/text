file1_name = "TF1_1.txt"
file2_name = "TF1_2.txt"


# Відкриття файлу з обробленням помилок
def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        print("Файл", file_name, "відкрито!")
        return file


#  Створення файлу TF1_1 із рядків різної довжини 
def create_file():
    file_1_w = Open(file1_name, "w")
    if file_1_w != None:
        file_1_w.write("Привіт, світ!\n")
        file_1_w.write("Python - проста і зручна мова програмування.\n")
        file_1_w.write("Відкрий файл; прочитай його, запиши: і закрий.\n")
        file_1_w.write("Справді?\n")
        file_1_w.write("Сьогодні ми вчимося працювати з текстовими файлами, рядками, словами і розділовими знаками...\n")
        print("Інформацію успішно записано у файл TF1_1.txt!")
        file_1_w.close()
        print("Файл TF1_1.txt закрито!")


#  Читання TF1_1 і запис кожного слова в окремий рядок TF1_2 
def write_words():
    pass


# Читання TF1_2 і друк по рядках 
def print_words():
    pass


# Додаткова функція
def show_info():
    pass


create_file()
write_words()
print_words()
show_info()