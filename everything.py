#from flask import render_template, redirect, url_for
#from flask_login import login_required, current_user
#from app import app, db
#from app.models import User, Quiz, Question, Answer

# Routes for all users
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#@app.route('/quiz_list')
#@login_required
#def quiz_list():
#    quizzes = Quiz.query.all()
#    return render_template('quiz_list.html', quizzes=quizzes)
#
#@app.route('/quiz/<int:quiz_id>/question/<int:question_id>', methods=['GET', 'POST'])
#@login_required
#def quiz_question(quiz_id, question_id):
#    quiz = Quiz.query.get(quiz_id)
#    question = Question.query.get(question_id)
#    if request.method == 'POST':
#        answer = Answer(user_id=current_user.id, question_id=question.id, selected_answer=request.form['answer'])
#        db.session.add(answer)
#        db.session.commit()
#        flash('Your answer has been submitted.')
#        next_question = quiz.next_question(question)
#        if next_question:
#            return redirect(url_for('quiz_question', quiz_id=quiz.id, question_id=next_question.id))
#        else:
#            return redirect(url_for('quiz_results', quiz_id=quiz.id))
#    return render_template('quiz_question.html', quiz=quiz, question=question)
#
#@app.route('/quiz/<int:quiz_id>/results')
#@login_required
#def quiz_results(quiz_id):
#    quiz = Quiz.query.get(quiz_id)
#    questions = quiz.questions
#    total_score = 0
#    for question in questions:
#        correct_answer = question.correct_answer()
#        user_answer = question.user_answer(current_user)
#        if user_answer == correct_answer:
#            total_score += 1
#    return render_template('quiz_results.html', quiz=quiz, questions=questions, total_score=total_score)
#
## Routes for admin users
#@app.route('/admin/')
#@login_required
#def admin_index():
#    return render_template('admin_index.html')
#
#@app.route('/admin/quiz_list')
#@login_required
#def admin_quiz_list():
#    quizzes = Quiz.query.all()
#    return render_template('admin_quiz_list.html', quizzes=quizzes)
#
#@app.route('/admin/quiz/new', methods=['GET', 'POST'])
#@login_required
#def admin_quiz_new():
#    if request.method == 'POST':
#        quiz = Quiz(title=request.form['title'], description=request.form['description'])
#        db.session.add(quiz)
#        db.session.commit()
#        flash('Quiz created.')
#        return redirect(url_for('admin_quiz_edit', quiz_id=quiz.id))
#    return render_template('admin_quiz_new.html')
#
#@app.route('/admin/quiz/<int:quiz_id>/edit', methods=['GET', 'POST'])
#@login_required
#def admin_quiz_edit(quiz_id):
#    quiz = Quiz.query.get(quiz_id)
#    if request.method == 'POST':
#        quiz.title = request.form['title']
#        quiz.description = request.form['description']
#        db.session.commit()
#        flash('Quiz updated.')
#        return redirect(url_for('admin_quiz_edit', quiz_id=quiz.id))
#    return render_template('admin_quiz_edit.html', quiz=quiz)
#
#@app.route('/admin/quiz/<int:quiz_id>/delete', methods=['POST'])
#@login_required
#def admin_quiz_delete(quiz_id):
#    quiz = Quiz.query.get(quiz_id)
#    db.session.delete(quiz)
#    db.session.commit()
#    flash('Quiz deleted.')
#    return redirect(url_for('admin_quiz_list'))
#