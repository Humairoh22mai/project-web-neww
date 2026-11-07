from xml.parsers.expat import errors

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

# Kunci rahasia untuk mengamankan session dan flash message
app.secret_key = 'kunci-rahasia-kantin-p06'

# Data menu kantin kampus sederhana untuk tampilan beranda
menu_list = [
    {
        'id': 1,
        'nama': 'Nasi Goreng Spesial',
        'harga': 'Rp 15.000',
        'kategori': 'Makanan',
        'deskripsi': 'Nasi goreng dengan bumbu rempah pilihan, telur mata sapi, dan kerupuk renyah.'
    },
    {
        'id': 2,
        'nama': 'Mie Ayam Bakso',
        'harga': 'Rp 13.000',
        'kategori': 'Makanan',
        'deskripsi': 'Mie kenyal gurih disajikan dengan suwiran ayam manis dan 2 butir bakso sapi.'
    },
    {
        'id': 3,
        'nama': 'Es Teh Manis Jumbo',
        'harga': 'Rp 5.000',
        'kategori': 'Minuman',
        'deskripsi': 'Teh melati segar disajikan dingin manis penyejuk dahaga saat istirahat kuliah.'
    }
]
 
@app.route('/')
def home():
    return render_template('index.html', menu_list=menu_list)


# ====================================================================
# LIVE CODING PRAKTIKUM PERTEMUAN 06
# Langkah 1 & 3: Buat route /register untuk menangani form registrasi member
# ====================================================================
# TULIS KODINGAN ROUTE /register DI SINI SAAT LIVE CODING
# ====================================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 1. Tangkap & Sanitasi input
        nama = request.form.get('nama', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        confirm = request.form.get('confirm', '').strip()

        # 2. Wadah Error Collector
        errors = []

        if not nama:
            errors.append('Nama lengkap wajib diisi!')
        elif len(nama) < 3:
            errors.append('Nama minimal 3 huruf!')

        if not email:
            errors.append('Email wajib diisi!')
        elif '@' not in email or '.' not in email:
            errors.append('Format email tidak valid!')

        if not password:
            errors.append('Password wajib diisi!')
        elif len(password) < 6:
            errors.append('Password minimal 6 karakter!')

        if password != confirm:
            errors.append('Konfirmasi kata sandi tidak cocok!')

        # 3. Keputusan Validasi
        if errors:
            for err in errors:
                flash(err, 'danger')
            return render_template('register.html')

        flash(f'Selamat datang, {nama}! Pendaftaran berhasil.', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
