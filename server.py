from flask import Flask, jsonify
app = Flask(__name__)
import json


@app.route("/")
def home():
    return "Please choose one of two function and paste them in your URL\n" \
           "/events/countByEventType   ------> For getting count of events by event type\n" \
           "/events/countWords   ------> For getting count of total words"

@app.route("/events/countByEventType")
def events_count_by_event_type():
    with open('data.txt') as json_file:
        data = json.load(json_file)
        events = {}
        for k, v in data.items():
            events[k] = sum(value for value in v.values())
        return jsonify(events)

@app.route("/events/countWords")
def events_count_words():
    with open('data.txt') as json_file:
        data = json.load(json_file)
        events = {}
        words_sum = 0
        for k, v in data.items():
            for key, value in v.items():
                try:
                    events[key] += value
                except:
                    events[key] = value
        return jsonify(events)

if __name__ == "__main__":
    app.run()