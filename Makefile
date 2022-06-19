#! /bin/bash
export PYTHONPATH := $(PYTHONPATH):app/
export IP := $(ipconfig getifaddr en0)
export DB_URL := "sqlite:///data/app.db"

# Clean project, including database and other temporary files.
clean:
	if [ -f "data/app.db" ] ;\
	then \
		rm -r data/app.db ;\
	fi;

# Initial project setup
setup_proj:
	if [ ! -d "environ" ] ;\
	then \
		python3 -m venv environ ;\
		source environ/bin/activate ;\
	fi;
	pip install -r requirements.txt

# args:
#	- CONFIG: [TEST/DEBUG]
run:
	( \
	source environ/bin/activate; \
	python3 app/main.py; \
	)

# Called on app startup. So it's not neccessary to call
test_gen:
	( \
	source environ/bin/activate; \
	python3 app/services/launch_command.py; \
	)
