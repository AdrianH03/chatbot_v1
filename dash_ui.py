import dash

import dash_html_components as html

students = [
    {"name": "Alice", "surname": "Johnson", "age": 16, "grade": "A"},
    {"name": "Bob", "surname": "Smith", "age": 17, "grade": "B"},
    {"name": "Charlie", "surname": "Brown", "age": 15, "grade": "A"},
    {"name": "Diana", "surname": "Miller", "age": 16, "grade": "C"},
    {"name": "Ethan", "surname": "Davis", "age": 18, "grade": "B"},
    {"name": "Fiona", "surname": "Wilson", "age": 17, "grade": "A"},
    {"name": "George", "surname": "Taylor", "age": 16, "grade": "B"},
    {"name": "Hannah", "surname": "Anderson", "age": 15, "grade": "A"},
    {"name": "Ian", "surname": "Thomas", "age": 17, "grade": "C"},
    {"name": "Julia", "surname": "Moore", "age": 16, "grade": "B"},
    {"name": "Kevin", "surname": "Martin", "age": 18, "grade": "A"},
    {"name": "Laura", "surname": "Jackson", "age": 17, "grade": "B"},
    {"name": "Michael", "surname": "White", "age": 16, "grade": "C"},
    {"name": "Nina", "surname": "Harris", "age": 15, "grade": "A"},
    {"name": "Oscar", "surname": "Clark", "age": 17, "grade": "B"},
    {"name": "Paula", "surname": "Lewis", "age": 16, "grade": "A"},
    {"name": "Quinn", "surname": "Walker", "age": 18, "grade": "B"},
    {"name": "Rachel", "surname": "Hall", "age": 17, "grade": "C"},
    {"name": "Sam", "surname": "Young", "age": 16, "grade": "A"},
    {"name": "Tina", "surname": "King", "age": 15, "grade": "B"},
]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Student Data", style={"color": "#2222ff"}),
    dash.dash_table.DataTable(students, page_size = 5)
])

if __name__ == "__main__":
    app.run(debug = True)