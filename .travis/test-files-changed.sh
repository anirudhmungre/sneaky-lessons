set -e

timetracker='TimeTracker.md'

# Grab all files that were changed
all_files_changed=$(git diff --name-only master)

# Grab all markdown files that were changed
markdown_files=$(git diff --diff-filter=d --name-only master -- '*.md' | sed "/$timetracker/d")

# Grab all css files that were changed
# gulp_files=$(git diff --diff-filter=d --name-only master -- '*.css')

# Grab all css files that were changed
javascript_files=$(git diff --diff-filter=d --name-only master -- '*.js')

# Grab all JavaScript files that were changed
python_files=$(git diff --diff-filter=d --name-only master -- '*.py') 

#####################################################################

printf "\n\n\e[52mFiles to Check for Testing:\e[0m\n\n\e[36;4m$all_files_changed \e[0m \n\n\n"

# Run Cspell on all files changed
if [ -z "$all_files_changed" ];
  then
    printf "No Files Changed therefore none to test\n\n"
    exit 0
else
    cspell -u $all_files_changed
    printf "\nNo Spelling Issues Found!!!\n\n"
    md-report
fi

# If there is markdown files that were changed, we will execute 
if [ -n "$markdown_files" ];
then
    printf "\n\e[52mFiles to Check for Markdown:\e[0m\n\n\e[32;4m$markdown_files\e[0m\n\n"
    remark $markdown_files --no-stdout -e .md -r .remarkrc.js --quiet --frail
    printf "\n\e[32mNo Markdwonn Issues Found!!! \e[0m\n"
fi

if [ -n "$javascript_files" ];
then
    printf "\n\n\e[52mFiles to Check for JavaScript:\e[0m\n\n\e[33;4m$javascript_files\e[0m\n\n"
    eslint -c .eslintrc.json $javascript_files
    printf "\n\e[33mNo JavaScript Issues Found!!! \e[0m\n\n"
fi

if [ -n "$python_files" ];
then
    printf "\n\n\e[54mFiles to Check for Python:\e[0m\n\n\e[34;4m$python_files\e[0m\n\n"
    pycodestyle --show-source $python_files
        printf "\n\e[34mNo Python Issues Found!!! \e[0m\n\n"
fi

# If there is css files that were changed, we will execute 
#if [ -n "$gulp_files" ];
#then
#    printf "\nFiles to Check for Gulp:\n$gulp_files\n"
#    gulp lint
#fi
