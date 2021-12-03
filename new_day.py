from os import listdir
import os
from pick import pick
from datetime import date
import sys
import subprocess

NO_LOOK = ['README.md', 'venv', 'LICENSE', '.gitignore', '.git', os.path.basename(__file__)]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def prompt_project():
    projects = [f for f in listdir(BASE_DIR) if f not in NO_LOOK]

    (option, index) = pick(projects, "Pick a project: ")
    return option

def make_dir(chosen_project):
    project_dir= BASE_DIR + '/' + chosen_project
    today = date.today().strftime('%Y-%m-%d')
    existing_kata_days = [f for f in listdir(project_dir)]
    if today in existing_kata_days:
        sys.exit("ERROR: You already have a kata for this project today. Exit 1")
    new_path = project_dir + '/' + today 
    os.mkdir(new_path)
    return new_path

def setup_venv(proj_dir):
    subprocess.call([sys.executable, "-m", "venv", proj_dir + "/venv"])

def open_vs_code(project_path):
    # TODO: we should open up the project in VS Code for the user, however, I believe the subprocess call is using a some sort of virtual shell so I believe that is why it is not opening.
    subprocess.call(["cd", project_path, "&&", "code", "-a", "."])

    print("The command to open this project in vscode has been entered into your clipboad. cmd+v and return...")
    import pyperclip as clip
    clip.copy(f"cd {project_path} && code -a .")

def main():
    todays_project = prompt_project()
    new_proj_path = make_dir(todays_project)
    setup_venv(new_proj_path)
    open_vs_code(new_proj_path)

if __name__ == "__main__":
    main()

