# AI Chatbot for Fiverr Sellers

This project is an AI chatbot system designed for Fiverr sellers to generate professional, polished responses to client communications. It utilizes the GPT-Neo model for text generation and is built with Flask for the web interface.

## Features
- Takes input text and generates a professional response.
- Uses GPT-Neo for text generation.
- Built with Flask for a lightweight web interface.
- Responsive front-end design.

## Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)
- Shared hosting environment with SSH access

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai_chatbot.git
    cd ai_chatbot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python run.py
    ```

5. Access the application in your browser at `http://localhost:5000`.

## Deployment

To deploy the application on a shared hosting environment:
1. Make sure you have SSH access to your shared hosting account.
2. Follow the hosting provider's instructions to deploy a Flask application.
3. Ensure the virtual environment and dependencies are properly set up on the server.

## Usage

1. Open the application in your web browser.
2. Enter the text you want to generate a response for in the textarea.
3. Click the "Generate Response" button to see the AI-generated response.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.