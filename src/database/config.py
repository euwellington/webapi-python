from src.setup import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'u5mmcrfkc6uvbx9e'
app.config['MYSQL_DATABASE_PASSWORD'] = 'RFov03t532hN0QFuiZSY'
app.config['MYSQL_DATABASE_DB'] = 'bqckidktpnyx3k1lp5td'
app.config['MYSQL_DATABASE_HOST'] = 'bqckidktpnyx3k1lp5td-mysql.services.clever-cloud.com'

mysql.init_app(app)