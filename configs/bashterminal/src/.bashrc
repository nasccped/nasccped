# .bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# if you want to use some bin program, adds the path and
# 'uncomment' the following line:
# export PATH="$HOME/path/to/bin:$PATH"

# this will toggle on the colors when ls command
alias ls='ls --color=auto'

# some cool color to use in our terminal:
# color naming as COLOR (first char + last char) + 'EP' (from `E`sca`P`e)
RTEP="\e[0m"    # RESET ESCAPE
GNEP="\e[1;32m" # GREEEN ESCAPE
YWEP="\e[1;33m" # YELLOW ESCAPE
BEEP="\e[1;34m" # BLUE ESCAPE
WEEP="\e[1;37m" # WHITE ESCAPE

# function to get the git branch (git required)
get_git_branch() {

  # creatting a local var
  local branch

  # putting our branch name into by 
  branch=$(git branch 2> /dev/null | grep '*' | sed 's/* //')

  # if branch is something, call it with no break line
  if [ -n "$branch" ]; then
    echo -e " ${PBLUE} $branch${WEEP}"
  fi
}

# export the marker to use in the shell
export PS1="$WEEP[$GNEP\u$WEEP|$YWEP\h$WEEP  \W\$(get_git_branch)]\$ $RTEP"
