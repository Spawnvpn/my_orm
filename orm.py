import MySQLdb
import MySQLdb.cursors


class AbstractModel:
    def save(self):
        print(self.__class__.__name__)
        """
        Передаем сюда инстанс класса наследника, определяем класс инстанса,
        определяем поля класса (таблицы/атрибуты), затем запись этого в базу
        """


class Field:
    def __init__(self, length=255):
        super().__init__()
        self.length = length

    def __get__(self, obj, objtype):
        print('Получаю', self.length)
        return self.length

    def __set__(self, type_field, length):
        print('Обновляю', length)
        self.type_field = type_field
        self.length = length


class IntField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CharField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FloatField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Boolean(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Users(AbstractModel):
    username = CharField(length=20)
    password = IntField()
    city = CharField(length=30)


def get_connection():
    connection = MySQLdb.connect(user='root',
                                 passwd='3926',
                                 db='books',
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def in_dict(cls, row):
    try:
        cls.__class__.__dict__[row]
        return True
    except KeyError:
        return False


def migrate(cls):
    associate_dict = {
        'IntField': 'INT',
        'CharField': 'VARCHAR',
        'FloatField': 'FLOAT',
        'Boolean': 'BOOL',
    }
    print(cls.__class__.__dict__)
    connection = get_connection()
    cursor = connection.cursor()
    table = "CREATE TABLE IF NOT EXISTS {0}".format(cls.__class__.__name__).lower()
    rows = ""
    for row in cls.__dir__():
        if not row.startswith("__") and in_dict(cls, row):
            type_data = associate_dict[cls.__class__.__dict__[row].__class__.__name__]
            value = cls.__class__.__dict__[row].__dict__
            rows += row + " " + type_data + "({})".format(
                value['length']) + ","
    rows = "(" + rows + "id INT AUTO_INCREMENT PRIMARY KEY)"
    print(rows)
    cursor.execute(table + rows + ";")


def select():
    pass


def insert():
    pass

migrate(Users())
petya = Users()
petya.username = "Petya"
petya.password = "123456"
petya.city = "London"
petya.save()


"""
azaz = getattr(cls, row)
if isnstance(azaz):
"""