from orm import *


class Users(AbstractModel):
    username = CharField(length=20)
    password = IntField()
    city = CharField(length=30)
    age = IntField


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
bob.password = 5664586
bob.city = "London"

first_car = Cars()
first_car.mark = "BMW"
first_car.model = "M650"
first_car.engine_type = "Benzine"
first_car.color = "White"
first_car.since = "2016"

first_camera = PhotoCamera()
first_camera.mark = "Nikon"
first_camera.model = "D4"
first_camera.battery = "Li-ion"
first_camera.frame_speed = "8 frames per second"
first_camera.matrix_type = "Full frame"
first_camera.flash_cards = "2"
first_camera.since = "2014"

bob.save()
first_car.save()
first_camera.save()