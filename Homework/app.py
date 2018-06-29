from flask import *
from mongoengine import *
from Models.service import Service
from Models.user import User
from Models.order import Order
import mlab

app = Flask(__name__)

app.secret_key = "A super secret key"

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')
    if "loggedin" in session:
        if request.method == "GET":
            users = User.objects()
            return redirect(url_for("service_page"))
    else:
        return redirect(url_for("login"))

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"

@app.route('/remove-all')
def remove_all():
    all_service = Service.objects()
    all_service.delete()
    return redirect(url_for('admin'))

@app.route('/service-page')
def service_page():
    all_service = Service.objects()
    return render_template('service-page.html',all_service = all_service)


@app.route('/detail/<service_id>')
def detail(service_id):
    all_service = Service.objects.with_id(service_id)
    return redirect(url_for('searchid',id=service_id))

@app.route('/<id>')
def searchid(id):
    all_service = Service.objects(id=id)
    return render_template('searchid.html',all_service=all_service)

@app.route('/gender',methods=['GET','POST'])
def gender():
    if request.method == "GET":
        return render_template('gender.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        if form['gender'] == "male":
            gender = 1
        elif form['gender']== "female":
            gender = 0
        new_service = Service(name=name, yob=yob, phone=phone, gender=gender)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/update-service/<service_id>',methods=['GET','POST'])
def update_service(service_id):
    all_service = Service.objects.with_id(service_id)
    if request.method == "GET":
        return render_template('update-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        phone = form['phone']
        height = form['height']
        status = form['status']
        description = form['description']
        measurements = form['measurements']
        if form['gender'] == "male":
            gender = 1
        elif form['gender']== "female":
            gender = 0
        new_service = Service(name=name,
                              yob=yob,
                              address=address,
                              phone=phone,
                              height=height,
                              status=status,
                              description=description,
                              measurements=measurements,
                              gender=gender)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/signin', methods=["GET","POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        email = form['email']
        username = form['username']
        password = form['password']
        new_user = User(name=name,
                        email=email,
                        username=username,
                        password=password)
        new_user.save()
        return redirect(url_for('index'))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        all_user = User.objects()
        if username == "username" and password == "password":
            session ['loggedin'] = True
            return redirect(url_for('service_page'))
        else:
            return "Wrong"


@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))

@app.route('/order', methods=["GET","POST"])
def order():
    return render_template('order.html')
    # if request.method == "GET":
    #     new_order = User(nameservice=nameservice,
    #                     username=username,
    #                     time=time,
    #                     is_accepted=is_accepted)
    #     new_order.save()
    # elif request.method == "POST":
    #     return render_template('order.html')

@app.route('/order-page')
def order_page():
    all_order = Order.objects()
    return render_template('order-page.html',all_order = all_order)


if __name__ == '__main__':
  app.run(debug=True)
