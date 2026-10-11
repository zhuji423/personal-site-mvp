---
title: "使用"
description: "Python 设计模式实现"
date: "2026-04-27"
category: "未分类"
source: "F:\\百度工作\\02_Agent_learn\\Agent_learn\\downloads_20260427_organized\\05_algorithm_backup\\ku_backup_20260427\\01_Python 设计模式实现.md"
---
Python 设计模式实现

根据具体场景选择最合适的模式，避免过度设计

## 1. 创建型模式
### 1.1 单例模式 (Singleton)
确保一个类只有一个实例，并提供一个全局访问点。

```
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 使用
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # 输出: True
```
**适用场景**：

* 数据库连接池管理
* 日志记录器
* 应用配置管理
* 线程池管理

```
# 数据库连接池管理
class DatabaseConnectionPool:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connections = []
            # 初始化连接池
            for _ in range(5):
                cls._instance.connections.append(f"DB-Connection-{_}")
        return cls._instance
    
    def get_connection(self):
        if self.connections:
            return self.connections.pop()
        raise Exception("No available connections")
    
    def release_connection(self, conn):
        self.connections.append(conn)

# 使用
pool1 = DatabaseConnectionPool()
pool2 = DatabaseConnectionPool()
print(pool1 is pool2)  # True

conn = pool1.get_connection()
print(conn)  # DB-Connection-4
pool1.release_connection(conn)
```
### 1.2 工厂模式 (Factory)
创建对象而不指定具体类。

```
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError("Unknown animal type")

# 使用
factory = AnimalFactory()
dog = factory.create_animal("dog")
print(dog.speak())  # 输出: Woof!
```
**适用场景**：

* 支付系统支持多种支付方式
* 跨平台UI组件创建
* 文档转换器(不同格式转换)
* 游戏中的角色创建

```
# 支付系统
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransfer(PaymentMethod):
    def pay(self, amount):
        print(f"Processing bank transfer of ${amount}")

class PaymentFactory:
    @staticmethod
    def create_payment(method_type):
        if method_type == "credit":
            return CreditCard()
        elif method_type == "paypal":
            return PayPal()
        elif method_type == "bank":
            return BankTransfer()
        raise ValueError("Invalid payment method")

# 使用
payment = PaymentFactory.create_payment("credit")
payment.pay(100)  # Processing credit card payment of $100
```
## 2. 结构型模式
### 2.1 适配器模式 (Adapter)
使不兼容接口的类能够一起工作。

```
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocket:
    def voltage(self):
        return 120

class Adapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return f"Adapted {self.socket.voltage()}V"

# 使用
euro_socket = EuropeanSocket()
adapter = Adapter(euro_socket)
print(adapter.voltage())  # 输出: Adapted 230V
```
**适用场景**：

* 集成第三方库/API
* 新旧系统兼容
* 数据格式转换
* 设备接口适配

```
# 新旧系统兼容 - 旧系统使用XML，新系统使用JSON
class OldSystem:
    def get_data(self):
        return "<data><value>123</value></data>"

class NewSystem:
    def process_json(self, json_data):
        print(f"Processing JSON: {json_data}")

class XMLToJSONAdapter:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def get_json_data(self):
        xml_data = self.old_system.get_data()
        # 简单转换逻辑(实际中可能使用xmltodict等库)
        json_data = {"value": xml_data.split("<value>")[1].split("</value>")[0]}
        return json_data

# 使用
old_system = OldSystem()
adapter = XMLToJSONAdapter(old_system)
new_system = NewSystem()
new_system.process_json(adapter.get_json_data())  # Processing JSON: {'value': '123'}
```
### 2.2 装饰器模式 (Decorator)
动态地给对象添加额外职责。

```
class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost() + 1

# 使用
simple_coffee = Coffee()
print(simple_coffee.cost())  # 5

milk_coffee = MilkDecorator(simple_coffee)
print(milk_coffee.cost())  # 7

sweet_milk_coffee = SugarDecorator(milk_coffee)
print(sweet_milk_coffee.cost())  # 8
```
**适用场景**：

* 动态添加日志功能
* 权限检查
* 数据验证
* 缓存功能
* 性能监控

```
# Web框架中的权限检查和日志记录
def login_required(func):
    def wrapper(*args, **kwargs):
        print("Checking user authentication...")
        # 实际中会检查session/cookie等
        print("User authenticated")
        result = func(*args, **kwargs)
        print("login_required decorator applied")
        return result

    return wrapper

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished executing {func.__name__}")
        return result
    return wrapper

@login_required
@log_execution
def transfer_money(amount, from_acc, to_acc):
    print(f"Transferring ${amount} from {from_acc} to {to_acc}")

# 使用
transfer_money(500, "ACC123", "ACC456")
# 输出:
# Checking user authentication...
# User authenticated
# Executing transfer_money with args: (500, 'ACC123', 'ACC456'), kwargs: {}
# Transferring $500 from ACC123 to ACC456
# Finished executing transfer_money
# login_required decorator applied
```
按下面的顺序执行的：

