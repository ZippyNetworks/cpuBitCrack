# cpuBitCrack

Bitcoin özel anahtarını bulmak için Python ile yazılmış bir araç. Verilen aralığı yüzdelerine ayırır ve yüzdelerine ayrılanları da yüzdelerine ayırır.

Özetle;

1. aşamada verilen aralığı yüzdelerine ayırır,
2. aşamada 1. aşamanın tüm aralıklarını yüzdelere ayırır,
3. aşamada 2. aşamanın tüm aralıkları arasında rastgele sayı arar.

Herhangi bir aşamada eşleşme olursa BULUNDU.txt dosyasına yazdırır. Büyük aralıklar için umut yok, eğer Dünya'nın en şanslı kişisi iseniz deneyin :)

`-a` -- Aranacak adres, ADDRESS

`-s` -- Aralığın Başlangıcı, START

`-e` -- Aralığın Bitişi, END

`-str` -- Adım, STRIDE

#Puzzle 64
`python3 cpuBitCrack.py -a 16jY7qLJ -s 9223372036854775807 -e 18446744073709551615 -str 1`

Desteklemek İstersen : `bc1q2sf6uq7k75dexddm9k9kw6ega7k75up57juf76`
