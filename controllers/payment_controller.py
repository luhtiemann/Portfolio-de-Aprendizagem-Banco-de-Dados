from flask import Blueprint, render_template,redirect,url_for, request
from models import Employee, Waiter, Payment, WorkingTimeRecord

payment = Blueprint("payment", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@payment.route("/")
def payment_index():
    return render_template("/payment/payment_index.html")


@payment.route("/register_payment")
def register_payment():
    employees = Employee.get_employee()
    return render_template("/payment/register_payment.html", employees = employees)

@payment.route("/view_payments")
def view_payments():
    payments = Payment.get_payments()
    return render_template("/payment/view_payments.html", payments = payments)

@payment.route("/save_payments", methods = ["POST"])
def save_payments():
    employee_id = request.form.get("employee_id")
    payment_datetime = request.form.get("payment_datetime")
    reference_date = request.form.get("reference_date")
    payment_value = request.form.get("payment_value")

    Payment.save_payment(employee_id, payment_datetime, reference_date, payment_value)

    return redirect(url_for('admin.payment.view_payments'))


@payment.route("/register_working_time")
def payment_register_working_time_record():
    waiters = Waiter.get_waiters()
    return render_template("/payment/register_working_time.html", waiters = waiters)


@payment.route("/view_working_time")
def payment_view_working_time_records():
    working_time_records = WorkingTimeRecord.get_working_time_records()
    return render_template("/payment/view_working_time.html", working_time_records=working_time_records)


@payment.route("/save_working_time", methods=["POST"])
def save_working_time_records():
    waiter_id = request.form.get("waiter_id", None)
    payment_id = request.form.get("payment_id", None)
    record_datetime = request.form.get("record_datetime", None)
    number_of_hours = request.form.get("number_of_hours", None)

    WorkingTimeRecord.save_working_time_record(waiter_id, payment_id, record_datetime, number_of_hours)

    return redirect(url_for("admin.payment.payment_view_working_time_records"))