
//  Created by Erdem Hasbek on 27.01.2026.




import UIKit // iOS'un içinde bulunan tüm görselleri (butonlar, etiketler vb.) import ediyoruz.

class AnaSayfaViewController: UIViewController { // Ekranı bir class olarak oluşturuyoruz.
    
    // ekranda kullanacağımız şeyleri class içinde en baştan tanımlıyoruz.
    
    // label = sabit düz yazı
    // button = kullanıcı uygulama iletişiöi
    // Image = ikonlar fotolar görseller vs vs
    
    
    // TANIMLAMALARI YAPIYORUZ
    
    let baslikLabel = UILabel() // Ekrana bir başlık yazısı eklemek için bir etiket oluşturur.
    let mesajLabel = UILabel() // Alt kısma daha küçük bir açıklama yazısı için etiket oluşturur.
    let buton = UIButton() // Kullanıcının tıklayabileceği bir düğme oluşturur.
    let sayacLabel = UILabel() // Tıklama sayısını gösterecek özel bir yazı alanı oluşturur.
    let imageView = UIImageView() // Ekranın ortasına bir resim/ikon koymak için kutu oluşturur.
    var sayac = 0 // Tıklama sayısını aklında tutacak olan basit bir matematiksel değişken.
    
    override func viewDidLoad() { // Ekran telefonun hafızasına yüklendiği an çalışan "başlangıç" fonksiyonu.
        super.viewDidLoad() // Apple'ın kendi temel hazırlıklarını yapmasına izin verir.
        
        // Arka plan: Ekranın zemin rengini belirler.
        view.backgroundColor = .systemBackground // Telefonun moduna göre ayarlamak en mantıklısı
        
        // Başlık Ayarları
        baslikLabel.text = "İlk IOS Uygulamam" // Yazılacak metni belirler.
        baslikLabel.font = .systemFont(ofSize: 32, weight: .bold) // BAŞLIK BOYUTUNU BELİRLİYORUZ. VE KALIN OLMASI
        baslikLabel.textAlignment = .center // Yazıyı bulunduğu kutunun tam ortasına hizalar.
        baslikLabel.textColor = .label // KOYU MOD AÇIK MOD
        
        // Mesaj Ayarları
        mesajLabel.text = "Tamamen Programmatic UI ile yapıldı!\nStoryboard kullanılmadı." // Alt mesaj metni.
        mesajLabel.font = .systemFont(ofSize: 16) // Yazı boyutunu 16 yapar.
        mesajLabel.textAlignment = .center // Yazıyı ortalar.
        mesajLabel.numberOfLines = 0 // 0 "sınırsız satır" demektir, metin sığmazsa alt satıra geçer.
        mesajLabel.textColor = .secondaryLabel // Yazı rengini biraz daha gri, ikincil bir tona getirir.
        
        // İkon (Resim) Ayarları
        imageView.image = UIImage(systemName: "star.fill") // Apple'ın hazır "yıldız" ikonunu içine koyar.
        imageView.tintColor = .systemYellow // Yıldızın rengini sarı yapar.
        imageView.contentMode = .scaleAspectFit // Resim kutunun içine sığarken şeklinin bozulmamasını sağlar.
        
        // Buton Ayarları
        buton.setTitle("Tıkla!", for: .normal) // Butonun üzerindeki yazıyı belirler.
        buton.backgroundColor = .systemBlue // Butonun arka planını mavi yapar.
        buton.setTitleColor(.white, for: .normal) // Buton yazısının rengini beyaz yapar.
        buton.titleLabel?.font = .systemFont(ofSize: 18, weight: .semibold) // Buton yazısını biraz kalınlaştırır.
        buton.layer.cornerRadius = 12 // Butonun köşelerini yumuşatır, yuvarlaklaştırır. arttırdıkça ovalleşir
        buton.addTarget(self, action: #selector(butonaTiklandi), for: .touchUpInside) // "Bana basılınca şu fonksiyonu çalıştır" der.
        
        // Sayaç Yazısı Ayarları
        sayacLabel.text = "Tıklama: 0" // Başlangıçta görünecek metin.
        sayacLabel.font = .systemFont(ofSize: 24, weight: .medium) // Yazı boyutu ve orta kalınlık.
        sayacLabel.textAlignment = .center // Ortaya hizalar.
        sayacLabel.textColor = .systemGreen // Sayıların rengini yeşil yapar.
        
        // View'e ekleme: Oluşturduğumuz parçaları tek tek sahneye davet ediyoruz.
        [baslikLabel, mesajLabel, imageView, buton, sayacLabel].forEach { // Hepsini bir listeye alıp döngüye sokar.
            view.addSubview($0) // Her bir parçayı sırayla ana ekrana yapıştırır.
            $0.translatesAutoresizingMaskIntoConstraints = false // "Kendi başına hareket etme, benim vereceğim kurallara (constraints) uy" der.
        }
        
        // Layout: Parçaların ekranda tam olarak nerede duracak (matematiksel)
        
        // YAKLAŞIK 400 BİRİM GENİŞLİK 800 BİRİM YÜKSEKLİK VARIDR (17 PRO MAX)
        // BUNA GÖRE HAREKET EDİLMELİ
        
        
        NSLayoutConstraint.activate([ // Bu blok içindeki tüm kuralları "aktif" hale getirir.
            // Başlık Konumu
            baslikLabel.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 40), // Üstten (çentikten sonra) 40 birim boşluk bırak.
            
            // GÜVENLİ BÖLGENİN EN TEPESİNİ REFERANS ALARAK BAŞLADIK
            
            
            baslikLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20), // Soldan 20 birim içeri gir.
            baslikLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20), // Sağdan 20 birim içeride dur.
            
            // İkon Konumu
            
            //
            imageView.topAnchor.constraint(equalTo: baslikLabel.bottomAnchor, constant: 30), // Başlığın 30 birim altına yerleş.
            // İKONU BAŞLIĞA GÖRE YERLEŞTİRİYORUZ
            
            
            imageView.centerXAnchor.constraint(equalTo: view.centerXAnchor), // Ekranı tam ortala.
            imageView.widthAnchor.constraint(equalToConstant: 80), // Genişliğini 80 piksel yap.
            imageView.heightAnchor.constraint(equalToConstant: 80), // Yüksekliğini 80 piksel yap.
            
            // Mesaj Konumu
            mesajLabel.topAnchor.constraint(equalTo: imageView.bottomAnchor, constant: 30), // İkonun 30 birim altına yerleş.
            mesajLabel.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 30), // Soldan 30 birim boşluk.
            mesajLabel.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -30), // Sağdan 30 birim boşluk.
            
            // Buton Konumu
            buton.centerXAnchor.constraint(equalTo: view.centerXAnchor), // Butonu yatayda ortala.
            buton.centerYAnchor.constraint(equalTo: view.centerYAnchor, constant: 50), // Dikeyde tam ortanın 50 birim aşağısına koy.
            buton.widthAnchor.constraint(equalToConstant: 200), // Genişlik 200 olsun.
            buton.heightAnchor.constraint(equalToConstant: 55), // Yükseklik 55 olsun.
            
            // Sayaç Konumu
            sayacLabel.topAnchor.constraint(equalTo: buton.bottomAnchor, constant: 40), // Butonun 40 birim altına yerleş.
            sayacLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor) // Yatayda tam ortada dur.
        ])
    }
    
    // Butona basıldığında ne olacak?
    @objc func butonaTiklandi() { // Objective-C dünyasından gelen buton tıklama sinyalini yakalar.
        sayac += 1 // Sayacı her tıkta 1 artırır.
        sayacLabel.text = "Tıklama: \(sayac)" // Yazıyı güncel sayıya göre değiştirir.
        
        // Animasyonlar: tıklama hissi
        UIView.animate(withDuration: 0.1, animations: { // 0.1 saniyede şu işlemi yap:
            self.buton.transform = CGAffineTransform(scaleX: 0.9, y: 0.9) // Butonu %10 küçült (basılma hissi).
        }) { _ in // Küçülme bitince:
            UIView.animate(withDuration: 0.1) { // Tekrar 0.1 saniyede:
                self.buton.transform = .identity // Butonu eski boyutuna geri getir.
            }
        }
        

        
        // Renk değiştir: Butonun her tıkta farklı bir renge bürünmesini sağlar.
        let renkler: [UIColor] = [.systemBlue, .systemGreen, .systemOrange, .systemPurple, .systemRed] // Renk listesi.
        buton.backgroundColor = renkler.randomElement() // Listeden rastgele bir renk seç ve uygula.
    }
}
