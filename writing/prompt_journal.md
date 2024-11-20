## 1. Prompts Used

* Generate code that serves as a narrative covering one of three themes: collaboration, discovery, or conflict
* Generate some narrative code, covering one of three themes: collaboration, discovery, or conflict. Use the structure, comments, and design of the code to create the narrative.
* Few-shot prompt: using the previous code as an example, generate narrative code in the same format with a different topic

## 2. Prompting Strategy

My strategy for prompting was to first get the main goal down, being a code that serves as a narrative. Later, I also used the themes to guide the code and create the type of narrative I wanted.

## 3. Output Evaluation

For each generated code output, consider:
    - Narrative Structure: How does the organization reflect the theme? Is there a clear flow that resembles a narrative?
    - Commentary and Documentation: How do Copilot’s comments contribute to the narrative? Do they add meaning to the code?
    - Design Choices: Evaluate how Copilot's naming conventions, variable usage, and logic choices enhance or detract from the narrative.

### Copilot

GitHub Copilot

* Narrative Structure
The code breaks down the narrative into distinct parts to represent collaboration in a team.
Each function corresponds to a specific action taken by a specific team member and creates a
clear flow. The main function ties the parts together, showing the resulting collaborative
effort.

* Commentary and Documentation
Copilot’s comments provides context for each part of the code. The comments act as a narrator, guiding the reader through the collaborative process and explaining the role of each team member. This makes the code more relatable and easier to understand.

* Design Choices
Naming Conventions: The function names (e.g., setup_project, add_task, display_status, finalize_project) are descriptive and align with the narrative, making it clear what each part of the code represents.
Variable Usage: A single project dictionary tracks the status and tasks of the project, simplifies the code, and keeps it organized.
Logic Choices: The sequential calling of functions in the main function mirrors the chronological order of events in a collaborative project, enhancing the narrative flow. Each function updates the project dictionary, reflecting the progression of the project and maintaining a cohesive story.

### Other Single LLM

* Narrative Structure
The structure reflects the progression of the narrative, being about conflict. This progression reflects a classic narrative arc with rising action, a climax, and resolution. Each character's contribution in the narrative feels cohesive and focused on collaboration during adversity.

* Commentary and Documentation
Comments provide narrative context and drama between code blocks. They explain functionality, but they also emphasize emotional stakes and character actions within the narrative. They strike a clean balance between technical langauge and narrative storytelling elements.

* Design Choices
Naming Conventions: Variables like defenders and enemy_waves immediately establish their roles in the story. Warrior attributes like name and skill are simple yet descriptive, tying directly to their narrative function. The method fight_wave is action-oriented, reinforcing the theme of conflict.
Variable Usage: The rotation of defenders through a list elegantly simulates their teamwork. This reinforces the narrative of shared responsibility during conflict. Each wave and enemy is presented as a distinct entity, making the stakes of each encounter feel meaningful and escalating.
Logic Choices: The linear progression of the waves reflects the inevitability of conflict. Each wave builds suspense, and the logic keeps focus on the warriors' individual and collective responses. The resolution and reflection are tied to the warriors’ contributions, ensuring the story feels complete and focused on the theme of overcoming adversity through cooperation.

## 4. Reflection

How did your prompt iterations impacted the narrative quality of the generated code? How did Copilot's suggestions supported or hindered the story within the code?

The prompt iterations made the code in Copilot more individualized rather than collaborative. However, the prompt iterations in ChatGPT made the code more collaborative, and it also tried to include all three themes for the code. I believe Copilot's suggestions hindered the story by keeping it focused on one person rather than a team. It did not help the narrative expand the story through the structure and design of the code.
