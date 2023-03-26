#from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
#from sqlalchemy.orm import relationship
#from sqlalchemy.ext.declarative import declarative_base
#
#Base = declarative_base()
#
#class User(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True)
#    username = Column(String(50), nullable=False)
#    is_quiz_admin = Column(Boolean, default=False)
#    quizzes = relationship('Quiz', back_populates='creator')
#    answers = relationship('Answer', back_populates='user')
#
#class Quiz(Base):
#    __tablename__ = 'quizzes'
#    id = Column(Integer, primary_key=True)
#    name = Column(String(50), nullable=False)
#    category = Column(String(50))
#    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#    creator = relationship('User', back_populates='quizzes')
#    questions = relationship('Question', back_populates='quiz')
#    answers = relationship('Answer', back_populates='quiz')

#class Question(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    text = db.Column(db.String(255), nullable=False)
#    option1 = db.Column(db.String(255), nullable=False)
#    option2 = db.Column(db.String(255), nullable=False)
#    option3 = db.Column(db.String(255), nullable=False)
#    option4 = db.Column(db.String(255), nullable=False)
#    answer = db.Column(db.String(255), nullable=False)