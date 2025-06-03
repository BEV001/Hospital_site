{% extends "base.html" %}
{% block title %}Таблица центров ядерной медицины{% endblock %}
{% block head_scripts %}
<style>
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  padding: 8px;
  border: 1px solid #ddd;
}
th {
  background-color: #f0f0f0;
}
#modalContainer {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  z-index: 9999;
}
#hotBedsCountContainer {
  margin-left: 20px;
  margin-bottom: 10px;
}
</style>
{% endblock %}
{% block content %}
<h1>Таблица больниц</h1>

<form id="filterForm">
    <label>Город:
        <input type="text" name="city" id="cityFilter" placeholder="Введите город" />
    </label>

    <label>
        <input type="checkbox" name="license_lu" value="true" /> Лицензия ЛУ
    </label>
    <label>
        <input type="checkbox" name="hot_beds" value="true" /> Горячие койки
    </label>
    <label>
        <input type="checkbox" name="quotas_vmp_2025" value="true" /> Квоты ВМП 2025
    </label>

    <button type="submit">Применить фильтры</button>
    <button type="button" id="btnAddHospital">Добавить больницу</button>
</form>

<table id="hospitalsTable">
    <thead>
        <tr>
            <th>Название</th>
            <th>Город</th>
            <th>Адрес</th>
            <th>Лицензия ЛУ</th>
            <th>Горячие койки</th>
            <th>Число горячих коек</th>
            <th>Квоты ВМП 2025</th>
            <th>План Lu 2025</th>
            <th>Продано (итого)</th>
            <th>Остаток</th>
            <th>Контакт</th>
            <th>Телефон</th>ы
            <th>Email</th>
            <th>Действия</th>
        </tr>
    </thead>
    <tbody>
    <!-- Данные подгружаются JS -->
    </tbody>
</table>

<!-- Модальное окно для добавления и редактирования -->
<div id="modalContainer" style="display:none;">
    <div id="modalContent" style="background:#fff; padding:20px; border:1px solid #ccc; max-width:600px; margin:40px auto; position:relative;">
        <button id="modalClose" style="position:absolute; top:10px; right:10px;">X</button>
        <div id="modalBody"></div>
    </div>
</div>

{% endblock %}

{% block scripts %}
<script>
function openModal(contentHtml) {
    $('#modalBody').html(contentHtml);
    $('#modalContainer').show();
    // Навесим обработчик для переключения видимости поля количества горячих коек
    $('#chkHotBeds').off('change').on('change', function() {
        if ($(this).is(':checked')) {
            $('#hotBedsCountContainer').show();
        } else {
            $('#hotBedsCountContainer').hide();
            $('#hotBedsCountContainer input[name="hot_beds_count"]').val(0);
        }
    });
}

function closeModal() {
    $('#modalContainer').hide();
    $('#modalBody').html('');
}

$('#modalClose').on('click', closeModal);

$('#btnAddHospital').on('click', function() {
    openModal(renderHospitalForm());
});

