
# Заняття 7. Ітератори. Генератори. Замикання. Декоратори

У цьому конспекті зібрано теоретичний матеріал про те, як влаштовані ітерації «під капотом» у Python, як економити оперативну пам'ять за допомогою «лінивих» обчислень та як розширювати поведінку функцій за допомогою замикань і декораторів.

---

## 1. Ітератори та ітеровані об'єкти

### У чому різниця?
* **Ітерований об'єкт (Iterable)** — це будь-який об'єкт, по якому можна пройтися в циклі `for` (наприклад, `list`, `str`, `tuple`, `dict`, `set`). Він знає, як створити ітератор, але сам не зберігає поточну позицію обходу.
* **Ітератор (Iterator)** — це спеціальний об'єкт-потік, який видає елементи по одному за запитом і пам'ятає, на якому місці зупинився. Коли елементи закінчуються, ітератор генерує виняток `StopIteration`.

Головна перевага ітераторів — **«ліниві» обчислення (lazy evaluation)**: елементи не зберігаються в пам'яті всі одразу, а обчислюються лише в момент звернення до них.

### Функції `iter()` та `next()`

Під час запуску циклу `for` Python автоматично перетворює ітерований об'єкт на ітератор за допомогою `iter()` і на кожному кроці викликає `next()`. Це можна зробити і вручну:

```python
my_list = [1, 2, 3]
iterator = iter(my_list)  # Створюємо об'єкт-ітератор

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator)) -> Викличе виняток StopIteration

```

> **Особливість ітератора:** Він одноразовий. Коли ви пройшли по ньому до кінця (через `next()` або цикл `for`), він стає «порожнім». Щоб пройтися знову, потрібно створити новий ітератор через `iter()`.

### Створення власного ітератора (протокол ітерації)

Щоб зробити власний клас ітерованим, потрібно реалізувати два магічні методи (протокол ітератора):

* `__iter__(self)` — повертає сам об'єкт ітератора (`return self`) і за потреби скидає лічильник у початковий стан.
* `__next__(self)` — повертає наступний елемент послідовності або генерує `raise StopIteration`, коли елементи вичерпано.

```python
class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)
for elem in count:
    print(elem)  # Виведе числа від 1 до 5

```

---

## 2. Генератори

**Генератор** — це спрощений спосіб створення ітератора у вигляді функції. Замість написання класу з методами `__iter__()` та `__next__()`, ми пишемо звичайну функцію, але замість `return` використовуємо ключове слово `yield`.

### Як працює `yield`?

Коли Python зустрічає `yield`, функція **не завершується** (як при `return`), а ставить своє виконання «на паузу», заморожує всі локальні змінні та віддає значення назовні. При наступному виклику `next()` виконання продовжується з того самого місця.

```python
def raise_to_the_degrees(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number ** i
        i += 1

res = raise_to_the_degrees(2, 5)
print(res)  # <generator object raise_to_the_degrees at ...>

for val in res:
    print(val)  # 1, 2, 4, 8, 16

```

### Нескінченні послідовності та зупинка генератора

Оскільки генератор обчислює лише одне значення за раз, він може працювати нескінченно, не переповнюючи оперативну пам'ять. Щоб достроково завершити роботу генератора за певної умови, використовують `return` (який «під капотом» викликає `StopIteration`):

```python
def raise_to_the_degrees(number):
    i = 0
    while True:
        result = number ** i
        yield result
        if result > 100 ** 5:
            return  # Зупиняє генератор (генерує StopIteration)
        i += 1

```

### Генераторні вирази (Generator Expressions)

Крім функцій з `yield`, генератор можна створити в один рядок — синтаксис схожий на генератор списків (list comprehension), але замість квадратних дужок `[]` використовуються круглі `()`:

```python
squares_list = [x ** 2 for x in range(1000000)]  # Одразу займає пам'ять під 1 млн чисел
squares_gen = (x ** 2 for x in range(1000000))   # Майже не займає пам'ять, рахує по одному

```

