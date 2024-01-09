from flask import Flask, jsonify, request
from main import linear_search, binary_search, ternary_search, jump_search
import random
from flask_cors import CORS
import matplotlib.pyplot as plt

app = Flask(__name__)

CORS(app)

def check_time_complexity_of_algorithms(linear=False, binary=False, ternary=False, jump=False, inp_list=[], number=0):

    linear_search_index = binary_search_index = ternary_search_index = jump_search_index = -1
    linear_search_time = binary_search_time = ternary_search_time = jump_search_time = -1
    
    inp_list = sorted(inp_list)
    if linear:
        print("linear", linear)
        linear_search_index, linear_search_time = linear_search(inp_list, number)
    if binary:
        print("binary", binary)
        binary_search_index, binary_search_time = binary_search(inp_list, number)
    if ternary:
        print("ternary", ternary)
        ternary_search_index, ternary_search_time = ternary_search(inp_list, number)
    if jump:
        print("jump", jump)
        jump_search_index, jump_search_time = jump_search(inp_list, number)
    
    response_data = {
        'linear': {
            "searching_time": linear_search_time,
            "index": linear_search_index,
        },
        'binary': {
            "searching_time": binary_search_time,
            "index": binary_search_index,
        },
        'ternary': {
            "searching_time": ternary_search_time,
            "index": ternary_search_index,
        },
        'jump': {
            "searching_time": jump_search_time,
            "index": jump_search_index,
        }
    }
    return response_data

def graph(response_data):
    
    # Extracting data

    categories = list(response_data.keys())
    search_times = [data['searching_time'] for data in response_data.values()]

    # Plotting the bar graph
    plt.bar(categories, search_times, color='green')

    # Adding labels and title
    plt.xlabel('Search Algorithms')
    plt.ylabel('Search Time (in seconds)')
    plt.title('Comparison of Search Times')
    
    plt.savefig('search_times_comparison.png')
    # Display the plot
    # plt.show()


@app.route('/', methods = ["GET", "POST"])
def checking():
    data = request.get_json()
    print(data)
    linear = data['Linear Search']
    binary = data['Binary Search']
    jump = data['Jump Search']
    ternary = data['Ternary Search']
    list_len = data['inputString']
    inp_list = [random.randint(1, list_len) for _ in range(list_len)]
    # print(inp_list)
    number = data['findingElement']
    response_data = check_time_complexity_of_algorithms(
        linear=linear, binary=binary, ternary=ternary, jump=jump,
        inp_list=inp_list, number=number
    )
    print(response_data)
    # no_element_found = all(data['index'] == -1 for data in response_data.values())
    # if not no_element_found:
    #     graph(response_data)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4001)
