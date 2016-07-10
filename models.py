from orm import *


class Users(AbstractModel):
    username = CharField(length=20)
    password = IntField()
    city = CharField(length=30)
    age = IntField()


class Cars(AbstractModel):
    mark = CharField(length=20)
    model = CharField(length=20)
    engine_type = CharField(length=20)
    color = CharField(length=20)
    since = CharField(length=20)


class PhotoCamera(AbstractModel):
    mark = CharField(length=20)
    model = CharField(length=20)
    battery = CharField(length=20)
    matrix_type = CharField(length=20)
    frame_speed = CharField(length=20)
    since = CharField(length=20)
    flash_cards = IntField()


migrate(Users())
migrate(Cars())
migrate(PhotoCamera())

bob = Users()
bob.username = "Bob"
bob.age = 21
bob.password = 589436
bob.city = "London"

second_car = Cars()
second_car.mark = "Mercedes"
second_car.model = "E230"
second_car.engine_type = "Benzine"
second_car.color = "Black"
second_car.since = "2008"

second_camera = PhotoCamera()
second_camera.mark = "Canon"
second_camera.model = "5D Mark II"
second_camera.battery = "Li-ion"
second_camera.frame_speed = "6 frames per second"
second_camera.matrix_type = "Full frame"
second_camera.flash_cards = 2
second_camera.since = "2013"

bob.save()
second_car.save()
second_camera.save()

print(select(Users, age__gt=22))
