from flask import flash, redirect, render_template, url_for
from flask_quiz import app
from flask_quiz.forms import LoginForm, RegistrationForm
#from flask_quiz.models import Post, Question, User

# question1 = Question(text='What is the capital of France?',
#                     option1='Berlin',
#                     option2='London',
#                     option3='Paris',
#                     option4='Rome',
#                     answer='Paris')
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


@app.route('/')
def start():
    return render_template('start.html')


@app.route('/home')
def home():
    return render_template('home.html')


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
    # flash('You have been logged out!', 'success')
    return render_template('start.html', title='start')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    #    if request.method == 'POST':
    #        # Evaluate quiz and show results
    #        questions = Question.query.all()
    #        score = 0
    #        total = 0
    #        for question in questions:
    #            total += 1
    #            selected_options = request.form.getlist(str(question.id))
    #            selected_answer = ','.join(selected_options)
    #            if selected_answer == question.answer:
    #                score += 1
    #        return render_template('results.html', score=score, total=total)
    #    else:
    #        # Show quiz questions
    #        questions = Question.query.all()
    return render_template('quiz.html')


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
