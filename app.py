from flask import Flask, request, render_template
from models import Conn
from collections import defaultdict
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    result = Conn.query_sql('SELECT * FROM nodes order by level')
    nodes = {}
    nodes_children = defaultdict(list)
    for r in result:
        print r
        nodes[r[0]] = r
        nodes_children[r[3]].append(r[0])
    # print(result[1])
    print nodes
    print nodes_children
    return render_template('index.html', nodes=nodes, nodes_children=nodes_children)


@app.route('/addNode', methods=["POST"])
def add_node():
    parent_id = int(request.form['parent_id'])
    name = request.form['name']
    if parent_id == 0:
        level = 1
    else:
        print(parent_id)
        result = Conn.query_one_sql('SELECT * FROM nodes where id=%s limit 1', parent_id)
        level = result[2]+1
    Conn.exec_sql('insert into nodes (name,level,parent_id,add_time) values (%s,%s,%s,%s)', (name, level, parent_id, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return '0'


@app.route('/delNode', methods=["POST"])
def del_node():
    node_id = int(request.form['id'])
    Conn.exec_sql('DELETE FROM nodes where id=%s limit 1', node_id)
    return '0'


@app.route('/addArticle', methods=["POST"])
def add_article():
    node_id = int(request.form['id'])
    name = request.form['name']
    author = request.form['author']
    result = Conn.query_one_sql('SELECT COUNT(*) FROM articles WHERE name=%s and node_id=%s', (name, node_id))
    if not result[0]:
        return '-1'
    Conn.exec_sql('INSERT INTO articles (node_id,name,author,upd_time) values (%s,%s,%s,%s)', (node_id, name, author, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return '0'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
