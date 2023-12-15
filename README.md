# BG Portfolio Projesi

## Proje Hakkında

BG Portfolio, Python ve Django kullanılarak geliştirilmiş bir portföy websitesi projesidir. Projede TemplateView, fonksiyon view, url'de id'ye göre proje getirme, tekli ilişkiler, projelere etiket ve kategori atama gibi Django konseptleri kullanılmıştır. Ayrıca, tek sayfa web sitelerini Django ile nasıl gerçekleştirebileceğimi deneyimleyerek projeyi oluşturdum.

## Kullanılan Yapılar ve Teknolojiler

- **TemplateView:** Sayfa görüntüleme işlemleri için TemplateView kullanılmıştır.
- **Fonksiyon View:** Django fonksiyon view'ları, sayfa işlemlerini yönetmek için kullanılmıştır.
- **URL Parametreleri ile Çalışma:** URL'den alınan id'ye göre proje detaylarını getirme işlemleri uygulanmıştır.
- **Tekli İlişkiler:** Django ORM kullanılarak projelere etiket ve kategori atama işlemleri yapılmıştır.
- **Tek Sayfa Web Sitesi:** Django ile tek sayfa web sitesi oluşturma konsepti deneyimlenmiştir.

## Projeyi Çalıştırma

1. Projeyi bilgisayarınıza klonlayın.
   ```bash
   git clone https://github.com/kullaniciadi/BGPortfolio.git
   ```
2. Virtual environment oluşturun ve etkinleştirin.
   ```bash
   python -m venv venv
   Windows için: env\Scripts\activate
   ```
3. Gerekli paketleri yükleyin.
   ```bash
   pip install -r requirements.txt
   ```
4. Veritabanını oluşturun ve uygulamayı başlatın.
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
5. ```bash
   Tarayıcıda http://127.0.0.1:8000/ adresine giderek projeyi görüntüleyin.
   ```
