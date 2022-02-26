import json
from flask import Flask, request, jsonify

from gdocs_ques.qa_gen_for_docs import load_model, get_qa


app = Flask(__name__)
app.secret_key = 'secret_key'


def send_error_response(message):
    return jsonify({
        'result': 'error',
        'message': message,
    })


def check_fields(data):
    if 'text' not in data:
        return 'text'
    if 'num_questions' not in data:
        return 'num_questions'
    if 'answer_style' not in data:
        return 'answer_style'
    return ''


@app.route('/', methods=['GET'])
def index():
    return jsonify({'result': 'success'})


@app.route('/', methods=['POST'])
def hello():
    if len(request.data) == 0:
        return send_error_response('No data sent.')

    data = json.loads(request.data)

    # Validate fields
    missing_field = check_fields(data)
    if missing_field != '':
        return send_error_response(f'{missing_field} missing for data.')

    model = load_model()
    qa_pairs = get_qa(model, data['text'], int(data['num_questions']), data['answer_style'])

    return jsonify({'result': 'success', 'qa_pairs': qa_pairs})


if __name__ == '__main__':
    app.run(host='0.0.0.0')

