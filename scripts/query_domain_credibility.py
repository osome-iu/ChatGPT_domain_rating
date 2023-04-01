import openai
import json
import gzip
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[-1]

# The key.json file should contains the API key for OpenAI:
# {"OPENAI_API_KEY": "YOUR_API_KEY"}
with open("/path/to/your/chatgpt/key.json") as f:
    openai_key_obj = json.load(f)

openai.api_key = openai_key_obj.get("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo-0301"

system = "You are an assistant to help the user determine the credibility of websites"
prompt = """
    Rate the website's credibility: {domain} on a scale between 0 and 1, where 0 means very low credibility and 1 means very high credibility.
    Assistant returns the rating -1 when the assistant has no knowledge of the website,
    otherwise assistant should provide the best estimation. Assistant should only provide the result in JSON format, do not provide anything else
    here is an example:
    {example}
    """
example = {'url': 'exmaple.com', 'rating': 0.5, 'reason': 'The example website is known to post credible content.'}
example_str = json.dumps(example).replace('"', "'")

domain_df = pd.read_csv(input_file)

with gzip.open(output_file, "wb") as f:
    for index, row in domain_df.iterrows():
        domain = row["domain"]
        print(domain)

        try:
            response = openai.ChatCompletion.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt.format(domain=domain, example=example_str)},
                ],
                temperature=0,
            )
            resp_json = response.to_dict_recursive()
            resp_in_bytes = f"{json.dumps(resp_json)}\n".encode(encoding="utf-8")
            f.write(resp_in_bytes)
        except Exception as e:
            print(e)

