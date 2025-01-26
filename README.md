**Project Objective**
This project aims to integrate 8 Large Language Models (LLMs) into a single, unified platform designed to generate and execute source code from natural language prompts. With the growing adoption of LLMs in software development, this platform provides developers and researchers with a practical tool to evaluate and compare LLMs based on their functionality, syntax accuracy, and real-world applicability. By consolidating practitioner feedback and empirical insights, the platform supports informed decision-making for the systematic selection and usage of LLMs in software development projects.

**Features**
Multi-Model Integration: Seamlessly integrates 8 LLMs into one platform for comparative analysis.
Customizable Configuration: Utilizes the OpenRouter API, which can be configured using the .env file.
Evaluation and Feedback: Conducted a survey with 60 software practitioners from diverse backgrounds to assess the strengths, weaknesses, and usability of each model.
Empirical Insights: Supports research and development by addressing gaps in benchmarks and metrics for LLM-generated code.

**Setup Instructions**
1. Clone the Repository
git clone <repository_url>
cd <repository_directory>

2. Install Dependencies
Use the provided requirements.txt file to install the necessary Python libraries:

pip install -r requirements.txt

3. Configure the Environment Variables
Replace the placeholder keys in the .env file with your OpenRouter API keys:

OPENROUTER_API_KEY=<your_api_key>

4. Run the Platform
Once the dependencies are installed and the API key is configured, start the platform:

python main.py

Requirements
Ensure you have the following installed:

Python 3.8 or higher
Libraries listed in requirements.txt
