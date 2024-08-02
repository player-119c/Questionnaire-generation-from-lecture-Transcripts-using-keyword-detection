import os
import google.generativeai as genai

def print_hi(text):
    with open("keywords.txt", "r") as f:
        data = f.read()

    keyword_lines = data.splitlines()
    keywords = ""
    for i in range(len(keyword_lines)):
        keywords = keywords + keyword_lines[i] + " ,"

    genai.configure(api_key="AIzaSyB09654M-nbPmDNQAZroCXSbP7awL3ICis")

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f"{keywords}  generate 10  mcq questions utlizing all these keyword along with answer key")
    print(response.text)

if __name__ == '__main__':
    print_hi('Pycharm')

