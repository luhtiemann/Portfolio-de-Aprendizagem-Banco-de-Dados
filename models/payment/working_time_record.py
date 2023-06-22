from models.db import db
from models import Person, Employee
from models import Waiter 
from models import Payment



class WorkingTimeRecord(db.Model):
    __tablename__ = 'working_time_records'
    id = db.Column(db.Integer(), primary_key=True)
    waiter_id = db.Column(db.Integer(), db.ForeignKey(Waiter.id), nullable=False)
    payment_id = db.Column(db.Integer(), db.ForeignKey(Payment.id), nullable=True)
    record_datetime = db.Column(db.DateTime, nullable = False)
    number_of_hours = db.Column(db.Float, nullable = False)

    def get_working_time_records():
        working_time_records = WorkingTimeRecord.query.join(Waiter, Waiter.id == WorkingTimeRecord.waiter_id)\
                                                .join(Payment, Payment.id == WorkingTimeRecord.payment_id)\
                                                .join(Employee, Employee.id == Waiter.id)\
                                                .join(Person, Person.id == Employee.id)\
                                                .add_columns(Person.name,WorkingTimeRecord.waiter_id, WorkingTimeRecord.payment_id, WorkingTimeRecord.record_datetime, WorkingTimeRecord.number_of_hours).all()
        #working_time_records = WorkingTimeRecord.query.join(Waiter, Waiter.id == WorkingTimeRecord.waiter_id)\
                   # .join(Payment, Payment.id == WorkingTimeRecord.payment_id)\
                   # .join(Employee, Employee.id == Waiter.id)\
                   # .add_columns(WorkingTimeRecord.waiter_id, WorkingTimeRecord.payment_id, WorkingTimeRecord.record_datetime, 
                   #              WorkingTimeRecord.number_of_hours).all()
        
        return working_time_records
    
    def save_working_time_record(waiter_id, payment_id, record_datetime, number_of_hours):
        #waiter= Waiter(waiter_id = Waiter.id)
        working_time_record = WorkingTimeRecord(waiter_id=waiter_id, payment_id = payment_id, record_datetime = record_datetime,
                                                number_of_hours = number_of_hours)

        #waiter.working_time_records.append(working_time_record)
        db.session.add(working_time_record)
        db.session.commit()