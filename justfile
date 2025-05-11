conda-hook := 'eval "$(/home/eivind/Documents/skole/master/8sem/dat259/miniconda/conda/bin/conda shell.fish hook)";'
conda-activate := 'conda activate snail;'

# Compile grammar for python using ANTLR
[working-directory: 'grammar']
@grammar:
	java -jar ~/.local/lib/antlr-4.13.2-complete.jar -visitor -o ../src/snail/parser -Dlanguage=Python3 Snail.g4

# Compile grammar to java
[working-directory: 'grammar']
@grammar-java:
	#!/usr/bin/env bash
	export CLASSPATH=".:/home/eivind/.local/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
	java -jar ~/.local/lib/antlr-4.13.2-complete.jar -visitor -o target Snail.g4
	cd target
	javac *.java

# Show tokens in ANTLR TestRig
[working-directory: 'grammar/target']
@test-tokens FILE:
	#!/usr/bin/env bash
	export CLASSPATH=".:/home/eivind/.local/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
	java org.antlr.v4.gui.TestRig Snail program -tokens {{invocation_directory()}}/{{FILE}}

# Show ? in ANTLR TestRig
[working-directory: 'grammar/target']
@test-grammar FILE:
	#!/usr/bin/env bash
	export CLASSPATH=".:/home/eivind/.local/lib/antlr-4.13.2-complete.jar:$CLASSPATH"
	java org.antlr.v4.gui.TestRig Snail program -tree {{invocation_directory()}}/{{FILE}}

[working-directory: 'grammar/target']
@test FILE:
	#!/usr/bin/env bash
	cat < {{invocation_directory()}}/{{FILE}}

# Export Conda environment to file
env-export:
	fish -c '{{conda-hook}} {{conda-activate}} conda env export --no-builds > environment.yml'

# Update Conda environment from file
env-update:
	fish -c '{{conda-hook}} {{conda-activate}} conda env update --file environment.yml --prune'

# Import Conda environment to file, only if it does not exist.
env-import:
	fish -c '{{conda-hook}} conda env create --name 'snail' --file environment.yml'

# Print info for environment
env-info:
	fish -c '{{conda-hook}} {{conda-activate}} conda info --envs'

# To run:
# env PYTHONPATH=src python -m snail.driver samples/hello-world.snail

# natives:
# 	java -jar alloy.jar natives

# exec FILE:
# 	java -jar alloy.jar exec {{FILE}}