1. 进入 `login_required` 的 `wrapper`：

    * 打印："Checking user authentication..."
    * 打印："User authenticated"

2. 进入内部函数（已经被 `log_execution` 装饰过）：

    * 打印："Executing transfer_money with args: (500, 'ACC123', 'ACC456'), kwargs: {}"
    * 执行 `transfer_money` 的实际逻辑：
        * 打印："Transferring $500 from ACC123 to ACC456"

    * 打印："Finished executing transfer_money"

3. 回到 `login_required` 的 `wrapper`继续执行：

    * 打印："login_required decorator applied"

4. 函数结束，返回结果。

## 3. 行为型模式
### 3.1 观察者模式 (Observer)
定义对象间的一对多依赖关系，当一个对象状态改变时，所有依赖它的对象都会得到通知。

```
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)

class ConcreteSubject(Subject):
    def __init__(self, state):
        super().__init__()
        self._state = state
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class Observer:
    def update(self, subject):
        pass

class ConcreteObserver(Observer):
    def update(self, subject):
        print(f"Observer: Subject's state changed to {subject.state}")

# 使用
subject = ConcreteSubject("Initial state")
observer = ConcreteObserver()
subject.attach(observer)

subject.state = "New state"  # 输出: Observer: Subject's state changed to New state
```
**适用场景**：

* 事件通知系统
* 股票价格变动通知
* 社交媒体订阅
* 自动保存功能

```
# 股票价格变动通知系统
class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self._observers = []
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if self._price != value:
            self._price = value
            self._notify_observers()
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class Investor:
    def __init__(self, name):
        self.name = name
    
    def update(self, stock):
        print(f"{self.name}: {stock.symbol} price changed to {stock.price}")

# 使用
apple = Stock("AAPL", 150.0)
investor1 = Investor("John")
investor2 = Investor("Alice")

apple.attach(investor1)
apple.attach(investor2)

apple.price = 152.5
# 输出:
# John: AAPL price changed to 152.5
# Alice: AAPL price changed to 152.5
```
### 3.2 策略模式 (Strategy)
定义一系列算法，将它们封装起来，并使它们可以相互替换。

```
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal")

class ShoppingCart:
    def __init__(self):
        self._items = []
        self._payment_strategy = None
    
    def add_item(self, item):
        self._items.append(item)
    
    def set_payment_strategy(self, strategy):
        self._payment_strategy = strategy
    
    def checkout(self):
        total = sum(self._items)
        self._payment_strategy.pay(total)

# 使用
cart = ShoppingCart()
cart.add_item(100)
cart.add_item(200)
cart.set_payment_strategy(CreditCardPayment())
cart.checkout()  # 输出: Paying 300 using Credit Card
```
**适用场景**：

* 排序算法选择
* 压缩算法选择
* 导航路线计算
* 折扣计算策略

```
# 电商折扣策略
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, order_value):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, order_value):
        return order_value

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage
    
    def apply_discount(self, order_value):
        return order_value * (1 - self.percentage/100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount
    
    def apply_discount(self, order_value):
        return max(0, order_value - self.amount)

class Order:
    def __init__(self, items, discount_strategy=NoDiscount()):
        self.items = items
        self.discount_strategy = discount_strategy
    
    def total(self):
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        return self.discount_strategy.apply_discount(subtotal)

# 使用
items = [
    {'name': 'Book', 'price': 20, 'quantity': 2},
    {'name': 'Pen', 'price': 5, 'quantity': 10}
]

# 无折扣
order = Order(items)
print(order.total())  # 90.0

# 10%折扣
order = Order(items, PercentageDiscount(10))
print(order.total())  # 81.0

# 固定20元折扣
order = Order(items, FixedAmountDiscount(20))
print(order.total())  # 70.0
```
## 4. 其他常用模式
### 4.1 命令模式 (Command)
将请求封装为对象，从而允许参数化客户端。

