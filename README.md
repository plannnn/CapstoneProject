# CapstoneProject
Capstone Project Studi Independen
Team ID: CSD-080
M004T5007 - Kivlan Khair Wijayanto
M298R4297 - Sang Putu Yoga Pramana

# Crop-Recommendation
Dataset didapatkan dari Kaggle : https://www.kaggle.com/atharvaingle/crop-recommendation-dataset

## Variabel Detail:
Dataset terdiri dari 8 variabel dimana 7 variabel dipertimbangkan untuk memprediksi variabel output. Rincian Variabel diberikan di bawah ini
1. N (Nitrogen): Kandungan Nitrogen dalam tanah. Nitrogen sangat penting untuk pertumbuhan (struktur), pengolahan makanan tanaman (metabolisme), dan pembentukan klorofil. Tanpa nitrogen yang cukup dalam tanaman, tanaman tidak dapat tumbuh lebih tinggi, atau menghasilkan cukup makanan (biasanya berwarna kuning).
2. P (Fosfor): Kandungan Fosfor dalam tanah. Peran utama fosfor dalam tanaman adalah untuk menyimpan dan mentransfer energi yang dihasilkan oleh fotosintesis untuk digunakan dalam proses pertumbuhan dan reproduksi. Siklus P tanah dalam berbagai bentuk di dalam tanah
3. K (Kalium): Kandungan Kalium dalam tanah. Kalium merupakan nutrisi penting untuk pertumbuhan tanaman.
4. Suhu: Suhu dalam derajat sensus. Suhu tinggi mempengaruhi pertumbuhan tanaman dalam banyak cara. Yang paling jelas adalah efek panas pada fotosintesis, di mana tanaman menggunakan karbon dioksida untuk menghasilkan oksigen, dan respirasi, proses yang berlawanan di mana tanaman menggunakan oksigen untuk menghasilkan karbon dioksida.
5. Humidity (Kelembaban) : Kelembaban relatif dalam %. Ketika kondisi terlalu lembab, hal itu dapat mendorong pertumbuhan jamur dan bakteri yang menyebabkan tanaman mati dan gagal panen, serta kondisi seperti akar atau mahkota busuk. Kondisi lembab juga mengundang kehadiran hama, seperti agas jamur, yang larvanya memakan akar tanaman dan tumbuh subur di tanah yang lembab.
6. PH : nilai ph tanah. Nutrisi tanaman larut dari tanah jauh lebih cepat pada nilai pH di bawah 5,5 daripada dari tanah dalam kisaran 5,5 hingga 7,0. Di beberapa tanah mineral aluminium dapat larut pada tingkat pH di bawah 5,0 menjadi racun bagi pertumbuhan tanaman. PH tanah juga dapat mempengaruhi ketersediaan unsur hara tanaman.
7. Rain fall (Curah Hujan) : Curah hujan dalam mm. Tanaman menggunakan kelembaban di tanah untuk mengisi kembali air yang hilang melalui transpirasi. Jika tidak ada air di tanah, daun akan layu. Karena semakin banyak air yang hilang, tanaman akan gagal dan akhirnya mati. Air hujan membangun tingkat kelembaban di tanah dan memastikan tanaman yang sehat.
Akhirnya,
8. Label : Ini adalah variabel keluaran yang berisi 22 nilai unik yaitu, 22 tanaman berbeda dan mereka adalah ['Apple','Banana','blackgram','chickpea','coconut','coffee','cotton' ,'grapes','jute','kidney beans','lentils','maize','mango','moth beans','mung bean','muskmelon','orange','papaya','pigeonpeas ','pomegranate','Rice','Watermelon']
Analisis data eksplorasi dilakukan untuk mengambil insight dari data tersebut.

## Algoritma :
Berikut merupakan Model Algoritma yang digunakan, beserta akurasi dari model tersebut 
  1. K Nearest Neighbours <br>
    Akurasi model: 97%
  2. Decision Tree <br>
    Akurasi Model: 98% 
  3. Support Vector Machine<br>
    Akurasi Model: 93%
  4. Linear Regression<br>
    Akurasi Model: 95%
  5. Random Forest<br>
    Akurasi Model: 100% 
  6. XGBoost<br>
    Akurasi Model: 99%<br><br>
Berdasarkan Akurasi Model yang didapat, model yang digunakan adalah Random Forest
## Deployment :
Aplikasi ini menggunakan platform Heroku untuk Deployment. URL Aplikasi (Sementara): https://cropred.herokuapp.com/
## Bentuk Website:<br>
Sejauh ini Bentuk Web sebagai berikut, (dapat dirubah kedepannya)
![image](https://user-images.githubusercontent.com/80215981/146590714-eaa081aa-4798-4d69-a67d-cbd10875e6b5.png)
![image](https://user-images.githubusercontent.com/80215981/146590763-648c08b5-6f09-4c12-a569-622e37ed3347.png)
![image](https://user-images.githubusercontent.com/80215981/146590860-09c4315d-7220-408d-96ee-63e0e4e66c6e.png)
## Demo :
### Demo Website :<br>
![Demo Website](https://media.giphy.com/media/xAcdKwMQuFFqkMNEFP/giphy.gif)
### Demo Mobile :<br>
![Demo Mobile](https://media.giphy.com/media/9zbShOXfzC5Ex0mZ3Z/giphy.gif)
