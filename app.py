from flask import Flask, render_template

app = Flask(__name__)

data = [
    {
        'text': "Parent 1",
        'nodes': [
            {
                'text': "Child 1",
                'nodes': [
                    {
                        'text': "Grandchild 1"
                    },
                    {
                        'text': "Grandchild 2"
                    }
                ]
            },
            {
                'text': "Child 2"
            }
        ]
    },
    {
        'text': "Parent 2"
    },
    {
        'text': "Parent 3"
    },
    {
        'text': "Parent 4"
    },
    {
        'text': "Parent 5"
    }
]


@app.route('/')
def index():
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
