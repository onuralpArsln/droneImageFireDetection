import cv2
import os

# Video dosyasını aç
video_path = '..\\vidResourcesLong\\KOZANSON.mp4'  # Videonuzun yolu
cap = cv2.VideoCapture(video_path)

# Video bilgilerini alın
fps = cap.get(cv2.CAP_PROP_FPS)  # Video FPS (saniyede kare sayısı)
frame_rate = int(fps)  # Her saniyede bir kare alacağız

# Çıkartılan resimlerin kaydedileceği dizini oluşturun
output_dir = 'output_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_count = 0
frame_num = 0

# Video karelerini al ve kaydet
while True:
    ret, frame = cap.read()
    if not ret:
        break  # Video bittiğinde döngüyü sonlandır

    # Eğer bu kare, her saniyede bir kareyi temsil ediyorsa
    if frame_count % frame_rate == 0:
        frame_filename = os.path.join(output_dir, f"frame_{frame_num}.jpg")
        cv2.imwrite(frame_filename, frame)  # Kareyi kaydet
        frame_num += 1

    frame_count += 1
# Video dosyasını kapat
cap.release()
print(f"Toplam {frame_num} kare çıkarıldı ve kaydedildi.")