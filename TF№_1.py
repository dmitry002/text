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

# Коментар Юлії - реалізовано частину В
def print_words():
    print("Слова:")
    file_3_r = Open(file2_name, "r")
    if file_3_r != None:
        for line in file_3_r.read().split():
            print(line)
        file_3_r.close()
        print("Файл TF1_2.txt закрито!")


# Додаткова функція
def show_info():
    file_1_r = Open(file1_name, "r")
    if file_1_r != None:
        lines = file_1_r.readlines()
        file_1_r.close()
        print("Кількість рядків у TF1_1.txt:", len(lines))
    file_2_r = Open(file2_name, "r")
    if file_2_r != None:
        words = file_2_r.read().split()
        file_2_r.close()
        print("Кількість слів у TF1_2.txt:", len(words))
        longest = ""
        for word in words:
            if len(word) > len(longest):
                longest = word
        print("Найдовше слово:", longest)


create_file()
write_words()
print_words()
show_info()
