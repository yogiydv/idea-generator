from flask import Flask
import random

app = Flask(__name__)

# Lists of words for the software ideas generator
keywords = ['Application', 'System', 'Platform', 'Tool', 'Service', 'Interface']
actions = ['management', 'monitoring', 'optimization', 'analysis', 'automation']
targets = ['projects', 'tasks', 'processes', 'data', 'reports']
extensions = ['for businesses', 'for learning', 'for developers', 'for commerce', 'for e-commerce']

# Generate a software idea
def generate_idea():
    idea = random.choice(keywords) + ' ' + random.choice(actions) + ' ' + random.choice(targets)
    extension = random.choice(extensions)
    if random.randint(0, 1):
        idea += ' ' + extension
    return idea

@app.route('/')
def main():
    idea = generate_idea()
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Software Ideas Generator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f7f7f7;
            }}

            .container {{
                text-align: center;
                padding: 20px;
                background-color: #ffffff;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }}

            h1 {{
                font-size: 32px;
                color: #333;
                margin-bottom: 20px;
            }}

            p {{
                font-size: 20px;
                color: #555;
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Software Ideas Generator</h1>
            <p>Generated software idea:</p>
            <p>{idea}</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
