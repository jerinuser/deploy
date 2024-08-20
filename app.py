
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    json_data = None
    error_message = None

    if request.method == 'POST':
        # Get the bytes data from the form
        byte_data = request.form.get('byte_data', '')

        if byte_data:
            try:
                # Step 1: Handle Python-specific syntax
                # Strip the b' and ' from the string, if present
                if byte_data.startswith("b'") and byte_data.endswith("'"):
                    byte_data = byte_data[2:-1]

                # Replace Python booleans and None with JSON equivalents
                byte_data = byte_data.replace("True", "true").replace("False", "false").replace("None", "null")

                # Replace single quotes with double quotes to comply with JSON format
                byte_data = byte_data.replace("'", '"')

                # Convert the string to bytes
                byte_data = bytes(byte_data, 'utf-8')

                # Convert bytes to string and then to JSON
                json_data_str = byte_data.decode('utf-8')

                # Step 2: Try to parse the string as JSON
                json_data = json.loads(json_data_str)

                # Convert the JSON object back to a formatted string
                json_data = json.dumps(json_data, indent=4)

            except json.JSONDecodeError as e:
                error_message = f"Invalid JSON format: {str(e)}"
            except Exception as e:
                error_message = f"Error: {str(e)}"
        else:
            error_message = "No data provided."

    return render_template('index.html', json_data=json_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
