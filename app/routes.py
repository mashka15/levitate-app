from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
from app.models import Product, Order

main = Blueprint('main', __name__)



# Главная страница
@main.route('/')
def home():
    cart_items = session.get('cart', [])
    total_items = sum(item['quantity'] for item in cart_items)

    products = []
    product1 = Product.query.get(13)
    product2 = Product.query.get(17)
    if product1:
        products.append(product1)
    if product2:
        products.append(product2)

    return render_template('index.html', products=products, total_items=total_items)

# Страница продуктов
@main.route('/products')
def products():
    best_sellers = Product.query.filter_by(is_best_seller=True).all()
    others = Product.query.filter_by(is_best_seller=False).all()
    all_products = best_sellers + others

    # Преобразуем объекты продуктов в список словарей, используя to_dict()
    products_data = [product.to_dict() for product in all_products]

    cart_items = session.get('cart', [])
    total_items = sum(item['quantity'] for item in cart_items)
    return render_template('products.html', products=products_data, total_items=total_items)



from flask import request, redirect, url_for, flash

from flask import request, redirect, url_for, flash, render_template
from app import app, db
from app.models import CooperationFormData

from flask import request, redirect, url_for, flash

@main.route('/cooperation', methods=['GET', 'POST'])
def cooperation():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not (name and email and message):
            flash("Пожалуйста, заполните все поля", "error")
            return redirect(url_for('main.cooperation'))

        existing = CooperationFormData.query.filter_by(email=email).first()
        if existing:
            flash("Пользователь с таким email уже существует.", "error")
            return redirect(url_for('main.cooperation'))

        data = CooperationFormData(name=name, email=email, message=message)

        try:
            db.session.add(data)
            db.session.commit()
            flash("Сообщение успешно отправлено!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Ошибка при сохранении: {str(e)}", "error")

        return redirect(url_for('main.cooperation'))

    return render_template('cooperation.html')

# Страница корзины
@main.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    total_items = sum(item.get('quantity', 0) for item in cart_items) or 0
    print("Cart items in session:", cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price, total_items=total_items)

# Добавление товара в корзину
@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form.get('quantity', 1))  # Получаем количество товара, по умолчанию 1

    # Получаем текущую корзину из сессии (если нет - создаем пустой список)
    cart = session.get('cart', [])

    # Проверяем, если товар уже в корзине
    for item in cart:
        if item['id'] == product.id:
            item['quantity'] += quantity  # увеличиваем количество
            break
    else:
        # Если товара нет в корзине, добавляем новый элемент
        cart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': quantity,
            'image': product.image_url
        })

    session['cart'] = cart  # сохраняем корзину в сессии
    session.modified = True  # Обязательно указать, что сессия изменилась, чтобы данные сохранились

    return redirect(url_for('main.cart'))

# Удаление товара из корзины
@main.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]  # удаляем товар по id
    session['cart'] = cart  # обновляем корзину в сессии
    return redirect(url_for('main.cart'))

# Оформление заказа из корзины
@main.route('/checkout', methods=['POST'])
def checkout():
    cart_items = session.get('cart', [])
    if not cart_items:
        return redirect(url_for('main.cart'))  # если корзина пуста, редиректим обратно

    # Создаем заказ для каждого товара в корзине
    for item in cart_items:
        new_order = Order(
            product_id=item['id'],
            quantity=item['quantity'],
            address=request.form['address']  # Адрес доставки
        )
        db.session.add(new_order)

    db.session.commit()
    session.pop('cart', None)  # Очищаем корзину
    return redirect(url_for('main.orders'))  # редирект на страницу с заказами

from flask import render_template, abort

@main.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)

    # Мапа id товара -> список фото (пути относительно папки static)
    product_images_map = {
        10: ['images/89792760.jpg', 'images/98349287_converted.jpg', 'images/106A5985.jpg'],
        11: ['images/106A5711.jpg', 'images/106A5690.jpg', 'images/106A5483.jpg'],
        12: ['images/106A9122.jpeg', 'images/106A8918.jpg', 'images/106A5853.jpg'],
        13: ['images/photo_2025-09-28_11-28-09.jpg', 'images/photo_2025-09-28_15-02-28.jpg', 'images/photo_2025-09-28_13-36-10.jpg', 'images/photo_2025-09-28_13-57-57.jpg'],
        14: ['images/DSC_0141.jpg', 'images/IMG_3030.jpeg', 'images/106A8823.jpg'],
        15: ['images/D6792057-7EB4-47E8-8A02-0E13B1CA8A19-7465-0000041405CC670F.jpg', 'images/98be42d7-ab84-4220-bb0c-a9f0afe2d12b.png'],
        16: ['images/34764212.jpg'],
        17: ['images/photo_2025-09-28_12-39-47.jpg', 'images/photo_2025-09-28_13-36-11.jpg', 'images/photo_2025-09-28_13-56-14.jpg', 'images/photo_2025-09-28_13-56-15.jpg'],
        18: ['images/photo_2025-09-28_11-24-33.jpg', 'images/photo_2025-09-28_13-53-04.jpg', 'images/photo_2025-09-28_13-57-10.jpg', 'images/photo_2025-09-28_13-57-10 (2).jpg'],
    }

    product_images = product_images_map.get(product_id, [])

    return render_template('product_details.html', product=product, product_images=product_images)

# Страница каталог
@main.route('/catalog')
def catalog():
    return render_template('catalog.html')  # Убедитесь, что у вас есть такая страница
