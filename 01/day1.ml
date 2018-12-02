#!/usr/bin/env ocaml

sum = 0

let () =
  let ic = open_in "data.txt" in
  try
    while true do
      let line = input_line ic in
      print_endline line
      sum += line
    done
  with End_of_file ->
    close_in ic
