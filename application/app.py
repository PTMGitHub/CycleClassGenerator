from psycopg2 import connect
from flask import render_template 
from flask import Flask
from random import randint

t_host = "db"
t_port = "5432" # default postgres port
t_dbname = "D_db"
t_user = "postgres"
t_pw = "root"
db_conn = connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()

app = Flask(__name__)
@app.route('/')
@app.route('/index', methods=['GET'])
def index():

    def query_track_designs_table(search_prase):
        query_warm_ups = "SELECT * FROM track_designs WHERE aim LIKE '%" + search_prase + "%';"
        db_cursor.execute(query_warm_ups)
        return db_cursor.fetchall()
        


    returned_warm_ups = query_track_designs_table('warm up')
    no_of_warm_ups_return = len(returned_warm_ups)
    selected_warm_up = randint(0,no_of_warm_ups_return-1)

    warm_up = returned_warm_ups[selected_warm_up]
    # print(warm_ups[0])
    # print("hello")
    
    return render_template("index.html", warm_up=warm_up)
    #return render_template("org_index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

db_conn.close()