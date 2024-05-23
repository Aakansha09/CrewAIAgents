
from crewai import Crew , Agent, Task, Process
from langchain_community.llms.ollama import Ollama

ollama_openhermes= Ollama(model = "openhermes")
Researcher = Agent(
    role = 'Researcher',
    goal = 'Research features of [Company Name]',
    backstory = 'You are an assistance for [Company Name]',
    verbose =  True,
    allow_delegation = False,
    llm = ollama_openhermes
)

Writer = Agent(
    role = 'Writer',
    goal = 'Write compiling and engaging pointers blogs about features of [Company Name]',
    backstory = 'You are AI writer for [Company Name] who specialize in writing',
    verbose =  True,
    allow_delegation = False,
    llm = ollama_openhermes
)

Tester = Agent(
    role = 'Tester',
    goal = 'Create test plan for the Admin features of [Company Name]',
    backstory = 'You are an AI tester for [Company Name] who specialize in testing',
    verbose =  True,
    allow_delegation = False,
    llm = ollama_openhermes
)

Automation_Tester = Agent(
    role = 'Tester',
    goal = 'Generate automation script in JS with mocha for all Public APIs of [Company Name]',
    backstory = 'You are an Automation tester for [Company Name] who specialize in writing JS scipts to automate feature testing',
    verbose =  True,
    allow_delegation = False,
    llm = ollama_openhermes
)

task1 = Task(
    description =  'Investigate the all information about [Company Name] from URL [Company URL] and create a Test plan with Test cases around the Admin features.', 
    agent = Tester,
    expected_output = 'A detailed Test Plan on [Company Name]'
)
task2 = Task(
    description =  'Write a compelling blog post about [Company Name]', 
    agent = Writer,
    expected_output = 'A compelling blog post about [Company Name]'
)

task3 = Task(
    description =  'Investigate the all information about [Company Name] and generate automation script in JS with mocha for all Public APIs of [Company Name]', 
    agent = Tester,
    expected_output = 'Test script in JS with mocha for all Public APIs of [Company Name]'
)

crew = Crew(
    agents = [Researcher, Writer, Tester, Automation_Tester],
    tasks = [task1, task2, task3],
    verbose = True,
    process = Process.sequential
    )

result = crew.kickoff()
