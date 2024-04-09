import logging
import sys

from flask import Flask, Response, stream_with_context, json
from flask import request
from flask_cors import CORS

from guard.actions import init_llm, chat
from src.config import HTTP_PORT

app = Flask(__name__)
CORS(app)

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/api/question', methods=['POST'])
def post_question():
    req = request.get_json(silent=True)
    question = req['question']
    resp = chat(question)
    return Response(stream_with_context(resp))


if __name__ == '__main__':
    global query_engine
    init_llm()
    app.run(host='0.0.0.0', port=HTTP_PORT, debug=True)
