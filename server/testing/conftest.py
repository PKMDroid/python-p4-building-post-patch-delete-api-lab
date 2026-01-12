import pytest
from app import app, db
from models import Bakery, BakedGood


@pytest.fixture(autouse=True)
def setup_database():
    """Set up test database before each test and tear down after."""
    with app.app_context():
      
        db.create_all()
        
        BakedGood.query.delete()
        Bakery.query.delete()
        
        bakery1 = Bakery(id=1, name="Delightful Donuts")
        bakery2 = Bakery(id=2, name="Bagel Heaven")
        
        db.session.add_all([bakery1, bakery2])
        db.session.commit()
        
        baked_goods = [
            BakedGood(name="Apple Fritter", price=3, bakery_id=bakery1.id),
            BakedGood(name="Chocolate Donut", price=2, bakery_id=bakery1.id),
        ]
        
        db.session.add_all(baked_goods)
        db.session.commit()
        
        yield 
        
        db.session.remove()
        db.drop_all()