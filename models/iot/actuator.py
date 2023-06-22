from models import db, Device

class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("actuator_id", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
    actuator_type = db.Column(db.String(30))

    activations = db.relationship("Activation", backref="actuators", lazy=True)

    def save_actuator(name, model, brand, voltage, description, is_active, actuator_type):
        device = Device(name=name, model=model, brand=brand, voltage=voltage, description=description, is_active=is_active)

        actuator = Actuator(id=device.id, actuator_type=actuator_type)
        device.actuators.append(actuator)

        db.session.add(device)
        #db.session.add_all([])
        db.session.commit()

    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id==Actuator.id)\
                        .add_columns(Device.id, Device.name, Device.model, Device.brand, Device.voltage, Device.description, Device.is_active,
                                     Actuator.actuator_type).all() #constroi automaticamente a consulta
        
        return actuators
    

    def delete_actuator(id):
        actuator = Actuator.query.filter(Actuator.id == id).first()
        Actuator.query.filter_by(actuator_type="%").delete()
        actuator.delete()

    def delete_actuator_by_measure(actuator_type):
        Actuator.query.filter_by(actuator_type=actuator_type).actuator_type()
        db.session.commit()

    def update_actuator(data):
        Device.query.filter_by(id=data['actuator_id'])\
                .update(dict(name = data['name'], brand=data['brand'], model = data['model'], 
                        voltage = data['voltage'], description = data['description'], 
                        is_active = data['is_active']))
        
        Actuator.query.filter_by(id=data['actuator_id'])\
                        .update(dict(actuator_type = data['actuator_type']))
        db.session.commit()