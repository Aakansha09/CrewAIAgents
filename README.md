# CrewAI Agents Project

This project uses the CrewAI framework to orchestrate role-playing, autonomous AI agents. The goal is to have these agents perform various tasks related to researching, writing, and testing for a company.

## Agents

The project defines four agents:

1. **Researcher**: This agent's role is to research the features of a company.
2. **Writer**: This agent's role is to write compelling and engaging blog posts about the features of a company.
3. **Tester**: This agent's role is to create a test plan for the admin features of a company.
4. **Automation Tester**: This agent's role is to automate testing for a company.

Each agent is an instance of the `Agent` class from the CrewAI framework and uses the `Ollama` language model from the Langchain Community.

## Tasks

Tasks are defined as instances of the `Task` class from the CrewAI framework. Each task has a description, an agent responsible for its execution, and an expected output.

## Execution

The agents and tasks are passed to an instance of the `Crew` class from the CrewAI framework. The `Crew` instance orchestrates the execution of the tasks by the agents.

## Setup

Before running the code, you need to set up a virtual environment and install the necessary packages.

### Creating a Virtual Environment

You can create a virtual environment using `venv` (built into Python 3) or `conda` (part of the Anaconda distribution). Here's how to do it with `venv`:

```bash
python3 -m venv env
```
### Installing Packages
After activating the virtual environment, you can install the necessary packages with pip:

```bash
Download Ollama 
ollama run openhermes
```
## Running the Code

To run the code, execute the `crewai_test.py` script. This will kickoff the execution of the tasks by the agents.

This will install the crewai and ollama packages, which are needed to run the code.

```bash
python crewai_test.py
```

## Output for Company - Linkedin -

### Agent - Writer
<img width="1195" alt="image" src="https://github.com/Aakansha09/CrewAIAgents/assets/32329514/92d7b6a3-fdcc-493d-8f6d-bea46ea3c179">

### Agent - Tester
<img width="1206" alt="image" src="https://github.com/Aakansha09/CrewAIAgents/assets/32329514/0630824d-d75d-4c18-b6b3-4f1881acc8a5">

