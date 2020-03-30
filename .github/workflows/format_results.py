from pytablewriter import MarkdownTableWriter
import json


def intent_table():
    writer = MarkdownTableWriter()
    writer.table_name = "Intent Cross-Validation Results (3 folds)"

    with open("results/intent_report.json", "r") as f:
        data = json.loads(f.read())

    cols = ["support", "f1-score", "confused_with"]
    writer.headers = ["class"] + cols

    classes = list(data.keys())
    try:
        classes.remove("accuracy")
    except:
        pass
    classes.sort(key=lambda x: data[x]["support"], reverse=True)

    def format_cell(data, c, k):
        if not data[c].get(k):
            return "N/A"
        if k == "confused_with":
            return ", ".join([f"{k}({v})" for k, v in data[c][k].items()])
        else:
            return data[c][k]

    writer.value_matrix = [
        [c] + [format_cell(data, c, k) for k in cols] for c in classes
    ]

    return writer.dumps()


def entity_table():

    writer = MarkdownTableWriter()
    writer.table_name = "Entity Cross-Validation Results (5 folds)"

    with open("results/DIETClassifier_report.json", "r") as f:
        data = json.loads(f.read())

    cols = ["support", "f1-score", "precision", "recall"]
    writer.headers = ["entity"] + cols

    classes = list(data.keys())
    classes.sort(key=lambda x: data[x]["support"], reverse=True)

    def format_cell(data, c, k):
        if not data[c].get(k):
            return "N/A"
        else:
            return data[c][k]

    writer.value_matrix = [
        [c] + [format_cell(data, c, k) for k in cols] for c in classes
    ]

    return writer.dumps()


intents = intent_table()
entities = entity_table()

with open("results.md", "w") as f:
    f.write(intents)
    f.write("\n\n\n")
    f.write(entities)
