from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class Converter(Agent):
    def __init__(self):
        super().__init__(
            name="Converter",
            description="This agent is responsible for converting .webp files to .png using JavaScript/TypeScript libraries in the WebPtoPNGConverter agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
