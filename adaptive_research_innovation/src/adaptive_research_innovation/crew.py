from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool

@CrewBase
class AdaptiveResearchInnovation():
	"""AdaptiveResearchInnovation crew"""

	@before_kickoff
	def before_kickoff_function(self, inputs):
		print(f"Preparing to run the project with inputs: {inputs}")
		return inputs

	@after_kickoff
	def after_kickoff_function(self, result):
		print(f"Project execution completed. Final result stored in output/report.md")
		return result
	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def research_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['research_agent'],
			verbose=True,
			tools=[SerperDevTool()]
		)

	@agent
	def analysis_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['analysis_agent'],
			verbose=True
		)
	
	@agent
	def innovation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['innovation_agent'],
			verbose=True
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['analysis_task'],
		)

	@task
	def innovation_task(self) -> Task:
		return Task(
			config=self.tasks_config['innovation_task'],
			output_file='output/report.md'
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the AdaptiveResearchInnovation crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
