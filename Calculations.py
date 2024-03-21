import numpy as np
import math


class Calculations:
    """
    Bu sınıf, çeşitli istatistik hesaplamaları gerçekleştirmek için kullanılır.
    """

    def aritmetik_ort(self, arr):
        """
        Gelen dizi için aritmetik ortalama hesaplar.

        Parameters:
        arr (list): Hesaplanacak sayıların listesi.

        Returns:
        float: Aritmetik ortalama değeri.
        """
        # İlgili dizideki tüm toplamları tutmak için.
        total = 0
        for num in arr:
            total += num
        # Hesaplamayı yapar ve return eder.
        return total / len(arr)

    def find_medyan(self, sorted_arr):
        """
        Sıralanmış bir dizi alır ve onun medyanını bulur.

        Parameters:
        sorted_arr (list): Sıralanmış sayıların listesi.

        Returns:
        float: Medyan değeri.
        """
        len_arr = len(sorted_arr)
        # Array uzuluğunun çift sayı olup olmamasına göre medyan formülü değişecektir. Bu yüzden onun kontrolünü yapar.
        if len_arr % 2 == 0:
            # Ortadaki elemanlardan birisini bulur. İndex değeri 0'dan başladığı için 1 çıkarır.
            index_1 = (len_arr // 2) - 1
            # Diğer eleman ise oonun hemen sağında olacağından yeni bir matematik işlemi yaptırmaya gerek kalmaz.
            index_2 = index_1 + 1
            return (sorted_arr[index_1] + sorted_arr[index_2]) / 2
        else:
            index_1 = ((len_arr + 1) // 2) - 1
            return sorted_arr[index_1]

    def find_medyan_index(self, arr):
        """
        Yardımcı fonksiyondur. Medyanın indexi bazı durumlarda gerektiği için özel olarak sadec medyan indexini bulan bir fonksiyon.

        Parameters:
        arr (list): İşlenecek dizi.

        Returns:
        int: Medyan index değeri.
        """
        len_arr = len(arr)
        if len_arr % 2 == 0:
            index_1 = (len_arr // 2) - 1
            return index_1
        else:
            index_1 = ((len_arr + 1) // 2) - 1
            return index_1

    def find_mods(self, sorted_arr):
        """
        İlgili dizinin modlarını veya modunu döndürür.

        Parameters:
        sorted_arr (list): Sıralanmış sayıların listesi.

        Returns:
        list: Modlar listesi.
        """
        # Döndürülecek olan mod dizisini tutar.
        mods = []
        # İlgili mod dizisi ile bağlantılıdır. Aynı sıra ile tekrar mod değerlerinin tekrar sayılarını tutar.
        repeats = []
        repeat_count = 0
        number = -1
        for num in sorted_arr:
            # Repeat count 0 ise daha önceden ilgili sayı kontrol edilmemiş demektir.
            if repeat_count == 0:
                number = num
                repeat_count += 1
            # Sorted_arr den alınan yenş sayı önceden depolanmış sayı ile eşitse bu onun tekrar ettiğini gösterir.
            elif num == number:
                repeat_count += 1
            # Ne ilk defa gelen bir sayı varsa elimizde ne de bu sayı depolanan sayı ile eşitse o zaman onu mod dizisine
            # atmamız gerekip gerekmediğini karar vermeliyiz.
            elif repeat_count > 1:
                # Eğer mods dizimiz boş ise veya mod dizisi içindeki herhangi bir eleman ile tekrar sayısı aynı ise
                # o zaman onu direk mod dizisine atarız.
                if len(mods) == 0 or repeats[0] == repeat_count:
                    mods.append(number)
                    repeats.append(repeat_count)
                # Mod dizisi boş değil ise tekrar sayısını kontrol ederiz ve ona göre mod dizisine atarız.
                elif repeats[0] < repeat_count:
                    # Yeni gelen sayının tekrar sayısı mod dizisi içindeki değerden büyük ise o zaman mod dizsis
                    # içindeki değerlerin gerçekten birer mod olamyacağını anlarız ve mod dizisini boşaltırız.
                    mods.clear()
                    repeats.clear()
                    mods.append(number)
                    repeats.append(repeat_count)
                # En son ise yeni sayımızı alır ve döngüye devam ederiz.
                number = num
                repeat_count = 1
            # Yukarıdaki seçeneklerin hiçbirisi uymuyor ise bu sayı mod olamaz çünkü 1'den fazla tekrar etmiyor.
            # O zaman yeni atamalrı yap ve devam et.
            else:
                number = num
                repeat_count = 1
        # En son mod dizimizi döneriz. Eğer kontrol ettimiz array içindeki değerlerin hepsi sadece birer kez tekrar
        # ediyor ise o zaman bu dizi boş dönecektir.
        return mods

    def range(self, arr):
        """
        Değişim aralığını hesaplar.

        Parameters:
        arr (list): Hesaplanacak sayıların listesi.

        Returns:
        float: Değişim aralığı.
        """
        return arr[len(arr) - 1] - arr[0]

    def mutlak_sapma(self, arr, art_ort):
        """
        Ortalama Mutlak sapmayı hesaplar. Kısaca ortalama sapma, verilerin aritmetik ortalamdan ne kadar
        saptığının ortlama değerini hesaplar.

        Parameters:
        arr (list): Hesaplanacak sayıların listesi.
        art_ort (float): Aritmetik ortalama değeri.

        Returns:
        float: Ortalama mutlak sapma değeri.
        """
        # Tüm sapmalarının toplamını tutar.
        total = 0
        for num in arr:
            total += abs(num - art_ort)

        return total / len(arr)

    # ilgili dizinin varyansını hesaplar.
    def varyans(self, arr, art_ort):
        """
        İlgili dizinin varyansını hesaplar.

        Parameters:
        arr (list): Hesaplanacak sayıların listesi.
        art_ort (float): Aritmetik ortalama değeri.

        Returns:
        float: Varyans değeri.
        """
        # Tüm sapmalarının karesinin toplamanı tutar.
        total = 0
        for num in arr:
            total += abs(num - art_ort) ** 2

        return total / (len(arr) - 1)

    def standart_sapma(self, arr, art_ort):
        """
        Standart sapmayı hesaplar.

        Parameters:
        arr (list): Hesaplanacak sayıların listesi.
        art_ort (float): Aritmetik ortalama değeri.

        Returns:
        float: Standart sapma değeri.
        """
        varyans = self.varyans(arr, art_ort)
        return math.sqrt(varyans)

    def degisim_katsayisi(self, arr, art_ort):
        """
        Verilerin değişim katsayısını hesaplar.

        Parameters:
        arr (list): Hesaplanacak sayıların listesi.
        art_ort (float): Aritmetik ortalama değeri.

        Returns:
        float: Değişim katsayısı.
        """
        std = self.standart_sapma(arr, art_ort)
        return std / art_ort

    def find_Q1_Q3(self, sorted_arr):
        """
        Bu fonksiyon alt ve üst çeyreklik değerlerini hesaplar. Bu outliersı bulmak ve çeyrekler aralığını bulmak için
        işimize yarayacaktır.

        Parameters:
        sorted_arr (list): İşlenecek dizi.

        Returns:
        tuple: Alt ve üst çeyreklik değerleri.
        """
        # self.merge_sort(arr)
        medyan_index = int(self.find_medyan_index(sorted_arr))
        if len(sorted_arr) % 2 == 0:
            L = np.copy(sorted_arr[:medyan_index])
            R = np.copy(sorted_arr[medyan_index:])
        else:
            L = np.copy(sorted_arr[:medyan_index])
            R = np.copy(sorted_arr[medyan_index + 1:])

        L_medyan = self.find_medyan(L)
        R_medyan = self.find_medyan(R)

        return L_medyan, R_medyan

    def remove_outliers(self, arr, multiplier=1.75):
        """
        Outliers değerleri ilgili diziden çıkarır ve bir numpy array olarak temiz diziyi döner.

        Parameters:
        arr (list): İşlenecek dizi.
        multiplier (float): Aykırı değerleri belirlemede kullanılacak çarpan. Varsayılan değer 1.75.

        Returns:
        numpy.ndarray: Aykırı olmayan değerlerin numpy dizisi.
        """
        Q1, Q3 = self.find_Q1_Q3(arr)
        IQR = Q3 - Q1
        lower_bound = Q1 - IQR * multiplier
        upper_bound = Q3 + IQR * multiplier
        self.print_outliers(arr, lower_bound, upper_bound)
        clear_arr = arr[(arr >= lower_bound) & (arr <= upper_bound)]
        return np.array(clear_arr)

    # Yardımcı fonskiyon
    def print_outliers(self, arr, lower_bound, upper_bound):
        outliers = arr[(arr < lower_bound) | (upper_bound < arr)]
        print(f"Çıkarılan aykırı değerler {outliers}")

    # Kendi yazdığım merge sort algortiması.
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2

            L = np.copy(arr[:mid])
            R = np.copy(arr[mid:])
            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0
            while len(L) > i and len(R) > j:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while len(L) > i:
                arr[k] = L[i]
                i += 1
                k += 1

            while len(R) > j:
                arr[k] = R[j]
                j += 1
                k += 1