```
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def on(self):
        print("Light is on")
    
    def off(self):
        print("Light is off")

class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light
    
    def execute(self):
        self._light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self._light = light
    
    def execute(self):
        self._light.off()

class RemoteControl:
    def __init__(self):
        self._command = None
    
    def set_command(self, command):
        self._command = command
    
    def press_button(self):
        self._command.execute()

# 使用
light = Light()
remote = RemoteControl()

remote.set_command(LightOnCommand(light))
remote.press_button()  # 输出: Light is on

remote.set_command(LightOffCommand(light))
remote.press_button()  # 输出: Light is off
```
**适用场景**：

* GUI按钮操作
* 事务系统
* 宏命令记录
* 撤销/重做功能

```
# 文本编辑器中的撤销/重做功能
class Document:
    def __init__(self):
        self.content = ""
    
    def insert_text(self, text, position):
        self.content = self.content[:position] + text + self.content[position:]
    
    def delete_text(self, start, end):
        deleted = self.content[start:end]
        self.content = self.content[:start] + self.content[end:]
        return deleted

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class InsertCommand(Command):
    def __init__(self, doc, text, position):
        self.doc = doc
        self.text = text
        self.position = position
    
    def execute(self):
        self.doc.insert_text(self.text, self.position)
    
    def undo(self):
        self.doc.delete_text(self.position, self.position + len(self.text))

class DeleteCommand(Command):
    def __init__(self, doc, start, end):
        self.doc = doc
        self.start = start
        self.end = end
        self.deleted = None
    
    def execute(self):
        self.deleted = self.doc.delete_text(self.start, self.end)
    
    def undo(self):
        if self.deleted:
            self.doc.insert_text(self.deleted, self.start)

class TextEditor:
    def __init__(self):
        self.doc = Document()
        self.history = []
        self.undo_stack = []
    
    def execute_command(self, command):
        command.execute()
        self.history.append(command)
    
    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
            self.undo_stack.append(command)

# 使用
editor = TextEditor()
editor.execute_command(InsertCommand(editor.doc, "Hello", 0))
print(editor.doc.content)  # Hello

editor.execute_command(InsertCommand(editor.doc, " World", 5))
print(editor.doc.content)  # Hello World

editor.undo()
print(editor.doc.content)  # Hello
```
### 4.2 状态模式 (State)
允许对象在其内部状态改变时改变其行为。

```
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def handle(self):
        print("Handling in State A")
        return ConcreteStateB()

class ConcreteStateB(State):
    def handle(self):
        print("Handling in State B")
        return ConcreteStateA()

class Context:
    def __init__(self):
        self._state = ConcreteStateA()
    
    def request(self):
        self._state = self._state.handle()

# 使用
context = Context()
context.request()  # Handling in State A
context.request()  # Handling in State B
context.request()  # Handling in State A
```
**适用场景**：

* 工作流系统
* 游戏角色状态
* 订单状态管理
* 网络连接状态

```
# 订单状态管理
class OrderState(ABC):
    @abstractmethod
    def next(self, order):
        pass
    
    @abstractmethod
    def prev(self, order):
        pass
    
    @abstractmethod
    def status(self):
        pass

class NewOrder(OrderState):
    def next(self, order):
        order.state = ProcessingOrder()
    
    def prev(self, order):
        print("Cannot go back from New order")
    
    def status(self):
        return "New"

class ProcessingOrder(OrderState):
    def next(self, order):
        order.state = ShippedOrder()
    
    def prev(self, order):
        order.state = NewOrder()
    
    def status(self):
        return "Processing"

class ShippedOrder(OrderState):
    def next(self, order):
        order.state = DeliveredOrder()
    
    def prev(self, order):
        order.state = ProcessingOrder()
    
    def status(self):
        return "Shipped"

class DeliveredOrder(OrderState):
    def next(self, order):
        print("Order already delivered")
    
    def prev(self, order):
        order.state = ShippedOrder()
    
    def status(self):
        return "Delivered"

class Order:
    def __init__(self):
        self.state = NewOrder()
    
    def next_state(self):
        self.state.next(self)
    
    def prev_state(self):
        self.state.prev(self)
    
    def get_status(self):
        return self.state.status()

# 使用
order = Order()
print(order.get_status())  # New

order.next_state()
print(order.get_status())  # Processing

order.next_state()
print(order.get_status())  # Shipped

order.prev_state()
print(order.get_status())  # Processing

order.next_state()
order.next_state()
print(order.get_status())  # Delivered
```


总结：

* **创建型模式**为系统提供了创建对象的灵活性
* **结构型模式**将这些对象组织成合理的结构
* **行为型模式**定义了这些对象如何交互和协作

在实际项目中，这三类模式常常结合使用。例如：

* 使用**工厂方法**(创建型)创建对象
* 使用**装饰器模式**(结构型)动态添加功能
* 使用**观察者模式**(行为型)实现对象间通信
