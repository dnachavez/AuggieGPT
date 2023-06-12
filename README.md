# Auggie: A ChatGPT-Powered Chatbot Assistant

Auggie is a simple Streamlit application powered by OpenAI's GPT-3.5-turbo model. This chatbot assistant can provide answers to questions specifically about the University of Southern Philippines Foundation (USPF).

## Requirements

- Python 3.7+
- OpenAI account and API keys
- Streamlit
- Other Python libraries specified in `requirements.txt`

## Installation and Deployment

1. Fork or clone the repository to your GitHub account.

2. Visit [Streamlit](https://www.streamlit.io/) and sign in using your preferred method.

3. Click on "New App" in the Streamlit dashboard.

4. In the "GitHub URL" field, enter the URL of your cloned repository and click "Deploy". Wait for a few minutes for the app to be deployed.

5. Navigate to the app's settings in the Streamlit dashboard, then select "Secrets". Here, add your OpenAI `API_key` and `API_base` in the following format:

    ```
    API_key = "{your OpenAI API key}"
    API_base = "{your OpenAI API base}"
    ```

6. Reboot the app. Your own chatbot assistant is now ready to use!

## Usage

Type your question about the University of Southern Philippines Foundation (USPF) into the text box and click "Submit" to get a response.

## Contribution

Contributions are always welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[MIT](LICENSE.md)

## Disclaimer

The chatbot assistant may produce inaccurate information about people, places, or facts, especially if the question is outside the scope of topics it was trained on.