function renderHospitalForm(hospital = {}) {
    return `
<form id="hospitalForm" enctype="multipart/form-data">
  <input type="hidden" name="id" value="${hospital.id || ''}">

  <label>Название:<br>
    <input type="text" name="name" value="${hospital.name || ''}" required>
  </label><br>

  <label>Страна:<br>
    <input type="text" name="country" value="${hospital.country || 'Россия'}" readonly>
  </label><br>

  <label>Область:<br>
    <input type="text" name="region" value="${hospital.region || ''}" required>
  </label><br>

  <label>Город:<br>
    <input type="text" name="city" value="${hospital.city || ''}" required>
  </label><br>

  <label>Тип улицы:<br>
    <select name="street_type" required>
      <option value="шоссе" ${hospital.street_type === 'шоссе' ? 'selected' : ''}>шоссе</option>
      <option value="бульвар" ${hospital.street_type === 'бульвар' ? 'selected' : ''}>бульвар</option>
      <option value="улица" ${hospital.street_type === 'улица' ? 'selected' : ''}>улица</option>
      <option value="площадь" ${hospital.street_type === 'площадь' ? 'selected' : ''}>площадь</option>
      <option value="проспект" ${hospital.street_type === 'проспект' ? 'selected' : ''}>проспект</option>
      <option value="переулок" ${hospital.street_type === 'переулок' ? 'selected' : ''}>переулок</option>
      <option value="набережная" ${hospital.street_type === 'набережная' ? 'selected' : ''}>набережная</option>
    </select>
  </label><br>

  <label>Улица:<br>
    <input type="text" name="street_name" value="${hospital.street_name || ''}" required>
  </label><br>

  <label>Дом:<br>
    <input type="text" name="house" value="${hospital.house || ''}" required>
  </label><br>

  <label>Корпус/строение:<br>
    <input type="text" name="building" value="${hospital.building || ''}">
  </label><br>

  <label>Широта:<br>
    <input type="text" name="latitude" value="${hospital.latitude || ''}" pattern="^-?\\d+(\\.\\d+)?$" title="Введите корректное число" required>
  </label><br>

  <label>Долгота:<br>
    <input type="text" name="longitude" value="${hospital.longitude || ''}" pattern="^-?\\d+(\\.\\d+)?$" title="Введите корректное число" required>
  </label><br>

  <label>Загрузить изображение:<br>
    <input type="file" name="image" accept="image/*">
  </label><br>

  <label><input type="checkbox" name="license_lu" ${hospital.license_lu ? 'checked' : ''}> Лицензия Lu</label><br>

  <label><input type="checkbox" name="hot_beds" id="chkHotBeds" ${hospital.hot_beds ? 'checked' : ''}> Горячие койки</label><br>

  <div id="hotBedsCountContainer" style="display: ${hospital.hot_beds ? 'block' : 'none'};">
    <label>Число горячих коек:<br>
      <input type="number" name="hot_beds_count" min="0" value="${hospital.hot_beds_count != null ? hospital.hot_beds_count : 0}">
    </label><br>
  </div>

  <label><input type="checkbox" name="quotas_vmp_2025" ${hospital.quotas_vmp_2025 ? 'checked' : ''}> Квоты ВМП 2025</label><br>

  <label>План Lu 2025:<br>
    <input type="number" name="plan_lu_2025" min="0" value="${hospital.plan_lu_2025 != null ? hospital.plan_lu_2025 : 0}">
  </label><br>

  <label>Продажи по месяцам (JSON):<br>
    <textarea name="sales_lu_2025" rows="4" placeholder='{"2024-01": 5, "2024-02": 8}'>${hospital.sales_lu_2025 ? JSON.stringify(hospital.sales_lu_2025, null, 2) : ''}</textarea>
  </label><br>
  <fieldset>
    <legend>Контактная информация</legend>
    <label>ФИО:<br>
      <input type="text" name="contact_full_name" value="${hospital.contact_full_name || ''}">
    </label><br>
    <label>Должность:<br>
      <input type="text" name="contact_position" value="${hospital.contact_position || ''}">
    </label><br>
    <label>Телефон:<br>
      <input type="text" name="contact_phone" value="${hospital.contact_phone || ''}">
    </label><br>
    <label>Email:<br>
      <input type="email" name="contact_email" value="${hospital.contact_email || ''}">
    </label><br>
  </fieldset>

  <button type="submit">Сохранить</button>
</form>
    `;
}

function fetchHospitals(filters = {}) {
    let params = new URLSearchParams(filters);
    fetch('/api/hospitals?' + params.toString())
    .then(res => res.json())
    .then(data => {
        const tbody = $('#hospitalsTable tbody');
        tbody.empty();
        data.forEach(hospital => {
            const hotBedsDisplay = hospital.hot_beds 
                ? 'Да' 
                : 'Нет';

            const hotBedsCountDisplay = hospital.hot_beds 
                ? (hospital.hot_beds_count != null ? hospital.hot_beds_count : '0') 
                : '-';

            const planLu2025 = hospital.plan_lu_2025 != null ? hospital.plan_lu_2025 : 0;

            const salesLu2025 = hospital.sales_lu_2025 || {};
            const totalSold = Object.values(salesLu2025).reduce((a,b) => a + b, 0);

            const remainder = planLu2025 - totalSold;

            const row = $(`
                <tr>
                    <td>${hospital.name}</td>                            <!-- Название -->
                    <td>${hospital.city}</td>                            <!-- Город -->
                    <td>${hospital.address || ''}</td>                   <!-- Адрес -->
                    <td>${hospital.license_lu ? 'Да' : 'Нет'}</td>      <!-- Лицензия ЛУ -->
                    <td>${hotBedsDisplay}</td>                            <!-- Горячие койки -->
                    <td>${hotBedsCountDisplay}</td>                       <!-- Число горячих коек -->
                    <td>${hospital.quotas_vmp_2025 ? 'Да' : 'Нет'}</td>  <!-- Квоты ВМП 2025 -->
                    <td>${planLu2025}</td>                                <!-- План Lu 2025 -->
                    <td>${totalSold}</td>                                 <!-- Продано (итого) -->
                    <td>${remainder >= 0 ? remainder : 0}</td>           <!-- Остаток -->
                    <td>${hospital.contact_full_name || ''}</td>         <!-- Контакт -->
                    <td>${hospital.contact_phone || ''}</td>             <!-- Телефон -->
                    <td>${hospital.contact_email || ''}</td>             <!-- Email -->
                    <td>
                        <button class="editBtn" data-id="${hospital.id}">Редактировать</button>
                    </td>
                </tr>
            `);
            tbody.append(row);
        });
    });
}

