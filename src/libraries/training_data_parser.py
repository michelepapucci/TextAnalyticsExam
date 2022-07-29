import re
import json
import csv


class TrainingDataParser:

    def __init__(self, src_path):
        self.src_path = src_path

    def to_dict(self):
        user_posts = {}
        current_id = None
        for line in open(self.src_path):
            if '<user id' in line:
                user_id = re.findall('<user id="(.*?)"', line)[0]
                current_id = user_id
                topic = re.findall('topic="(.*?)"', line)[0]
                gender = re.findall('gender="(.*?)"', line)[0]
                age = re.findall('age="(.*?)"', line)[0]
                if user_id not in user_posts:
                    user_posts[user_id] = {
                        'topic': topic,
                        'gender': gender,
                        'age': age,
                    }
                else:
                    print(f"Duplicate id {user_id}")
            elif '</user>' in line:
                current_id = None
            elif line != '\n' and 'post>' not in line:
                if 'posts' in user_posts[current_id]:
                    user_posts[current_id]['posts'].append(line)
                else:
                    user_posts[current_id]['posts'] = [line]
        return user_posts

    def to_csv(self, file_output=False, output_path='src/data/post_processed', output_name='training.csv'):
        data = self.to_dict()

        rowlist = []
        for user in data:
            for sentence in data[user]['posts']:
                row = [user, data[user]['gender'], data[user]['age'], data[user]['topic'], sentence.strip()]
                rowlist.append(row)

        if file_output:
            file = open(f"{output_path}/{output_name}", "w", encoding="utf-8", newline='')
            writer = csv.writer(file, delimiter=',',
                                lineterminator='\r\n',
                                quoting=csv.QUOTE_NONNUMERIC
                                )
            writer.writerow(['Id', 'Gender', 'Age', 'Topic', 'Sentence'])
            writer.writerows(rowlist)
            file.close()
        return rowlist

    def to_json(self):
        return json.dumps(self.to_dict())
