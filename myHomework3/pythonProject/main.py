import time


def countDown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")  # Aynı satırda güncelle
        time.sleep(1)  # 1 saniye bekle
        t -= 1  # Zamanı 1 azalt

    # Ekranı temizle ve bitiş mesajını göster
    print('00:00', end="\r")
    print('Fire in the hole!!')


# Input time in seconds
t = int(input("Enter the time in seconds: "))

# Function call
countDown(t)