$('#filterForm').on('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const filters = {};
    for (const [key, value] of formData.entries()) {
        if (key === 'license_lu' || key === 'hot_beds' || key === 'quotas_vmp_2025') {
            filters[key] = 'true';
        } else if (value.trim() !== '') {
            filters[key] = value;
        }
    }
    fetchHospitals(filters);
});

// Обработка клика на редактирование
$('#hospitalsTable').on('click', '.editBtn', function() {
    const id = $(this).data('id');
    fetch(`/api/hospitals/${id}`)
    .then(res => {
        if (!res.ok) throw new Error('Больница не найдена');
        return res.json();
    })
    .then(hosp => {
        openModal(renderHospitalForm(hosp));
    })
    .catch(err => alert(err.message));
});

// Обработка отправки формы добавления/редактирования
$('#modalContainer').on('submit', '#hospitalForm', function(e) {
    e.preventDefault();
    const formData = new FormData(this);

    const streetType = formData.get('street_type');
    const streetName = formData.get('street_name');
    const house = formData.get('house');
    const building = formData.get('building');

    const addressFull = `${streetType} ${streetName}, д. ${house}` + (building ? `, корп. ${building}` : '');

    const id = formData.get('id');

    // Для координат парсим float, если пусто - ставим null
    const latitudeRaw = formData.get('latitude');
    const longitudeRaw = formData.get('longitude');
    const latitude = latitudeRaw ? parseFloat(latitudeRaw) : null;
    const longitude = longitudeRaw ? parseFloat(longitudeRaw) : null;

    // Обработка чекбоксов
    const licenseLu = formData.has('license_lu');
    const hotBeds = formData.has('hot_beds');
    const quotasVmp2025 = formData.has('quotas_vmp_2025');

    // Обработка количества горячих коек
    let hotBedsCountRaw = formData.get('hot_beds_count');
    let hotBedsCount = 0;
    if (hotBeds && hotBedsCountRaw) {
        hotBedsCount = parseInt(hotBedsCountRaw, 10);
        if (isNaN(hotBedsCount) || hotBedsCount < 0) hotBedsCount = 0;
    }

    const planLu2025Raw = formData.get('plan_lu_2025');
    const planLu2025 = planLu2025Raw ? parseInt(planLu2025Raw, 10) : 0;

    let salesLu2025Raw = formData.get('sales_lu_2025');
    let salesLu2025 = {};
    if (salesLu2025Raw) {
      try {
        salesLu2025 = JSON.parse(salesLu2025Raw);
      } catch(e) {
        alert('Неверный формат JSON в поле продаж по месяцам');
        return;
      }
    }

    // Обработка файла (пока не загружаем, просто игнорируем - можно реализовать отдельно)
    const image = null;

    const data = {
        name: formData.get('name'),
        country: formData.get('country'),
        region: formData.get('region'),
        city: formData.get('city'),
        street_type: streetType,
        street_name: streetName,
        house: house,
        building: building,
        address_full: addressFull,
        latitude: latitude,
        longitude: longitude,
        license_lu: licenseLu,
        hot_beds: hotBeds,
        hot_beds_count: hotBedsCount,
        quotas_vmp_2025: quotasVmp2025,
        contact_full_name: formData.get('contact_full_name'),
        contact_position: formData.get('contact_position'),
        contact_phone: formData.get('contact_phone'),
        contact_email: formData.get('contact_email'),
        image: image,

        plan_lu_2025: planLu2025,
        sales_lu_2025: salesLu2025
    };

    if (!id) {
        // Добавление
        fetch('/api/hospitals', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        })
        .then(res => {
            if (res.status === 201) return res.json();
            else throw new Error('Ошибка при добавлении');
        })
        .then(() => {
            alert('Больница добавлена');
            closeModal();
            fetchHospitals();
        })
        .catch(err => alert(err.message));
    } else {
        // Редактирование
        fetch(`/api/hospitals/${id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        })
        .then(res => {
            if (res.ok) return res.json();
            else throw new Error('Ошибка при редактировании');
        })
        .then(() => {
            alert('Больница обновлена');
            closeModal();
            fetchHospitals();
        })
        .catch(err => alert(err.message));
    }
});

// Загрузка списка при старте
fetchHospitals();

</script>
{% endblock %}
