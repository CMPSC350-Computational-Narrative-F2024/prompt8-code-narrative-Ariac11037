# Copilot Code

# Team Collaboration Project
# This script simulates a team of developers working together on a project.
# Each function represents a different team member's contribution.

# Alice starts the project by setting up the initial structure
def setup_project():
    print("Project setup complete.")
    return {"status": "initialized", "tasks": []}

# Bob adds a task management system
def add_task(project, task):
    project["tasks"].append(task)
    print(f"Task '{task}' added.")
    return project

# Carol implements a function to display the current status of the project
def display_status(project):
    print("Project Status:")
    print(f"Status: {project['status']}")
    print("Tasks:")
    for task in project["tasks"]:
        print(f"- {task}")

# Dave finalizes the project by marking it as complete
def finalize_project(project):
    project["status"] = "completed"
    print("Project finalized.")
    return project

# Main function to simulate the collaboration
def main():
    # Alice sets up the project
    project = setup_project()
    
    # Bob adds tasks to the project
    project = add_task(project, "Design the architecture")
    project = add_task(project, "Implement the core features")
    project = add_task(project, "Write unit tests")
    
    # Carol displays the current status
    display_status(project)
    
    # Dave finalizes the project
    project = finalize_project(project)
    
    # Carol displays the final status
    display_status(project)

# Run the main function to simulate the collaboration
if __name__ == "__main__":
    main()
