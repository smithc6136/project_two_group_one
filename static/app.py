from sqlalchemy import create_engine
import psycopg2
from flask import Flask, jsonify

conn_string = "host='localhost' dbname='pothole_db' user='mark' password='password'"

# rows = cur.fetchall()
# # print(rows)

# print("\nShow me the databases:\n")
# for row in rows:
#     print("   ", row[9])

app = Flask(__name__)


@app.route("/")
def location():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM potholes""")
    # cur.close()
    locationrows= cur.fetchall()
    # print(locationrows)

    # new_dict = {}
    # for row in results:
    #     new_dict[row.location] = row.category
    # print(new_dict)
    return jsonify({"location":locationrows})
        

if __name__ == '__main__':
    app.run(debug=True, port=5001)