---

## 3. Виклик об'єктів та замикання функцій (Closures)

### Виклик екземплярів класу: метод `__call__`

У Python викликати через круглі дужки `()` можна не лише функції, а й об'єкти класів, якщо в класі визначено метод `__call__()`. Це дозволяє об'єкту зберігати внутрішній стан між викликами:

```python
class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, new_work):
        return f"I will help you with your {self.work}. Afterwards I will help you with {new_work}"

helper = Helper("homework")
print(helper("cleaning"))  # Викликаємо об'єкт як функцію

```

### Замикання (Closures)

У функціональному програмуванні ту саму поведінку (збереження стану без використання класів) реалізують за допомогою **замикань**.

**Замикання** виникає тоді, коли вкладена функція посилається на змінні із зовнішньої функції, а зовнішня функція повертає цю вкладену функцію як результат. Навіть після завершення роботи зовнішньої функції вкладена функція «пам'ятає» оточення, в якому була створена.

```python
def helper(work):
    work_in_memory = work  # Змінна зовнішньої області видимості

    def inner_helper(new_work):
        # Вкладена функція «замикає» в собі work_in_memory
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {new_work}"

    return inner_helper  # Повертаємо саму функцію (без дужок!)

my_helper = helper("homework")
print(my_helper("cleaning"))
print(my_helper("driving"))

```

---

## 4. Декоратори

**Декоратор** — це патерн проєктування (побудований на замиканнях), який дозволяє «обгорнути» іншу функцію, щоб додати їй нову поведінку (логіку до або після виклику, логування, перевірку прав, обробку помилок) **без зміни коду самої функції**.

### Як декоратор працює без синтаксичного цукру

Декоратор приймає функцію як аргумент і повертає нову функцію-обгортку (`wrapper`):

```python
def checker(function):
    def wrapper(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems: {exc}")
        else:
            print(f"No problems. Result - {result}")
            return result
    return wrapper

def calculate(expression):
    return eval(expression)

calculate = checker(calculate)  # Ручне декорування
calculate("2 + 2")

```

### Синтаксичний цукор `@`

Щоб не переприсвоювати функцію вручну, у Python використовують символ `@` перед оголошенням функції:

```python
@checker
def calculate(expression):
    return eval(expression)

calculate("2 + 2")
calculate("2 / 0")  # Помилка буде перехоплена декоратором

```

### Декоратори з параметрами (декоратори вищого порядку)

Якщо декоратору потрібно передати власні налаштування (наприклад, кортеж винятків, які слід перехоплювати), створюється ще один зовнішній рівень вкладеності:

```python
def checker(*exc_types):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except exc_types as exc:
                print(f"We have problems: {exc}")
            else:
                print(f"No problems. Result - {result}")
                return result
        return wrapper
    return decorator

@checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
    return eval(expression)

calculate("2 + 2")
calculate("unknown_var + 5")

```

### Збереження метаданих функції (`functools.wraps`)

Коли функція обгортається декоратором, її ім'я (`__name__`) та документація (`__doc__`) замінюються на дані функції `wrapper`. Щоб зберегти оригінальні метадані функції, у професійній розробці на `wrapper` навішують декоратор `@wraps(func)` зі стандартного модуля `functools`:

```python
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with args={args}, kwargs={kwargs} -> {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    """Додає два числа."""
    return a + b

print(add.__name__)  # Завдяки @wraps виведе 'add', а не 'wrapper'

```

---

## Корисні посилання

* [Офіційна документація Python: Functional Programming HOWTO (ітератори та генератори)](https://docs.python.org/3/howto/functional.html)
* [Офіційна документація Python: модуль `functools` та декоратор `wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)
* [Офіційна документація Python: магічні методи `__iter__`, `__next__`, `__call__`](https://docs.python.org/3/reference/datamodel.html#special-method-names)
