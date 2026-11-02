# Итоговый аналитический отчет (Лабораторная работа №1)
# 1. Резюме
Цель проекта: спроектировать и настроить надежную, стандартизированную инженерную инфраструктуру микросервиса с нуля.
Был выполнен комплексный запуск и базовая настройка процесса разработки для нового Cloud-Native микросервиса «Расчет корзины и скидок» системы лояльности.
# 2. Сравнительный анализ технологий
## 2.1. Матрица принятия решений
<img width="1203" height="213" alt="image" src="https://github.com/user-attachments/assets/3b026d7a-7997-4566-b375-15fb04bf17db" />
## 2.2. Расчет и обоснование выбора
Формула: Оценка = Сумма (Вес_критерия * Балл_кандидата).
# 3. Архитектура и контроль версий
## 3.1. Настройка репозитория
https://github.com/anastasia-shhh/lab1-comprehensive-sannikova
## 3.2. Контроль доступа
<img width="822" height="269" alt="image" src="https://github.com/user-attachments/assets/4bfdcd66-29cf-42e7-9492-054328471d72" />
<img width="869" height="251" alt="image" src="https://github.com/user-attachments/assets/355d6f69-1216-4576-8baf-2fce8504b8fe" />
# 4. Инструментальный контроль качества
## 4.1. Настройка CI/CD
https://github.com/anastasia-shhh/lab1-comprehensive-sannikova/blob/develop/.github/workflows/qa.yml
## 4.2. Работа Quality Gate
-
# 5. Обратное проектирование и планирование ревью
https://github.com/anastasia-shhh/lab1-comprehensive-sannikova/blob/feature/review-plan/docs/uml_diagram.png
## 5.2. План code-review
https://github.com/anastasia-shhh/lab1-comprehensive-sannikova/pull/3
# 6. Заключение
Внедрение автоматического линтера в CI/CD пайплайне и правил защиты веток гарантирует, что дефектный или нерегламентированный код физически не сможет попасть в общую сборку. В сочетании с обязательным ревью от владельцев кода по UML-схемам это сводит к минимуму человеческий фактор и предотвращает логические или финансовые ошибки в расчете скидок.
