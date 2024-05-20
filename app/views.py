from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'emir123@gmail.com': {
        'password': 'emir123',
        'role': 'ogrenci'
    },
    'alperen123@gmail.com': {
        'password': 'alperen123',
        'role': 'kurum'
    },
    'eda123@gmail.com': {
        'password': 'eda123',
        'role': 'staj_komisyon_baskani'
    },
    'ertugrul123@gmail.com': {
        'password': 'ertugrul123',
        'role': 'dekan'
    },
    'harun123@gmail.com': {
        'password': 'harun123',
        'role': 'sks'
    },
    'ahmet123@gmail.com': {
        'password': 'ahmet123',
        'role': 'bolum_baskani'
    }
}

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    password = request.form['password']
    if email in users and users[email]['password'] == password:
        role = users[email]['role']
        if role == 'ogrenci':
            return redirect(url_for('ogrenci_bilgi_formu'))
        elif role == 'kurum':
            return redirect(url_for('kurum_formu'))
        elif role == 'staj_komisyon_baskani':
            return redirect(url_for('staj_komisyon_baskani_onay'))
        elif role == 'dekan':
            return redirect(url_for('dekan_onay'))
        elif role == 'sks':
            return redirect(url_for('sks_onay'))
        elif role == 'bolum_baskani':
            return redirect(url_for('bolum_baskani_onay'))
    else:
        return 'Geçersiz email veya şifre. Lütfen tekrar deneyin.'

@app.route('/ogrenci_bilgi_formu')
def ogrenci_bilgi_formu():
    return render_template('ogrenci_bilgi_formu.html')

@app.route('/kurum_formu')
def kurum_formu():
    return render_template('kurumformu.html')

@app.route('/staj_komisyon_baskani_onay')
def staj_komisyon_baskani_onay():
    return render_template('stajkbonayı.html')

@app.route('/dekan_onay')
def dekan_onay():
    return render_template('dekanlıkonayı.html')

@app.route('/sks_onay')
def sks_onay():
    return render_template('sksonayı.html')

@app.route('/bolum_baskani_onay')
def bolum_baskani_onay():
    return render_template('bölümbaşkanı.html')

if __name__ == '__main__':
    app.run(debug=True)
