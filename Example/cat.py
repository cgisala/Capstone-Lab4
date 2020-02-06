from peewee import * 

# Which database?
db = SqliteDatabase('cats.sqlite')

# Create a Model class. This defines both the fields in the objects in your program
# and also the columns in the database.  Peewee maps between the two.

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    # Link this model to a particular database
    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is a {self.color} cat and is {self.age} years old'

    
# Connect to DB,, and create tables that map to the model Cat.
# Can have many models, create_tables takes a list of model classes as the argument
db.connect()
db.create_tables([Cat])

# Create Cat objects and call save function to insert them into the database
print('\nCreate and save 3 cats')

zoe = Cat(name="Zoe", color='Ginger', age=3)
zoe.save()

holly = Cat(name="Holly", color='Tabby', age=7)
holly.save()

fluffy = Cat(name="Fluffy", color='Black', age=1)
fluffy.save()

print('\nFind all cats')

cats = Cat.select()

for cat in cats:
    print(cat)




