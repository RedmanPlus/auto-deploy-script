import shutil
import subprocess

import git
import docker

def update():
	repo = git.Repo("/home/devseye/Python_Job_Website/.git")
	cur_branch = repo.active_branch
	if cur_branch != "main":
		repo.git.checkout("main")
	cur_branch = repo.active_branch
	origin = repo.remotes.origin

	origin.fetch()
	origin.pull("main")
	print("done")

	client = docker.from_env()

	containers = client.containers.list()

	for container in containers:
		if container.id == "16be314e5bf3dcc4bd1c4b742e778206d8612a66ad6ccd419b4531a97f73b262":
			continue

		print(container)
		print(container.id)
		container.kill()

	needed_path = "/home/devseye/Python_Job_Website/"

	result = subprocess.call("docker compose up --detach", shell=True, cwd=needed_path)
	print(result)