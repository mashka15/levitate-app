from app import create_app  # Импортируем функцию create_app

app = create_app()  # Создаем экземпляр приложения с помощью create_app()

if __name__ == "__main__":
    app.run()  # Запуск приложения локально для тестирования
