import json

# Open the input file
with open('yelp_academic_dataset_review.json') as f:
    data = [json.loads(line) for line in f]

# Take only the first 100000 dictionaries
data = data[:100000]

# Extract the 'stars' and 'text' keys from each dictionary
new_data = []
for d in data:
    if isinstance(d, dict):
        new_data.append({'stars': d.get('stars'), 'text': d.get('text')})

# Write the new data to a new file
with open('yelp_academic_dataset_review_v2.json', 'w') as f:
    json.dump(new_data, f)