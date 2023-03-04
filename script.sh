#!/bin/bash

args=("$@")
num_of_args=${#args[@]}

if (( num_of_args == 0 )); then
  labels=("a" "b" "c")
  numbers=()

  while (( ${#numbers[@]} < 3 )); do
    read -p "Enter ${labels[${#numbers[@]}]}: " user_input
    if [[ $user_input =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
      numbers+=($user_input)
    else
      echo -e "\033[0;31mError. Expected a valid real number, got invalid instead\033[0m"
    fi
  done

  a=${numbers[0]}
  b=${numbers[1]}
  c=${numbers[2]}

elif (( num_of_args == 1 )); then
  if [[ -f $1 ]]; then
    first_line=$(head -n 1 $1)
    if [[ $first_line =~ ^-?[0-9]+(\.[0-9]+)?[[:space:]]+-?[0-9]+(\.[0-9]+)?[[:space:]]+-?[0-9]+(\.[0-9]+)?$ ]]; then
      a=$(echo $first_line | awk '{print $1}')
      b=$(echo $first_line | awk '{print $2}')
      c=$(echo $first_line | awk '{print $3}')
    else
      echo -e "\033[0;31mError. File contains invalid data\033[0m"
      exit 1
    fi
  else
    echo -e "\033[0;31mError. It looks like the argument passed is not a path to a file\033[0m"
    exit 1
  fi

else
  echo -e "\033[0;31mError. Invalid number of arguments\033[0m"
  exit 1
fi

if (( $(bc <<< "$a == 0") )); then
  echo -e "\033[0;31mError. Coefficient 'a' cannot be 0\033[0m"
  exit 1
fi

echo "Equation is: $a x^2 + $b x + $c = 0"

discriminant=$(bc <<< "$b^2 - 4*$a*$c")

if (( $(bc <<< "$discriminant < 0") )); then
  echo "There are 0 roots"
elif (( $(bc <<< "$discriminant == 0") )); then
  x=$(echo "scale=2; (-$b / (2*$a))" | bc)
  echo "There is 1 root"
  echo -e "\033[0;32mx = $x\033[0m"
else
  x1=$(echo "scale=2; (-$b + sqrt($discriminant)) / (2*$a)" | bc)
  x2=$(echo "scale=2; (-$b - sqrt($discriminant)) / (2*$a)" | bc)
  echo "There are 2 roots"
  echo -e "\033[0;32mx1 = $(printf "%.2f" $x1)\033[0m"
  echo -e "\033[0;32mx2 = $(printf "%.2f" $x2)\033[0m"
fi