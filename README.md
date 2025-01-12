# Flask Application

A basic Flask application that prompts the user to enter a name and forwards to a new page displaying the submitted name.

## How to Run the Application

1. **Install Python 3**
    - Ensure Python 3 is installed on your machine. You can check by running the following command in the terminal:
      ```bash
      python3 --version
      ```
    - If Python 3 is not installed, [download it here](https://www.python.org/downloads/).

2. **Clone the repository**:
    ```bash
    git clone https://github.com/SaproFX/flask_project.git
    ```

3. **Navigate to the project directory**:
    In the terminal, input:
    ```bash
    cd flask_project
    ```

4. **Set up a virtual environment**:
    - Create a virtual environment to isolate the application’s dependencies:
      ```bash
      python3 -m venv venv
      ```
    - Activate it by running:
      ```bash
      source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
      ```
    - You should see `(venv)` appear before your terminal prompt, indicating that the virtual environment is active.

5. **Install dependencies**:
    - In the terminal, run:
      ```bash
      pip install -r requirements.txt
      ```
    - If you don't have a `requirements.txt` file, you can manually install Flask by running:
      ```bash
      pip install Flask
      ```

6. **Run the application**:
    - To start the Flask application, run:
      ```bash
      python app.py
      ```
    - The application will run on `http://127.0.0.1:5000/`. You should see the following output in your terminal:
      ```
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
      ```
    - Open your browser and visit `http://127.0.0.1:5000/` to see the application. Right-click on the link to open it in a new tab.

7. **Stop the application**:
    - To stop the Flask application, press `CTRL+C` in the terminal.

## Additional Information
