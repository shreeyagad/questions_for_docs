import json
from datetime import datetime
from flask import Flask, request, jsonify

from gdocs_ques.qa_gen_for_docs import load_model, get_qa


app = Flask(__name__)
app.secret_key = 'some_secret_key'


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


def print_log(message):
    print(f'[{datetime.now().strftime("%m:%d:%y - %H:%M:%S")}] {message}')


@app.before_first_request
def get_qa_model():
    app.model = load_model()


@app.route('/', methods=['GET'])
def index():
    return jsonify({'result': 'success'})


@app.route('/', methods=['POST'])
def hello():
    print_log('Request Received')
    if len(request.data) == 0:
        return send_error_response('No data sent.')

    data = json.loads(request.data)

    # Validate fields
    missing_field = check_fields(data)
    if missing_field != '':
        return send_error_response(f'{missing_field} missing for data.')

    try:
        num_questions = int(float(data['num_questions']))
    except ValueError:
        return send_error_response('Invalid data type for num question parameter')

    answer_style = data['answer_style']
    if answer_style not in ['all', 'multiple_choice', 'sentence']:
        return send_error_response('answer style can only be of type "all", "multiple_choice" or "sentence".')

    print_log('Generation QAs')
    qa_pairs = get_qa(app.model, data['text'], num_questions, answer_style)

    print_log('Sending response')

    return jsonify({'result': 'success', 'qa_pairs': qa_pairs})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
