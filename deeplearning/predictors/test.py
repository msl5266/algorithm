import json
import jieba
from predictors.predict import Predictor


with open("../config/transformer_config.json", "r") as fr:
    config = json.load(fr)

with open("../data/imdb/eval_data.txt", "r", encoding="utf8") as f:
    data = [line for line in f.readlines()]
    inputs = []
    labels = []
    for line in data:
        try:
            x, y = line.strip().split("<SEP>")
            inputs.append(x.strip())
            labels.append(y.strip())
        except:
            print(line)

# text = " ".join([" ".join(jieba.lcut(line)) for line in data])

predictor = Predictor(config)

total = len(labels)
print(total)
corr = 0
for i in range(len(inputs)):
    result = predictor.predict(inputs[i].split(" "))
    if result == labels[i]:
        corr += 1
    else:
        print(inputs[i])
print(corr / total)

