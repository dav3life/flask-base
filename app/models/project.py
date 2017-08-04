
from .. import db
from datetime import datetime
import enum

class Project_Access(enum.Enum):
    Public = 0
    Private = 1

class Task_Urgency(enum.Enum):
    Minimal = 0 # 1-7 days
    Low = 1 # 8-24 hrs
    Medium = 2 # 1-8 hrs
    High = 3 # 15-60 min
    Very_High = 4 # 5 to 15 min
    Maximal = 5 # Up to 5 min

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(140), nullable=False)

    access = db.Column(db.Enum(Project_Access), default=Project_Access.Public)
    project_deadline = db.Column(db.DateTime, nullable=False,
                                 default=datetime.max) # default is no deadline
    task_urgency = db.Column(db.Enum(Task_Urgency), nullable=False)
    task_reward = db.Column(db.Numeric, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    def __repr__(self):
        return '<Role \'%s\'>' % self.name

