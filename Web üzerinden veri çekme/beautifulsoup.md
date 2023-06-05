
# Beautiful Soup ile Web Üzerinden Veri Çekme

Web üzerinden veri çekme, Python'da yaygın olarak kullanılan bir işlemdir ve bunu yapmak için `beautifulsoup` kütüphanesi oldukça popülerdir. Bu kütüphane, HTML ve XML belgelerini analiz etmek ve bu belgelerden veri çekmek için kullanılır.
## Örnek 1: Verileri Ekrana Yazdırma

Bu Python kodu, "[https://www.btkakademi.gov.tr/portal/catalog?sf=popular](https://www.btkakademi.gov.tr/portal/catalog?sf=popular)" adresinden verileri çeker ve kurs isimlerini ekrana yazdırır.
## Örnek 2: Verileri Dosyaya Kaydetme

Bu Python kodu, "[https://www.btkakademi.gov.tr/portal/catalog?categoryId=353](https://www.btkakademi.gov.tr/portal/catalog?categoryId=353)" adresinden verileri çeker ve kurs isimlerini "btk_kurslar.txt" adlı bir dosyaya kaydeder.
Bu örnekte, yine web sayfasını alır ve içeriği BeautifulSoup ile işleriz. Ardından kurs isimlerini seçip "btk_kurslar.txt" adlı bir dosyaya kaydederiz. Bunun için `open` fonksiyonunu kullanır ve kurs isimlerini dosyaya yazdırırız.

Bu iki örnek, BeautifulSoup kütüphanesini kullanarak web sayfalarından veri çekme işlemini basit bir şekilde göstermektedir.
