from flask import render_template, Response, redirect, flash, request, url_for
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import sqlite3

@app.route('/')

@app.route('/index')
def index():
    return render_template('index.html', title = 'Code Guide')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/aboutus')
def aboutus():
    return render_template('about.html', title = 'Code Guide')

@app.route('/array')
@login_required
def array():
    return render_template('array.html', title = 'Code Guide')
@app.route('/stack')
@login_required
def stack():
    return render_template('stack.html', title = 'Code Guide')
@app.route('/queue')
@login_required
def queue():
    return render_template('queue.html', title = 'Code Guide')
@app.route('/linkedlist')
@login_required
def linkedlist():
    return render_template('linkedlist.html', title = 'Code Guide')
@app.route('/tree')
@login_required
def tree():
    return render_template('tree.html', title = 'Code Guide')
questionsll = [
{
"id": "1",
"question": "Which of the following sorting algorithms can be used to sort a random linked list with minimum time complexity?",
"answers": ["a) Merge Sort", "b) Insertion sort", "c) Quick sort"],
"correct": "a) Merge Sort"
},
{
"id": "2",
"question": "Which of the following points is/are true about Linked List data structure when it is compared with array",
"answers": ["a) Random access is not allowed in a typical implementation of Linked Lists", "b) The size of array has to be pre-decided, linked lists can change their size any time.", "c) Both of these"],
"correct": "c) Both of these"
},
{
"id": "3",
"question": "In the worst case, the number of comparisons needed to search a singly linked list of length n for a given element is",
"answers": ["a) n/2", "b) log n", "c) n"],
"correct": "c) n"
},
{
"id": "4",
"question": "What are the time complexities of finding 8th element from beginning and 8th element from end in a singly linked list? Let n be the number of nodes in linked list, you may assume that n > 8.",
"answers": ["a) O(1) and O(1)", "b) O(1) and O(n)", "c) O(n) and O(1)"],
"correct": "b) O(1) and O(n)"
},
{
"id": "5",
"question": "You are given pointers to first and last nodes of a singly linked list, which of the following operations are dependent on the length of the linked list?",
"answers": ["a) Add a new element at the end of the list", "b) Insert a new element as a first element", "c) Delete the last element of the list"],
"correct": "c) Delete the last element of the list"
}
]

questionsar = [
{
"id": "1",
"question": "Which of the following describes an array?",
"answers": ["a) Container of objects of similar types", "b) Data structure that shows a hierarchical behavior", "c) Arrays are immutable"],
"correct": "a) Container of objects of similar types"
},
{
"id": "2",
"question": "Assuming int is of 4bytes, what is the size of int arr[15];?",
"answers": ["a) 4", "b) 15", "c) 60"],
"correct": "c) 60"
},
{
"id": "3",
"question": "Elements in an array are accessed",
"answers": ["a) sequentially", "b) exponentially", "c) randomly"],
"correct": "c) randomly"
},
{
"id": "4",
"question": "A program P reads in 500 integers in the range [0..100] exepresenting the scores of 500 students. It then prints the frequency of each score above 50. What would be the best way for P to store the frequencies?",
"answers": ["a) An array of 500 numbers", "b) An array of 50 numbers", "c) A dynamically allocated array of 550 numbers"],
"correct": "b) An array of 50 numbers"
},
{
"id": "5",
"question": "Which of the following operations is not O(1) for an array of sorted data. You may assume that array elements are distinct.",
"answers": ["a) Find the ith largest element", "b) Delete an element", "c) Both of these"],
"correct": "b) Delete an element"
}
]

questionsst = [
{
"id": "1",
"question": "Which one of the following is an application of Stack Data Structure?",
"answers": ["a) Arithmetic expression evaluation", "b) Managing function calls", "c) Both"],
"correct": "c) Both"
},
{
"id": "2",
"question": "Which data structure can be used in infix to postfix conversion",
"answers": ["a) Array", "b) Queue", "c) Stack"],
"correct": "c) Stack"
},
{
"id": "3",
"question": "Which of the following is true about linked list implementation of stack?",
"answers": ["a) In push operation, if new nodes are inserted at the beginning of linked list, then in pop operation, nodes must be removed from end.", "b) In push operation, if new nodes are inserted at the end, then in pop operation, nodes must be removed from the beginning.", "c) None"],
"correct": "c) None"
},
{
"id": "4",
"question": "Assume that the operators +, -, × are left associative and ^ is right associative. The order of precedence (from highest to lowest) is ^, x , +, -. The postfix expression corresponding to the infix expression a + b × c - d ^ e ^ f is",
"answers": ["a) abc × + de ^ f ^ -", "b) abc × + def ^ ^ -", "c) ab + c × d - e ^ f ^"],
"correct": "b) abc × + def ^ ^ -"
},
{
"id": "5",
"question": "To evaluate an expression without any embedded function calls:",
"answers": ["a) As many stacks as the height of the expression tree are needed", "b) Two stacks are needed", "c) One stack is enough"],
"correct": "c) One stack is enough"
}
]

