from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate  # <-- добавьте импорт
from models import db, User, Hospital, Region
from config import Config
from werkzeug.security import generate_password_hash
import json

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)  # <-- инициализация миграций здесь

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Загрузчик пользователя
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Роуты

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            # Проверка смены пароля (если пароль == '123')
            if password == '123':
                return redirect(url_for('change_password'))
            return redirect(url_for('map_view'))
        else:
            flash('Неверный логин или пароль')
    return render_template('login.html')

@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')
        if new_password != confirm_password:
            flash('Пароли не совпадают')
        elif len(new_password) < 6:
            flash('Пароль должен быть не менее 6 символов')
        else:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Пароль успешно изменен')
            return redirect(url_for('map_view'))
    return render_template('change_password.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def map_view():
    return render_template('map.html')

@app.route('/table')
@login_required
def table_view():
    return render_template('table.html')

@app.route('/api/hospitals', methods=['GET'])
@login_required
def get_hospitals():
    # Получение фильтров из запросов
    region_filter = request.args.get('region')
    city_filter = request.args.get('city')
    license_filter = request.args.get('license_lu')
    hot_beds_filter = request.args.get('hot_beds')
    quotas_filter = request.args.get('quotas_vmp_2025')

    query = Hospital.query

    # Применяем фильтры
    if region_filter:
        # Нужно связать с регионом, если есть связь в модели
        # Упрощенно - фильтрация по городу
        query = query.filter(Hospital.city == city_filter) if city_filter else query

    if license_filter in ['true', 'false']:
        query = query.filter(Hospital.license_lu == (license_filter == 'true'))
    if hot_beds_filter in ['true', 'false']:
        query = query.filter(Hospital.hot_beds == (hot_beds_filter == 'true'))
    if quotas_filter in ['true', 'false']:
        query = query.filter(Hospital.quotas_vmp_2025 == (quotas_filter == 'true'))

    hospitals = query.all()
    result = []
    for h in hospitals:
        result.append({
            'id': h.id,
            'name': h.name,
            'latitude': h.latitude,
            'longitude': h.longitude,
            'city': h.city,
            'address': h.address_full,
            'license_lu': h.license_lu,
            'hot_beds': h.hot_beds,
            'quotas_vmp_2025': h.quotas_vmp_2025,
            'contact_full_name': h.contact_full_name,
            'contact_position': h.contact_position,
            'contact_phone': h.contact_phone,
            'contact_email': h.contact_email,
            'image': h.image_filename,
        })
    return jsonify(result)

@app.route('/api/hospitals', methods=['POST'])
@login_required
def add_hospital():
    data = request.json
    # Валидация данных пропущена для краткости
    hospital = Hospital(
        name=data['name'],
        country=data.get('country', 'Россия'),
        city=data['city'],
        street_type=data['street_type'],
        street_name=data['street_name'],
        address_full=data['address_full'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        license_lu=data.get('license_lu', False),
        hot_beds=data.get('hot_beds', False),
        quotas_vmp_2025=data.get('quotas_vmp_2025', False),
        contact_full_name=data['contact']['full_name'],
        contact_position=data['contact']['position'],
        contact_phone=data['contact']['phone'],
        contact_email=data['contact']['email'],
        image_filename=data.get('image')
    )
    db.session.add(hospital)
    db.session.commit()
    return jsonify({'status': 'success', 'id': hospital.id}), 201

@app.route('/api/hospitals/<int:hospital_id>', methods=['PUT'])
@login_required
def edit_hospital(hospital_id):
    hospital = Hospital.query.get_or_404(hospital_id)
    data = request.json
    # Обновляем поля
    hospital.name = data.get('name', hospital.name)
    hospital.city = data.get('city', hospital.city)
    hospital.street_type = data.get('street_type', hospital.street_type)
    hospital.street_name = data.get('street_name', hospital.street_name)
    hospital.address_full = data.get('address_full', hospital.address_full)
    hospital.latitude = data.get('latitude', hospital.latitude)
    hospital.longitude = data.get('longitude', hospital.longitude)
    hospital.license_lu = data.get('license_lu', hospital.license_lu)
    hospital.hot_beds = data.get('hot_beds', hospital.hot_beds)
    hospital.quotas_vmp_2025 = data.get('quotas_vmp_2025', hospital.quotas_vmp_2025)
    contact = data.get('contact', {})
    hospital.contact_full_name = contact.get('full_name', hospital.contact_full_name)
    hospital.contact_position = contact.get('position', hospital.contact_position)
    hospital.contact_phone = contact.get('phone', hospital.contact_phone)
    hospital.contact_email = contact.get('email', hospital.contact_email)
    # image_filename можно обновить аналогично
    db.session.commit()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)