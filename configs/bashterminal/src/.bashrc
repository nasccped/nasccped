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
GREEN_ESCAPE="\e[1;32m"
YELLOW_ESCAPE="\e[1;33m"
WHITE_ESCAPE="\e[1;37m"
ORANGE_ESCAPE="\e[1;38;5;202m"

# function to get current time
get_hostname() {
  local local_hostname
  local_hostname=$(hostname)
  echo -e "${GREEN_ESCAPE}$local_hostname${WHITE_ESCAPE}"
}

# function to get username
get_username() {
  local local_username
  local_username=$(whoami)
  echo -e "${YELLOW_ESCAPE}$local_username${WHITE_ESCAPE}"
}

# function to get current directory
get_current_directory() {
  local cur_dir
  cur_dir=$(pwd)
  if [ "$cur_dir" == "$HOME" ]; then
    cur_dir="~"
  else
    cur_dir=$(echo $(pwd) | rev | cut -d'/' -f 1 | rev)
  fi
  echo -e "${WHITE_ESCAPE} $cur_dir"
}

#functions to get git branch
get_git_branch() {
  local branch
  branch=$(git branch 2> /dev/null | grep '*' | sed 's/* //')
  if [ ! -z "${branch}" ]; then
    echo -e " ${ORANGE_ESCAPE} $branch${WHITE_ESCAPE}"
  fi
}

# exporting the prompt
export PS1="$WHITE_ESCAPE[\$(get_hostname).\$(get_username) \$(get_current_directory)\$(get_git_branch)]\$ $RESET_ESCAPE"
