from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dbda4145ffad045622e6f11a0b1f2e1f'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://stud_v23_ssa171:flaskappquiz23@kark.uit.no/stud_v23_ssa171'
# db = SQLAlchemy(app)

quiz_liste = [
    {
        'author': 'Frank Smith',
        'title': 'Quiz 1',
        'content': 'First Quiz content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Quiz 2',
        'content': 'Second Quiz content',
        'date_posted': 'April 21, 2018'
    }
]


# class Question(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    text = db.Column(db.String(255), nullable=False)
#    option1 = db.Column(db.String(255), nullable=False)
#    option2 = db.Column(db.String(255), nullable=False)
#    option3 = db.Column(db.String(255), nullable=False)
#    option4 = db.Column(db.String(255), nullable=False)
#    answer = db.Column(db.String(255), nullable=False)
#
#
# class User(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(20), unique=True, nullable=False)
#    password = db.Column(db.String(60), nullable=False)


# db.create_all()
# User accounts
# users = {'user': 'password', 'admin': 'password'}
# is_user = User(id=1, username='user', password='userpassword')
# is_admin = User(id=2, username='admin', password='adminpassword')
# db.session.add_all([is_user, is_admin])

# question1 = Question(text='What is the capital of France?',
#                     option1='Berlin',
#                     option2='London',
#                     option3='Paris',
#                     option4='Rome',
#                     answer='Paris')
#
# question2 = Question(text='Which planet is closest to the sun?',
#                     option1='Earth',
#                     option2='Mars',
#                     option3='Mercury',
#                     option4='Jupiter',
#                     answer='Mercury')

# question3 = Question(text='What is the largest organ in the human body?',
#                     option1='Brain',
#                     option2='Liver',
#                     option3='Heart',
#                     option4='Skin',
#                     answer='Skin')

# question4 = Question(text='Which famous physicist developed the theory of general relativity?',
#                     option1='Albert Einstein',
#                     option2='Isaac Newton',
#                     option3='Stephen Hawking',
#                     option4='Galileo Galilei',
#                     answer='Albert Einstein')

# question5 = Question(text='What is the highest mountain in the world?',
#                     option1='Mount Kilimanjaro',
#                     option2='Mount Everest',
#                     option3='Mount Fuji',
#                     option4='Mount McKinley',
#                     answer='Mount Everest')


# db.session.add_all([question1, question2, question3, question4, question5])
# db.session.commit()


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/home')
def home():
    return render_template('home.html', quiz_liste=quiz_liste)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('start'))
    return render_template('register.html', title='Register', form=form)


@app.route("/logout")
def logout():
    #flash('You have been logged out!', 'success')
    return render_template('start.html', title='start')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Evaluate quiz and show results
        questions = Question.query.all()
        score = 0
        total = 0
        for question in questions:
            total += 1
            selected_options = request.form.getlist(str(question.id))
            selected_answer = ','.join(selected_options)
            if selected_answer == question.answer:
                score += 1
        return render_template('results.html', score=score, total=total)
    else:
        # Show quiz questions
        questions = Question.query.all()
        return render_template('quiz.html', questions=questions)


@app.route('/quiz_list')
def quiz_list():
    return render_template('quiz_list.html')


@app.route('/quiz/question')
def quiz_question():
    return render_template('quiz_question.html')


@app.route('/quiz/results')
def quiz_results():
    return render_template('quiz_results.html')


@app.route('/admin/')
def admin_home():
    return render_template('admin_home.html')


@app.route('/admin/quiz/new')
def admin_quiz_new():
    return render_template('admin_quiz_new.html')


@app.route('/admin/quiz/edit')
def admin_quiz_edit():
    return render_template('admin_quiz_edit.html')


@app.route('/admin/quiz/delete')
def admin_quiz_delete():
    return render_template('admin_quiz_delete.html')


if __name__ == '__main__':
    app.run(debug=True)
