from ideabox_app import db
from models import IdeaPost

# create the db and db tables
db.create_all()

# insert
db.session.add(IdeaPost("Jump out of the earth","You can walk straight into the end of the world,or fall in to the pacific and swim to enternity that sounds like a a great idea to me."))


# commit the changes
db.session.commit()