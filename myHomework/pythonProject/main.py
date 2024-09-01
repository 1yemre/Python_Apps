from PIL import Image, ImageDraw  # Pillow kütüphanesinden Image ve ImageDraw sınıflarını içe aktarıyoruz

images = []  # GIF için kullanılacak tüm görüntüleri saklayacak boş bir liste oluşturuyoruz

width = 200  # Her bir görüntünün genişliğini ve yüksekliğini 200 piksel olarak ayarlıyoruz
center = width // 2  # Görüntünün merkez noktasını hesaplıyoruz, tam sayı olarak (100 piksel)

Color1 = (41, 95, 152)  # Elipsin rengi (RGB formatında mavi bir renk)
Color2 = (205, 194, 165)  # Arka plan rengi (RGB formatında bej bir renk)

max_radius = int(center * 1.5)  # Elipsin maksimum yarıçapını belirliyoruz (150 piksel)
step = 8  # Elipsin büyüme adımlarını belirliyoruz (her adımda 8 piksel artış olacak)

for i in range(0, max_radius, step):  # 0'dan max_radius'a kadar, step değerine göre döngü oluşturuyoruz
    im = Image.new('RGB', (width, width), Color2)  # Arka planı Color2 rengine sahip yeni bir görüntü oluşturuyoruz
    draw = ImageDraw.Draw(im)  # Çizim yapmamızı sağlayacak bir Draw nesnesi oluşturuyoruz
    draw.ellipse((center - i, center - i,  # Elipsin üst sol ve alt sağ köşelerinin koordinatlarını belirliyoruz
                  center + i, center + i),
                 fill=Color1)  # Elipsi Color1 rengiyle dolduruyoruz
    images.append(im)  # Oluşturduğumuz görüntüyü images listesine ekliyoruz

# GIF'i kaydetme
images[0].save('deneme.gif',  # İlk görüntüyü 'deneme.gif' adıyla kaydediyoruz
               save_all=True,  # Tüm görüntülerin kaydedilmesini sağlıyoruz
               append_images=images[1:],  # İlk görüntü dışındaki tüm görüntüleri ekliyoruz
               optimize=False,  # Optimizasyon yapmıyoruz (kaliteyi korumak için)
               duration=100,  # Her bir karenin 100 milisaniye gösterilmesini sağlıyoruz
               loop=0)  # GIF'in sonsuz döngüde tekrar etmesini sağlıyoruz
