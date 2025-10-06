from app import create_app  # Используем функцию create_app

app = create_app()  # Создаем экземпляр приложения с помощью create_app()

if __name__ == "__main__":
    app.run()  # Для локальной разработки, но в продакшн-окружении используем gunicorn
