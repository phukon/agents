from agency_swarm.agents import Agent


class WebPtoPNGCEO(Agent):
    def __init__(self):
        super().__init__(
            name="WebPtoPNGCEO",
            description="This agent is responsible for managing user requests, delegating tasks to the Converter, and handling user communication in the WebPtoPNGConverter agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )
        
    def response_validator(self, message):
        return message
