# Довідник по бібліотеці `tkinter` для фінального проєкту

**`tkinter`** — це стандартна бібліотека Python для створення графічного інтерфейсу користувача (GUI — вікон, кнопок, полів введення та списків). Вона вже вбудована у Python, тому встановлювати її через `pip` не потрібно.

---

## 1. Базовий каркас вікна

Будь-яка програма на `tkinter` складається з 4 обов'язкових кроків:
1. Імпорт бібліотеки (`import tkinter as tk`).
2. Створення головного вікна (`root = tk.Tk()`).
3. Налаштування параметрів вікна та додавання елементів (**віджетів**).
4. Запуск головного циклу обробки подій (`root.mainloop()`), який утримує вікно відкритим і реагує на натискання кнопок.

```python
import tkinter as tk

root = tk.Tk()
root.title("Пошукова система")     # Заголовок вікна
root.geometry("650x500")          # Розмір вікна: ширина x висота у пікселях
root.resizable(False, False)      # Заборонити зміну розміру вікна (за бажанням)

# Тут додаються всі віджети (кнопки, поля, написи)

root.mainloop()                   # Обов'язковий рядок у самому кінці

```

---

## 2. Основні віджети (елементи інтерфейсу)

Усі елементи на екрані в `tkinter` називаються **віджетами**. Першим аргументом при створенні будь-якого віджета завжди передається батьківський контейнер (наприклад, `root` або `frame`), у якому він розміщується.

### 1. `tk.Label` — Текстовий напис (підказка або заголовок)

Використовується для підписів біля полів введення або заголовків розділів.

```python
label = tk.Label(root, text="Введіть посилання на сайт:", font=("Arial", 11))

```

### 2. `tk.Entry` — Однорядкове поле введення

Використовується для введення URL-адреси або пошукового слова.

* **`entry.get()`** — повертає рядок, який користувач ввів у поле.
* **`entry.delete(0, tk.END)`** — повністю очищає поле від нульового символу до кінця.
* **`entry.insert(0, "https://")`** — вставляє початковий текст у поле.

```python
url_entry = tk.Entry(root, width=45, font=("Arial", 11))

```

### 3. `tk.Button` — Кнопка

Виконується певна функція або метод при натисканні.

* Параметр **`command`** приймає **посилання на функцію без дужок** (`command=self.add_site`, а не `command=self.add_site()`). Якщо поставити дужки, функція спрацює одразу при запуску програми, а не при натисканні!

```python
add_btn = tk.Button(
    root,
    text="Додати сайт",
    command=on_add_click,
    bg="#4CAF50",       # Колір фону кнопки
    fg="white",         # Колір тексту
    font=("Arial", 10, "bold")
)

```

### 4. `tk.Text` — Багаторядкове текстове поле (для виведення результатів)

Зручний віджет для відображення списку сайтів та результатів пошуку.

* **`text_box.delete("1.0", tk.END)`** — очищає все поле (від 1-го рядка, 0-го символу до кінця).
* **`text_box.insert(tk.END, "Новий рядок\n")`** — додає текст у кінець поля (не забувайте `\n` для переходу на новий рядок).
* **`state="disabled"` / `state="normal"**` — блокує поле, щоб користувач не міг випадково стерти результати з клавіатури (перед вставкою тексту через код стан перемикають у `"normal"`, а після вставки повертають у `"disabled"`).

```python
result_box = tk.Text(root, width=72, height=18, font=("Consolas", 10))

```

### 5. `tk.Frame` — Контейнер (рамка для групування елементів)

Невидимий блок, у який зручно покласти кілька елементів поруч (наприклад, в один рядок поставити поле введення та дві кнопки).

```python
top_frame = tk.Frame(root)
# Тепер віджети можна додавати всередину top_frame замість root

```

---

## 3. Розміщення віджетів на екрані (Менеджери геометрії)

Створити віджет недостатньо — його потрібно розмістити у вікні. У `tkinter` для цього є два основні способи.

> **Важливе правило:** ніколи не змішуйте `.pack()` і `.grid()` в одному контейнері (наприклад, одночасно у `root`), інакше програма зависне! Проте можна розмістити кілька `Frame` через `.pack()`, а всередині одного `Frame` використати `.grid()`.

### Спосіб 1: `.pack()` — Послідовне пакування (зверху вниз або зліва направо)

Найпростіший спосіб: елементи стають один за одним.

* `side=tk.TOP` (за замовчуванням) — ставити зверху вниз.
* `side=tk.LEFT` — ставити в один рядок зліва направо.
* `padx=10, pady=5` — зовнішні відступи по горизонталі та вертикалі у пікселях (щоб елементи не злипалися).
* `fill=tk.X` — розтягнути віджет на всю ширину вікна.

```python
label.pack(pady=5)
url_entry.pack(pady=5)
add_btn.pack(pady=5)

```

### Спосіб 2: `.grid()` — Розміщення по таблиці (рядки та стовпці)

Ідеально підходить, коли потрібно поставити підпис, поле введення та кнопку рівно в один рядок:

