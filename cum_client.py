from dash import Dash, html, dcc, callback, State, Output, Input
from requests import post
url = "http://127.0.0.1:8000"

app = Dash(__name__)

app.layout = html.Div(children = [
    html.Div(id = "output-conversation",
             style = {"width": "90%",
                      "height": "80vh",
                      "margin": "auto",
                      "overflow-y": "auto"}),
    html.Div(children = [
        dcc.Textarea(id = "input-text", placeholder = "Type here...",
                     style = {"width": "100%"}),
        html.Button("Submit", id = "input-submit")
        ],
        style = {"width": "90%", "margin": "auto"}
    ),
    dcc.Store(id = "store-chat", data = "")
])

@app.callback(
    [Output("store-chat", "data"), Output("input-text", "value")],
    [Input("input-submit", "n_clicks")],
    [State("input-text", "value"), State("store-chat", "data")]
)
def query_chatbot(n_clicks, input_value, chat):
    if n_clicks == 0:
        return "", ""
    if input_value == "" or input_value is None:
        return chat, ""
    chat += f"You: {input_value}<split>Bot: "

    query = chat.replace("<split>", "\n").replace("Bot:", "").replace("You:", "")
    result = post(url, json = {"question": query})

    if result.status_code == 200:
        response = result.json()["response"]
    else:
        response = f"Error: {result.reason}"
    chat += f"{response}<split>"

    return chat, ""

@app.callback(
    Output("output-conversation", "children"),
    Input("store-chat", "data")
)
def update_conversation(conversation):
    return [
        html.Div(message, style = {
            "max-width": "60%",
            "width": "max-content",
            "padding": "10px"
        })
        for message in conversation.split("<split>")
    ]
if __name__ == "__main__":
    app.run(port = 5000, debug = True)