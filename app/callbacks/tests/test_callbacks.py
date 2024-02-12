from dash.testing.application_runners import import_app
from dash.testing.browser import Browser

def test_update_output(dash_duo: Browser):
    # Import your Dash app
    app = import_app("visualization_project.callbacks.register_callbacks")
    
    # Start the Dash app in a test browser
    dash_duo.start_server(app)
    
    # Input a test value into the dummy-input component
    test_value = "Test input"
    dash_duo.find_element("#dummy-input").send_keys(test_value)
    
    # Wait for the output to be updated
    dash_duo.wait_for_text_to_equal("#dummy-output", f"You have entered {test_value}", timeout=4)
    
    # Assert that the output text is as expected
    output_text = dash_duo.find_element("#dummy-output").text
    assert output_text == f"You have entered {test_value}", "The output text does not match the expected value."
