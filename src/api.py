from flask import Flask, Response, stream_with_context
from flask import request
from flask_cors import CORS

from query_model import *

app = Flask(__name__)
CORS(app)

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/api/question', methods=['POST'])
def post_question():
    json = request.get_json(silent=True)
    question = json['question']
    logging.info("post question `%s`", question)
    resp = chat(question)
    return Response(stream_with_context(resp.response_gen))


if __name__ == '__main__':
    init_llm()
    index = init_index()
    init_query_engine(index)
    app.run(host='0.0.0.0', port=HTTP_PORT, debug=True)
