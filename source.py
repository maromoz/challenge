from subprocess import Popen, PIPE
import ast
import rx
import json


def stream_func():
    events_dict = {}
    proc = Popen("generator-windows-amd64.exe", stdout=PIPE)
    while proc.poll() is None:
        line = proc.stdout.readline().strip()
        # Trying to decode the line to UTF,
        # Error ==> line is jibrish and should skip
        try:
            line = line.decode("utf-8")
            print(line)
            line_as_dict = ast.literal_eval(line)
            try:
                x = events_dict[line_as_dict.get('event_type')]

                try:
                    x = events_dict[line_as_dict.get('event_type')][line_as_dict.get('data')]
                    events_dict[line_as_dict.get('event_type')][line_as_dict.get('data')] += 1
                except KeyError:
                    events_dict[line_as_dict.get('event_type')][line_as_dict.get('data')] = 1

            except:
                events_dict[line_as_dict.get('event_type')] = {}
                events_dict[line_as_dict.get('event_type')][line_as_dict.get('data')] = 1

            with open('data.txt', 'w') as outfile:
                json.dump(events_dict, outfile)

        except:
            print('Error, skipping', line)


rx.interval(1,stream_func())

