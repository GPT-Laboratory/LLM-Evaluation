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


**Replication Package**


**Objective**

This repository provides the _replication package.xlsx_ for the study "**Large Language Models for Code Generation: The Practitioners’ Perspective.**" The study aims to explore how practitioners perceive and use large language models for code generation.  We collected survey data and performed:

_Descriptive Analysis_ for closed-ended survey questions (Q1 to Q13) and _Open Coding_ for open-ended survey responses (Q14 and Q15). 

The replication package is provided above under the name "Replication_Package.xlsx".


1️⃣ **Survey Data**

The dataset consists of responses collected from software development practitioners regarding their experience with large language models for code generation. The data includes:

Closed-ended questions (Q1-Q13): Responses related to experience, role, industry, programming languages, tool usability, and performance evaluation of different models.

Open-ended questions (Q14-Q15): Participants' insights on challenges and suggestions for improvements in code generation models.

📂 **Files:**

Survey_Data - Contains the raw survey responses.


2️⃣ **Descriptive Analysis**

We performed descriptive statistical analysis on the closed-ended questions (Q1 to Q13) to extract insights such as:

Distribution of participants' experience and industry.

Preferences for programming languages used in testing and development.

Feedback on tool usability and performance of different models.

📂 **Files:**

_Descriptive_Analysis_ - Contains summary statistics and key insights from Q1 to Q13.


3️⃣ **Open Coding**

For open-ended survey questions (Q14 and Q15), we applied thematic analysis and open coding to categorize qualitative responses into meaningful themes. This helped in identifying:

Common challenges faced by practitioners while using LLMs for code generation.

Suggestions for improving these models.

📂 **Files:**

_OpenCoding_ - Contains coded responses and thematic analysis. A document explaining the coding process and framework used.

🔍 How to Use This Package

Researchers can use the survey data for further analysis or comparative studies.

The descriptive analysis provides insights into practitioners' experiences with LLMs.

The open coding results offer qualitative insights into user challenges and recommendations.

📩 **Contact & Contributions**

For questions or contributions, feel free to open an issue or submit a pull request. This dataset and analysis are shared for academic and research purposes. You can also contact on this email: zeeshan.rasheed@tuni.fi

## 📜 Citation

Below, you can find the replication package dataset on Zenodo.

```bibtex
@dataset{rasheed_2025_14810003,
  author       = {Rasheed, Zeeshan},
  title        = {Large Language Models for Code Generation: The
                   Practitioners' Perspective},
  month        = feb,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.14810003},
  url          = {https://doi.org/10.5281/zenodo.14810003}
}

## 📜 You can find full paper for _citation_ below:

To cite our work **Large Language Models for Code Generation: The Practitioners’ Perspective** paper, please use the following BibTeX entry:

```bibtex
@article{rasheed2025large,
  title={Large Language Models for Code Generation: The Practitioners' Perspective},
  author={Rasheed, Zeeshan and Waseem, Muhammad and Kemell, Kai Kristian and Ahmad, Aakash and Sami, Malik Abdul and Rasku, Jussi and Systä, Kari and Abrahamsson, Pekka},
  journal={arXiv preprint},
  eprint={2501.16998},
  archivePrefix={arXiv},
  primaryClass={cs.SE},
  year={2025},
  url={https://arxiv.org/abs/2501.16998}
}



