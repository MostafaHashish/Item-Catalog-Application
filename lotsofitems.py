from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut to update database
engine = create_engine("postgresql://catalog:topsecret@localhost/catalogdb")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Test Name", email="test22@gmail.com")
session.add(User1)
session.commit()

# Create category of Premier League
category1 = Categories(user_id=1, name="Premier League")
session.add(category1)
session.commit()


# Create category of La Liga
category2 = Categories(user_id=1, name="La Liga")
session.add(category2)
session.commit()

# Create category of Seria A
category3 = Categories(user_id=1, name="Seria A")
session.add(category3)
session.commit()

# Create category of Bundesliga
category4 = Categories(user_id=1, name="Bundesliga")
session.add(category4)
session.commit()

# Create category of Ligue 1
category5 = Categories(user_id=1, name="Ligue 1")
session.add(category5)
session.commit()

# Create category of Eredivisie
category6 = Categories(user_id=1, name="Eredivisie")
session.add(category6)
session.commit()

# Create category of Primeira Liga
category7 = Categories(user_id=1, name="Primeira Liga")
session.add(category7)
session.commit()



# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="Porto",
                             description="Futebol Clube do Porto,\
                              MHIH, OM, commonly known as FC Porto or simply Porto,\
                              is a Portuguese sports club based in Porto.",
                             categories=category7)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Bayern Munich",
                             description=" commonly known as FC Bayern München,\
                                is a German sports club based in Munich, Bavaria.\
                                Bayern is historically the most successful team in German football.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Juventus",
                             description="colloquially known as Juve, \
                                is a professional Italian football club in Turin, Piedmont.\
                                Italy's most successful club of the 20th century.",
                             categories=category3)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Paris Saint-Germain",
                             description="commonly known as PSG\
                               Today the city's largest club by far.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Ajax",
                             description=" is a Dutch professional football club based in Amsterdam.",
                             categories=category6)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Liverpool",
                             description="is a professional football club in Liverpool, England\
                             The club's anthem is 'You'll Never Walk Alone'.",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Real Madrid",
                             description="Bayern is historically the most successful team in Europe.",
                             categories=category2)
session.add(categoryItem1)
session.commit()


print "added category items!"
