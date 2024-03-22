from tkinter import filedialog
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

from Calculations import Calculations


def dosya_sec():
    # Tkinter penceresini oluşturun ve gizleyin
    root = tk.Tk()
    root.withdraw()
    tk.messagebox.showinfo("Bilgi", "Programın çalışması için verileri içeren CSV dosyasını seçmelisiniz.")
    # Kullanıcıdan CSV dosyasını seçmesini isteyin
    dosya_yolu = filedialog.askopenfilename(title="CSV Dosyasını Seçin", filetypes=[("CSV Files", "*.csv")])

    if dosya_yolu:
        return dosya_yolu
    else:
        # Dosya seçilmediği için hata mesajı gösterin
        messagebox.showerror("Hata", "CSV dosyası seçilmedi.")
        exit(-1)


if __name__ == '__main__':
    # Merkezi Eğilim ve Merkezi Dağılım hesaplamalarını yapan kendi yazdığım sınıf/mini kütüphane.
    calculate = Calculations()
    register = [[], [], []]
    mod_list = []

    # Tkinter penceresini oluşturun
    root = tk.Tk()
    root.withdraw()  # Tkinter penceresini gizleyin

    file_path = dosya_sec()

    # file_path = r"C:\Users\alica\OneDrive\Masaüstü\study_performance.csv"
    data = pd.read_csv(file_path)

    # Datalarımızı data frameden çekiyoruz
    math_score = data["math_score"]
    reading_score = data["reading_score"]
    writing_score = data["writing_score"]
    #  Topluca çizdirmek için bir dizide topladım.
    datas = [math_score, reading_score, writing_score]

    # İlk önce verimizi boxplot olarak çizdiriyoruz.
    plt.boxplot(datas, whis=1.75)
    plt.show()

    for i, data in enumerate(datas):
        # Kendi yazdığım outliers değerleri çıkarıp temiz verileri dönen fonksiyon
        np_arr = np.array(data)
        calculate.merge_sort(np_arr)
        np_clear_data = calculate.remove_outliers(np_arr)
        # Daha sonra matematik işlemleri için yazdığım sınıftaki ilgili fonksiyonu çağırarak hesaplama yapıyoruz.
        art_ort = calculate.aritmetik_ort(np_clear_data)
        medyan = calculate.find_medyan(np_clear_data)
        mods = calculate.find_mods(np_clear_data)
        arr_range = calculate.range(np_clear_data)
        mutlak_sapma = calculate.mutlak_sapma(np_clear_data, art_ort)
        varyans = calculate.varyans(np_clear_data, art_ort)
        standart_sapma = calculate.standart_sapma(np_clear_data, art_ort)
        degisim_katsayisi = calculate.degisim_katsayisi(np_clear_data, art_ort)
        Q1, Q3 = calculate.find_Q1_Q3(np_arr)
        IQR = Q3 - Q1

        register[i].append(art_ort)
        register[i].append(medyan)
        mod_list.append(mods)
        register[i].append(arr_range)
        register[i].append(mutlak_sapma)
        register[i].append(varyans)
        register[i].append(standart_sapma)
        register[i].append(degisim_katsayisi)
        register[i].append(IQR)

        print(f"{data.name} aritmetik ort : {art_ort}")
        print(f"{data.name} medyan: {medyan}")
        print(f"{data.name} mods: {mods}")
        print(f"{data.name} range: {arr_range}")
        print(f"{data.name} mutlak sapma: {mutlak_sapma}")
        print(f"{data.name} varyans: {varyans}")
        print(f"{data.name} standart sapma: {standart_sapma}")
        print(f"{data.name} değişim katsayısı: {degisim_katsayisi}")
        print(f"{data.name} IQR : {IQR}")
        print("----------------------------------------------------------------")

    df = pd.DataFrame(np.array(register), columns=["Art Ort", "Medyan", "Range", "Mutlak Sapma",
                                                   "Varyans", "Standart Sapma", "Değişim Katsayısı", "IQR"])
    df["Mods"] = mod_list
    df.to_excel("sonuc.xlsx")

    print("Verileriniz başarıyla sonuc.xlsx dosyasına kaydedilmiştir.")
    input("Çıkmak için herhangi bir tuşa basın")
