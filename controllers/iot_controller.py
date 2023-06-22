from flask import Blueprint, render_template,redirect,url_for, request
from models import Sensor, Actuator
iot = Blueprint("iot", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/register_sensor")
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors)

@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))


@iot.route("/register_actuator")
def iot_register_actuator():
    return render_template("/iot/register_actuator.html")


@iot.route("/view_actuators")
def iot_view_actuators():
    actuators = Actuator.get_actuators()
    return render_template("/iot/view_actuators.html", actuators=actuators)


@iot.route("/save_actuators", methods=["POST"])
def save_actuators():
    name = request.form.get("name", None)
    model = request.form.get("model", None)
    brand = request.form.get("brand", None)
    voltage = request.form.get("voltage", None)
    description = request.form.get("description", None)
    is_active = True if request.form.get("name", None) == "on" else False
    actuator_type = request.form.get("type", None)

    Actuator.save_actuator(name, model, brand, voltage, description, is_active, actuator_type)

    return redirect(url_for("admin.iot.iot_view_actuators"))