from flask import Flask, render_template, request, session, redirect, url_for
from random import sample
from questions import questions

app = Flask(__name__)
app.secret_key = 'Shruti'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    quiz_questions = sample(questions, 10)
    session['quiz_questions'] = quiz_questions  
    session['answers'] = {}  
    return redirect(url_for('question', qnum=0))

@app.route('/question/<int:qnum>', methods=['GET', 'POST'])
def question(qnum):
    quiz_questions = session.get('quiz_questions', [])
    if not quiz_questions or qnum < 0 or qnum >= len(quiz_questions):
        return redirect(url_for('quiz')) 
    
    if request.method == 'POST':
        selected = request.form.get('answer')
        answers = session.get('answers', {})
        answers[str(qnum)] = selected
        session['answers'] = answers

        next_qnum = qnum + 1
        if next_qnum >= len(quiz_questions):
            return redirect(url_for('result'))
        else:
            return redirect(url_for('question', qnum=next_qnum))
    
    question_data = quiz_questions[qnum]
    answers = session.get('answers', {})
    selected_answer = answers.get(str(qnum))

    return render_template('question.html',
                           question=question_data,
                           qnum=qnum,
                           total=len(quiz_questions),
                           answers=answers)

@app.route('/result')
def result():
    quiz_questions = session.get('quiz_questions', [])
    answers = session.get('answers', {})
    score = 0
    results = []

    for idx, q in enumerate(quiz_questions):
        q_text = q["question"]
        selected = answers.get(str(idx))
        correct = q["answer"]
        is_correct = selected == correct
        if is_correct:
            score += 1
        results.append({
            "question": q_text,
            "selected": selected if selected else "Not answered",
            "correct": correct,
            "is_correct": is_correct,
            "chapter": q.get("chapter", "Not Available"),
            "explanation": q.get("explanation", "Explanation not provided.")
        })

    return render_template('result.html', score=score, total=len(quiz_questions), results=results)

if __name__ == '__main__':
    app.run(debug=True)
