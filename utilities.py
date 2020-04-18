import json

def create_drop_down_options(json_file, dictionary=True):
    with open("data/" + json_file, "r") as read_file:
        data = json.load(read_file)

    output = []
    if dictionary is True:
        for item in data:
            output.append({'label': item, 'value': data[item]})
    else:
        for item in data:
            output.append({'label': item, 'value': item})

    return output




# def create_drop_down_options(data, dictionary=True):
#     data_list = []
#
#     if dictionary is True:
#         for value in data:
#             data_list.append({'label': value, 'value': data[value]})
#     else:
#         for value in data:
#             data_list.append({'label': value, 'value': value})
#
#     return data_list