# cpuBitCrack

Bitcoin özel anahtarını bulmak için Python ile yazılmış bir araç. Verilen aralığı yüzdelerine ayırır ve yüzdelerine ayrılanları da yüzdelerine ayırır. Yani 1. aşamada verilen aralığı yüzdelerine ayırır, 2. aşamada 1. aşamanın aralıklarını yüzdelere ayırır. Ayrıca tüm yüzdelerine ayrılmış sayıların arasında rastgele sayı arar. Eşleşme olursa BULUNDU.txt dosyasına yazdırır.

Acemice hazırladığım bir python aracıdır. Büyük aralıklar için umut yok, eğer Dünya'nın en şanslı kişisi iseniz deneyin :)

`-a` -- Aranacak adres, ADDRESS

`-s` -- Aralığın Başlangıcı, START

`-e` -- Aralığın Bitişi, END

`-str` -- Adım, STRIDE

#Puzzle 64
`python3 cpuBitCrack.py -a 16jY7qLJnxb7CHZyqBP8qca9d51gAjyXQN -s 9223372036854775807 -e 18446744073709551615 -str 1354254`

Desteklemek İstersen : `bc1q2sf6uq7k75dexddm9k9kw6ega7k75up57juf76`