* `row` — номер рядка (починається з `0`).
* `column` — номер стовпця (починається з `0`).
* `columnspan` — розтягнути елемент на кілька стовпців одразу (як об'єднання комірок у Excel).

```python
# Рядок 0: Поле URL + кнопка "Додати" + кнопка "Очистити БД"
url_entry.grid(row=0, column=0, padx=5, pady=5)
add_btn.grid(row=0, column=1, padx=5, pady=5)
clear_btn.grid(row=0, column=2, padx=5, pady=5)

# Рядок 1: Поле пошуку + кнопка "Знайти"
search_entry.grid(row=1, column=0, padx=5, pady=5)
search_btn.grid(row=1, column=1, columnspan=2, sticky="ew", padx=5, pady=5)

```

---

## 4. Спливаючі діалогові вікна (`messagebox`)

Для сповіщень про помилки, успішне додавання або підтвердження видалення використовують окремий підмодуль **`messagebox`**:

```python
from tkinter import messagebox

# 1. Інформаційне вікно
messagebox.showinfo("Успіх", "Сайт успішно додано до бази даних!")

# 2. Попередження
messagebox.showwarning("Увага", "Поле пошуку не може бути порожнім!")

# 3. Вікно помилки
messagebox.showerror("Помилка", "Не вдалося підключитися до бази даних.")

# 4. Вікно підтвердження (повертає True, якщо натиснули "Так", і False, якщо "Ні")
answer = messagebox.askyesno("Підтвердження", "Ви дійсно хочете очистити всю базу сайтів?")
if answer:
    print("Базу очищено!")

```

---

## 5. Поєднання `tkinter` з ООП (Готовий шаблон класу інтерфейсу)

У фінальному проєкті інтерфейс має бути оформлений як окремий клас `SearchAppUI`, який приймає об'єкти бази даних (`db`) та парсера (`parser`):

```python
import tkinter as tk
from tkinter import messagebox


class SearchAppUI:
    def __init__(self, db, parser):
        self.db = db
        self.parser = parser

        self.root = tk.Tk()
        self.root.title("Пошук по збережених сайтах")
        self.root.geometry("680x500")

        self._build_ui()

    def _build_ui(self):
        # Верхня панель керування (сітка)
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Рядок 0: Додавання URL
        tk.Label(control_frame, text="URL сайту:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.url_entry = tk.Entry(control_frame, width=40)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(control_frame, text="Додати сайт", command=self.on_add_site, width=14).grid(row=0, column=2, padx=5)
        tk.Button(control_frame, text="Очистити БД", command=self.on_clear_db, width=14).grid(row=0, column=3, padx=5)

        # Рядок 1: Пошуковий запит
        tk.Label(control_frame, text="Пошук:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.search_entry = tk.Entry(control_frame, width=40)
        self.search_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(control_frame, text="Знайти", command=self.on_search, width=14).grid(row=1, column=2, padx=5)
        tk.Button(control_frame, text="Усі сайти", command=self.on_show_sites, width=14).grid(row=1, column=3, padx=5)

        # Нижня панель: Поле виведення результатів
        self.result_box = tk.Text(self.root, width=80, height=20, font=("Consolas", 10))
        self.result_box.pack(padx=10, pady=10)

    def _print_to_box(self, text, clear=False):
        if clear:
            self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, text + "\n")

    def on_add_site(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Увага", "Введіть посилання на сайт!")
            return
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        # Виклик методу класу DatabaseManager
        added = self.db.add_url(url)
        if added:
            self.url_entry.delete(0, tk.END)
            self._print_to_box(f"[+] Додано: {url}", clear=True)
        else:
            messagebox.showinfo("Інформація", "Цей сайт уже є в базі даних.")

    def on_show_sites(self):
        urls = self.db.get_all_urls()
        self._print_to_box("=== Збережені сайти у БД ===", clear=True)
        if not urls:
            self._print_to_box("База даних порожня.")
            return
        for idx, url in enumerate(urls, start=1):
            self._print_to_box(f"{idx}. {url}")

    def on_clear_db(self):
        if messagebox.askyesno("Підтвердження", "Видалити всі сайти з бази даних?"):
            self.db.clear_database()
            self._print_to_box("Базу даних очищено.", clear=True)

    def on_search(self):
        query = self.search_entry.get().strip()
        if not query:
            messagebox.showwarning("Увага", "Введіть слово або фразу для пошуку!")
            return

        urls = self.db.get_all_urls()
        if not urls:
            messagebox.showinfo("Порожня база", "Спочатку додайте хоча б один сайт.")
            return

        self._print_to_box(f"Шукаємо '{query}' на {len(urls)} сайтах...", clear=True)
        self.root.update()  # Оновлює вікно до початку завантаження сторінок

        results = self.parser.search(urls, query)
        self._print_to_box(f"=== Результати пошуку за запитом '{query}' ===\n", clear=True)
        for rank, (url, count) in enumerate(results, start=1):
            self._print_to_box(f"{rank}. {url} — знайдено збігів: {count}")

    def start(self):
        self.root.mainloop()

```

---

## 6. Корисні покращення для інтерфейсу (за бажанням)

* **Полоса прокрутки (`tk.Scrollbar`):** якщо результатів багато, до поля `tk.Text` можна прикріпити вертикальний скролбар:
```python
scrollbar = tk.Scrollbar(self.root, command=self.result_box.yview)
self.result_box.config(yscrollcommand=scrollbar.set)

```


* **Запуск пошуку клавішею `Enter`:** можна прив'язати натискання `Enter` у полі пошуку до кнопки «Знайти»:
```python
self.search_entry.bind("<Return>", lambda event: self.on_search())

```


* **Сучасний вигляд (`customtkinter`):** якщо хочеться зробити інтерфейс із темною темою та заокругленими кнопками, можна встановити бібліотеку `pip install customtkinter` — її класи (`CTk`, `CTkButton`, `CTkEntry`, `CTkTextbox`) працюють за тими самими принципами, що й стандартний `tkinter`.

---

## Корисні посилання

* [Офіційна документація Python: tkinter](https://docs.python.org/3/library/tkinter.html)`
* [Документація Python: tkinter.messagebox](https://docs.python.org/3/library/tkinter.messagebox.html)`
* [Довідник по віджетах і параметрах `tkinter` (TkDocs)](https://tkdocs.com/tutorial/)
* [Документація `CustomTkinter` (сучасний дизайн для `tkinter`)](https://customtkinter.tomschimansky.com/)
