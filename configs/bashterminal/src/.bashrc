# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# if you want to use some bin program, adds the path and
# 'uncomment' the following line:
# export PATH="$HOME/path/to/bin:$PATH"

# this will toggle on the colors when ls command
alias ls='ls --color=auto'

# better escape namming
RESET_ESCAPE="\e[0m"
RED_ESCAPE="\e[1;31m"
GREEN_ESCAPE="\e[1;32m"
YELLOW_ESCAPE="\e[1;33m"
BLUE_ESCAPE="\e[1;34m"
WHITE_ESCAPE="\e[1;37m"

# function to get current time
get_time() {
  # get date by format + echo it
  local local_time
  local_time=$(date +"%H:%M")
  echo -e "${WHITE_ESCAPE}[${GREEN_ESCAPE}$local_time${WHITE_ESCAPE}]"
}

# function to get current directory
get_current_directory() {

  local cur_dir
  # get full path dir
  cur_dir=$(pwd)

  # if it's home, replace by '~'
  if [ "$cur_dir" == "$HOME" ]; then
    cur_dir="~"

  # else, split each dir name and get the last one
  else
    cur_dir=$(echo $(pwd) | rev | cut -d'/' -f 1 | rev)
  fi

  # print
  echo -e "${WHITE_ESCAPE}dir:$cur_dir"
}

#functions to get git branch
get_git_branch() {
  # get branch
  local branch
  branch=$(git branch 2> /dev/null | grep '*' | sed 's/* //')

  # if no branch returned, replace value with '?'
  if [ -z "${branch}" ]; then
    branch="?"
  fi

  # echo it
  echo -e "${WHITE_ESCAPE}[${BLUE_ESCAPE}git:$branch${WHITE_ESCAPE}]"
}

# exporting the prompt
export PS1="\$(get_time) \$(get_current_directory) \$(get_git_branch)\$ $RESET_ESCAPE"
