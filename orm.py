import MySQLdb
import MySQLdb.cursors


class AbstractModel:

    def get_fields(self):
        fields = []
        for field in self.__dir__():
            attr = getattr(self.__class__, field)
            if isinstance(attr, Field):
                fields.append(field)
        return fields

    def save(self):
        insert(self)


class Field:
    def __init__(self, length=255):
        super().__init__()
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


def get_connection():
    connection = MySQLdb.connect(user='root',
                                 passwd='3926',
                                 db='first',
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def migrate(cls):
    associate_dict = {
        'IntField': 'INT',
        'CharField': 'VARCHAR',
        'FloatField': 'FLOAT',
        'Boolean': 'BOOL',
    }
    connection = get_connection()
    cursor = connection.cursor()
    table = "CREATE TABLE IF NOT EXISTS {0}".format(cls.__class__.__name__).lower()
    rows = ""

    for row in cls.__dir__():
        attr = getattr(cls, row)
        if isinstance(attr, Field):
            type_data = associate_dict[attr.__class__.__name__]
            value = getattr(attr, 'length')
            rows += row + " " + type_data + "({})".format(
                value) + ","
    rows = "(id INT AUTO_INCREMENT PRIMARY KEY," + rows[:len(rows) - 1] + ")"
    cursor.execute(table + rows)


def select(model_class, **kwargs):
    connection = get_connection()
    cursor = connection.cursor()
    name = model_class.__name__.lower() + " "
    where = ""
    associated_dict = {
        '__gt': ' > ',
        '__gte': ' >= ',
        '__lt': ' < ',
        '__lte': ' <= '
    }
    if kwargs:
        q = "SELECT "
        # fields = ""
        for key, value in kwargs.items():
            if "__" in key:
                operator = associated_dict[key[key.find("_"):]]
                key = key[:key.find("_")]
            else:
                operator = " = "
            where += key + "{}" "'{}'" .format(operator, value) + " AND "
            # fields += select_id + ", "
        where = where[:len(where) - 4]
        # fields = fields[:len(fields) - 2]
        q += "*" + " FROM " + name + "WHERE " + where
    else:
        q = "SELECT * FROM %s" % name
    cursor.execute(q)

    return cursor.fetchall()


def insert(instance):
    connection = get_connection()
    cursor = connection.cursor()
    name = instance.__class__.__name__.lower()
    values = ''
    command = "INSERT INTO %s " % name
    str_fields = ""
    fields = instance.get_fields()

    for attr in fields:
        str_fields += " " + attr + ","
        value = getattr(instance, attr)
        values += " " + "'%s'," % value
    str_fields = "(" + str_fields[1:len(str_fields) - 1] + ")"
    values = "(" + values[1:len(values) - 1] + ")"
    command += str_fields + " VALUES " + values
    cursor.execute(command)
    connection.commit()
