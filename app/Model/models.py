from app import db

# drinkIngredients = db.Table('drinkIngredients',
#     db.Column('recipe_id', db.ForeignKey('recipe.id')),
#     db.Column('ingredient_id', db.ForeignKey('ingredient.id'))
# )

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    spirit = db.Colum(db.String(50))
    spirit_measurement = db.Column(db.Double)
    ingredients = db.relationship('Ingredient', back_populates='drink')
    garnish = db.relationship('Garnish', back_populates='garnishedDrinks')
    glass = db.Column(db.String(50))

    def __repr__(self):
        return '<Recipe {}: {} made with {}oz {}>'.format(self.id,self.name,self.spirit_measurement,self.spirit)

class Spirit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colum(db.String(50), unique=True)
    drinks = db.Relationship('Recipe')

    def __repr__(self):
        return '<Mixer {} - {}>'.format(self.id,self.name)

class Mixer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colum(db.String(50), unique=True)
    drinks = db.Relationship('Recipe')

    def __repr__(self):
        return '<Mixer {} - {}>'.format(self.id,self.name)

class Ingredient(db.Model):
    mixerid = db.Column(db.Integer, db.ForeignKey('mixer.id'), primary_key=True)
    drinkid = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    measurement = db.Column(db.Double)
    mixer = db.Relationship('Mixer')
    drink = db.Relationship('Recipe')

    def __repr__(self):
        return '<Ingredient: {} ({} oz) in {}>'.format(self.mixer,self.measurement, self.drink)

class Garnish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    garnishedDrinks = db.relationship('Recipe')
    def __repr__(self):
        return '<Garnish {} - {}>'.format(self.id,self.name)

