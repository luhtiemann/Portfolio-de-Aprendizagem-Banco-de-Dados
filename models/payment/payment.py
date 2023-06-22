from models.db import db
from models import Employee

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), db.ForeignKey(Employee.id))
    payment_datetime = db.Column(db.DateTime, nullable = False)
    reference_date = db.Column(db.Date, nullable = True)
    payment_value = db.Column(db.Float, nullable=True)

    working_time_records = db.relationship('WorkingTimeRecord', backref='payments')
    orders = db.relationship('Order', backref='payments')

    def get_payments():
        payments = Payment.query.join(Employee, Employee.id == Payment.employee_id)\
                         .add_columns(Payment.employee_id, Employee.user_id, Employee.created_at, Payment.id, Payment.payment_datetime, 
                                      Payment.reference_date, Payment.payment_value, ).all()
        
        return payments
    
    def save_payment(employee_id, payment_datetime, reference_date, payment_value):

        #employee = Employee(id=employee_id)
        payment = Payment(employee_id = employee_id, payment_datetime = payment_datetime, reference_date = reference_date, payment_value = payment_value)
        
        #employee.payments.append(payment)
        db.session.add(payment)
        db.session.commit()