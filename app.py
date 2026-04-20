from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Mohammad@1830',
    database='order_db'
)

@app.route('/')
def home():
    return render_template('index.html')


# ✅ CREATE
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO orders (item, status) VALUES (%s, %s)",
        (data['item'], "Pending")
    )

    connection.commit()
    order_id = cursor.lastrowid

    return jsonify({
        "id": order_id,
        "item": data['item'],
        "status": "Pending"
    })


# ✅ READ
@app.route('/orders', methods=['GET'])
def get_orders():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orders")

    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "item": row[1],
            "status": row[2]
        })

    return jsonify(result)


# ✅ UPDATE
@app.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    data = request.json
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE orders SET status=%s WHERE id=%s",
        (data['status'], id)
    )

    connection.commit()
    return jsonify({"message": "Updated successfully"})


# ✅ DELETE
@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM orders WHERE id=%s", (id,))
    connection.commit()

    return jsonify({"message": "Deleted successfully"})


app.run(debug=True)