from flask import Flask, request, send_from_directory
import pymysql as db # <-- adjust for MySQL connection
import pandas as pd

app = Flask(__name__)
REPORT_DIRECTORY = '/tmp/pipeline/out_data'

class DisasterDB:
 # Connect to database
 def __init__(self):
   # reference https://opensourceforu.com/2009/05/database-programming-in-python/
   config = Config.ConfigParser()
   config.read('config.ini')
   self.DB_HOST = str(config['DEFAULT']['PRODUCTION_DB_HOST'])
   self.DB_USER = str(config['DEFAULT']['PRODUCTION_DB_USER'])
   self.DB_PASSWORD = str(config['DEFAULT']['PRODUCTION_DB_PW'])
   self.DB_DB=str(config['DEFAULT']['PRODUCTION_DB_DB'])
   self.connection = db.connect(host=self.DB_HOST,
                                user=self.DB_USER,
                                password=self.DB_PASSWORD,
                                db=self.DB_DB,
                                charset='utf8mb4')

 def get_all_data(self):
     """
     Retrieve all data from the disaster database
     """
     query = (
        """
        select

        """
        )
     disaster_data = pd.read_sql( query ,self.connection )
     return(disaster_data)

# Must ping the specific path/filename
@app.route('/apiv1/<path:path>')
def get_reports(path):
    data_frame = DisasterDB().get_all_data()
    #Records csv file to the working directory
    data_frame.to_csv("all_data.csv")
    return send_from_directory(REPORT_DIRECTORY, path, as_attachment=True)


if __name__ == '__main__':
    app.run(port=8052,debug=True,host='0.0.0.0')
