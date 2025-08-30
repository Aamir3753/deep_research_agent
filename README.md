# DeepResearchAgent

## Setup and Running

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/DeepResearchAgent.git
    cd DeepResearchAgent
    ```
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Configure environment variables:**  
    Edit `.env` with your API keys and settings.

4. **Run the system:**
    ```bash
    python main.py
    ```

## Example Research Questions

- What are the latest advancements in reinforcement learning?
- How does transformer architecture improve NLP tasks?
- What are the ethical implications of autonomous agents?

## Agent Roles

## Agent Roles

- **Requirement Gathering Agent:** Collects and defines research requirements and objectives.
- **Planning Agent:** Designs research strategies and allocates tasks to other agents.
- **Search Agent:** Finds relevant information from academic sources and web articles.
- **Reporting Agent:** Compiles findings and insights into structured reports.

## System Workflow Demo

![Working Demo](assets/Agent_Demo.gif)

## Team Coordination

Agents communicate via a shared message queue.  
Each agent posts updates and requests to the queue, enabling asynchronous collaboration.  
The system orchestrator assigns tasks and monitors progress, ensuring efficient workflow and timely completion.