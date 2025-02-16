import sys
import warnings
import os
from datetime import datetime

from adaptive_research_innovation.crew import AdaptiveResearchInnovation

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    print("Loaded API Key:", os.getenv("OPENAI_API_KEY"))

    """
    Run the crew.
    """
    inputs = {
        'topic': input("Enter your research topic: "),
        'current_year': str(datetime.now().year)
    }
    
    try:
        AdaptiveResearchInnovation().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": input("Enter your research topic: ")
    }
    try:
        AdaptiveResearchInnovation().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AdaptiveResearchInnovation().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": input("Enter your research topic: ")
    }
    try:
        AdaptiveResearchInnovation().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
