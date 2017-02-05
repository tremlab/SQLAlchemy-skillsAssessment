"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# brand object -  an object instantiated on the class "Brand"



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An 'association' table helps to artificially create the impossible
# 'many-to-many' relationship in a relational database. It is distinguished
# from a 'middle' table in that an association table has no other purpose 
# or data beyond enabling the cross-reference of two other tables.



# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "Brand.query.get('ram')"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "Model.query.filter(Model.name =='Corvette', Model.brand_id =='che').all()"

# Get all models that are older than 1960.
q3 = "Model.query.filter(Model.year < 1960).all()"

# Get all brands that were founded after 1920.
q4 = "Brand.query.filter(Brand.founded > 1920).all()"

# Get all models with names that begin with "Cor."
q5 = "Model.query.filter(Model.name.like('Cor%')).all()"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "Brand.query.filter( (Brand.founded < 1950) | (Brand.discontinued != None) ).all()"

# Get any model whose brand_id is not "for."
q8 = "Model.query.filter(Model.brand_id != 'for').all()"



# -------------------------------------------------------------------
# Part 4: Write Functions

def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = db.session.query(Model.name,
                              Model.year,
                              Brand.name,
                              Brand.headquarters).join(Brand).all()

    print "Models for the year:", year

    for model, mod_year, brand, hq in models:
        if mod_year == year:
            print "Model: %s, Brand: %s, HQ: %s" % (model, brand, hq)


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    models = db.session.query(Model.name,
                              Model.year,
                              Brand.name).join(Brand).all()

    brand_summary = {}

    # breakout data by brand into a dictionary
    # "print each brand name (once)"
    for model, mod_year, brand in models:
        if brand in brand_summary:
            brand_summary[brand].append((model, mod_year))
        else:
            brand_summary[brand] = [(model, mod_year)]

    # print all data, grouped by brand
    for brand, models in brand_summary.items():
        print brand
        for model in models:
            print "\t%s, %i" % (model[0], model[1])


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brands = Brand.query.filter(Brand.name.like('%mystr%')).all()

    return brands


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

    return models
