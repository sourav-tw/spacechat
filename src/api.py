from flask import Flask, Response, stream_with_context
from flask import request
from flask_cors import CORS
import logging
import sys
from query_model import *
from config import *

app = Flask(__name__)
CORS(app)

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/api/question', methods=['POST'])
def post_question():
    json = request.get_json(silent=True)
    question = json['question']
    logging.info("post question `%s`", question)

    def generate_response():
        resp = chat(question)
        for chunk in resp.response_gen:
            yield chunk

    return Response(stream_with_context(generate_response()))


if __name__ == '__main__':
    init_llm()
    index = init_index()
    init_query_engine(index)
    app.run(host='0.0.0.0', port=HTTP_PORT, debug=True)
