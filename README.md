## Шаблон для автоматизации тестирования на python
Данный проект содержит автотесты для UI и API тестирования, написанные с использованием паттерна 
Page Object Model (POM) и Allure-отчётов.


### Стек:
- **pytest** – фреймворк для написания тестов
- **selenium** – автоматизация UI
- **requests** – тестирование API
- **allure** – генерация отчётов
- **webdriver-manager** – автоматическое управление драйверами
- **tenacity** – повторные попытки для нестабильных запросов


### Струткура:
- ./tests - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)


### Шаги
1. Склонировать проект `git clone https://github.com/имя_пользователя/pytest_ui_api_template.git`
2. Установить зависимости
3. Запустить тесты `pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Библиотеки (!)
- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure
- pip3 install requests