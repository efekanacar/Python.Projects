
# Windows Kayıt Defteri - Başlangıç Programları Listeleme

Bu Markdown belgesi, Python'da `winreg` kütüphanesini kullanarak Windows kayıt defterindeki "Run" anahtarına erişerek kayıtlı başlangıç programlarını listeleyen bir kodu açıklamaktadır.

Bu örnek, Windows kayıt defterinin "Run" anahtarına erişmek için `winreg` kütüphanesini kullanır. İlk olarak, `OpenKey` fonksiyonunu kullanarak anahtarın açılır ve içindeki alt anahtarları numaralandırırız. Daha sonra, her alt anahtar için `OpenKey` fonksiyonunu tekrar kullanarak kayıtlı değerleri numaralandırırız.

Her alt anahtar için, `EnumValue` fonksiyonunu kullanarak kayıtlı değerleri alır ve ekrana yazdırırız. Bu değerler, başlangıç programlarının adı, verisi ve türüdür.

Bu kod, kayıtlı başlangıç programlarını listeleyerek Windows kayıt defteri üzerinde yapılan bir işlemi basit bir şekilde göstermektedir.

