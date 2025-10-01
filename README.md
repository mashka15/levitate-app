from app import db
from app.models import Product

# Найдем продукт по ID и обновим его поля
product_10 = Product.query.get(10)
if product_10:
    product_10.composition = "Состав: Ферментный комплекс, витамины, минералы."  # Пример состава
    product_10.certificates = "Сертификаты: ISO 9001, GMP."  # Пример сертификатов
    db.session.commit()

product_11 = Product.query.get(11)
if product_11:
    product_11.composition = "Состав: Витамин C, биофлавоноиды, минералы."
    product_11.certificates = "Сертификаты: GMP."
    db.session.commit()

product_12 = Product.query.get(12)
if product_12:
    product_12.composition = "Состав: Масла, экстракты растений, витамины."
    product_12.certificates = "Сертификаты: ISO 22000."
    db.session.commit()

product_13 = Product.query.get(13)
if product_13:
    product_13.composition = "Состав: Экстракты растений, витамин E, коллаген."
    product_13.certificates = "Сертификаты: ECOCERT."
    db.session.commit()

product_14 = Product.query.get(14)
if product_14:
    product_14.composition = "Состав: Молочная кислота, экстракт ромашки."
    product_14.certificates = "Сертификаты: ISO 22716."
    db.session.commit()

product_15 = Product.query.get(15)
if product_15:
    product_15.composition = "Состав: Экстракты трав, увлажняющие компоненты."
    product_15.certificates = "Сертификаты: GMP."
    db.session.commit()

product_16 = Product.query.get(16)
if product_16:
    product_16.composition = "Состав: Бумага высокого качества."
    product_16.certificates = "Сертификаты: FSC."
    db.session.commit()

product_17 = Product.query.get(17)
if product_17:
    product_17.composition = "Состав: Коэнзим Q10, витамины."
    product_17.certificates = "Сертификаты: GMP."
    db.session.commit()

product_18 = Product.query.get(18)
if product_18:
    product_18.composition = "Состав: Селен, витамины группы B."
    product_18.certificates = "Сертификаты: ISO 9001."
    db.session.commit()

print("Данные успешно обновлены!")