questionstr = [
    {
        "id": "1",
        "question": "Which of the following is a true about Binary Trees",
        "answers": ["a) Every complete binary tree is also a full binary tree.", "b) Every full binary tree is also a complete binary tree.", "c) None of the above"],
        "correct": "c) None of the above"
    },
    {
        "id": "2",
        "question": "The maximum number of binary trees that can be formed with three unlabeled nodes is:",
        "answers": ["a) 5", "b) 3", "c) 1"],
        "correct": "a) 5"
    },
    {
        "id": "3",
        "question": "The number of leaf nodes in a rooted tree of n nodes, with each node having 0 or 3 children is:",
        "answers": ["a) n / 2", "b) (n - 1) / 2", "c) (2n + 1) / 3"],
        "correct": "c) (2n + 1) / 3"
    },
    {
        "id": "4",
        "question": "What is common in three different types of traversals (Inorder, Preorder and Postorder)?",
        "answers": ["a) Root is visited before right subtree", "b) Left subtree is always visited before right subtree", "c) Root is visited after left subtree"],
        "correct": "b) Left subtree is always visited before right subtree"
    },
    {
        "id": "5",
        "question": "Which of the following pairs of traversals is not sufficient to build a binary tree from the given traversals?",
        "answers": ["a) Preorder and Postorder", "b) Inorder and Postorder", "c) Preorder and Inorder"],
        "correct": "a) Preorder and Postorder"
    }
]

questionsqu = [
    {
        "id": "1",
        "question": "How many stacks are needed to implement a queue. Consider the situation where no other data structure like arrays, linked list is available to you.",
        "answers": ["a) 1", "b) 2", "c) 3"],
        "correct": "b) 2"
    },
    {
        "id": "2",
        "question": "Which of the following is true about linked list implementation of queue?",
        "answers": ["a) In push operation, if new nodes are inserted at the beginning of linked list, then in pop operation, nodes must be removed from end.", "b) In push operation, if new nodes are inserted at the end, then in pop operation, nodes must be removed from the beginning.", "c) Both of the above"],
        "correct": "c) Both of the above"
    },
    {
        "id": "3",
        "question": "How many queues are needed to implement a stack. Consider the situation where no other data structure like arrays, linked list is available to you.",
        "answers": ["a) 1", "b) 2", "c) 3"],
        "correct": "b) 2"
    },
    {
        "id": "4",
        "question": "Suppose a circular queue of capacity (n – 1) elements is implemented with an array of n elements. Assume that the insertion and deletion operation are carried out using REAR and FRONT as array index variables, respectively. Initially, REAR = FRONT = 0. The conditions to detect queue full and queue empty are",
        "answers": ["a) Full: (REAR+1) mod n == FRONT, empty: REAR == FRONT", "b) Full: REAR == FRONT, empty: (REAR+1) mod n == FRONT", "c) Full: (FRONT+1) mod n == REAR, empty: REAR == FRONT"],
        "correct": "a) Full: (REAR+1) mod n == FRONT, empty: REAR == FRONT"
    },
    {
        "id": "5",
        "question": "A Priority-Queue is implemented as a Max-Heap. Initially, it has 5 elements. The level-order traversal of the heap is given below: 10, 8, 5, 3, 2 Two new elements '1' and '7' are inserted in the heap in that order. The level-order traversal of the heap after the insertion of the elements is:",
        "answers": ["a) 10, 8, 7, 5, 3, 2, 1", "b) 10, 8, 7, 3, 2, 1, 5", "c) 10, 8, 7, 1, 2, 3, 5"],
        "correct": "b) 10, 8, 7, 3, 2, 1, 5"
    }
]

@app.route('/quizLL',  methods=['GET', 'POST'])
@login_required
def quizll():
    if request.method == 'GET':
        return render_template("quizll.html", data=questionsll)
    else:
        result = 0
        total = 0
        for question in questionsll:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        current_user.quiz1 = result 
        db.session.commit()
        return render_template('resultll.html', total=total, result=result)

@app.route('/quizAr',  methods=['GET', 'POST'])
def quizar():
    if request.method == 'GET':
        return render_template("quizar.html", data=questionsar)
    else:
        result = 0
        total = 0
        for question in questionsar:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        current_user.quizAr = result 
        db.session.commit()
        return render_template('resultar.html', total=total, result=result)

@app.route('/quizSt',  methods=['GET', 'POST'])
def quizst():
    if request.method == 'GET':
        return render_template("quizst.html", data=questionsst)
    else:
        result = 0
        total = 0
        for question in questionsst:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        current_user.quizSt = result 
        db.session.commit()
        return render_template('resultst.html', total=total, result=result)
@app.route('/quizTr',  methods=['GET', 'POST'])
@login_required
def quiztr():
    if request.method == 'GET':
        return render_template("quiztr.html", data=questionstr)
    else:
        result = 0
        total = 0
        for question in questionstr:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        current_user.quizTr = result 
        db.session.commit()
        return render_template('resulttr.html', total=total, result=result)

@app.route('/quizQu',  methods=['GET', 'POST'])
@login_required
def quizqu():
    if request.method == 'GET':
        return render_template("quizqu.html", data=questionsqu)
    else:
        result = 0
        total = 0
        for question in questionsqu:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        current_user.quizQu = result 
        db.session.commit()
        return render_template('resultqu.html', total=total, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
