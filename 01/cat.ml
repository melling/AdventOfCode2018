#!/usr/bin/env ocaml


let () =
  let ic = open_in "data.txt" in
  try
    while true do
      let line = input_line ic in
      print_endline line
    done
  with End_of_file ->
    close_in ic
