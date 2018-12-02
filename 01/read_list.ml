open Printf

let file = "data.txt"

let () =
     let ic = open_in file in
     let rec build_list infile =
          try
               let line = input_line infile in
               line :: build_list(infile)
          with End_of_file ->
               close_in infile;
               [] in
     let rec print_list = function
          [] -> ()
          | e::l -> print_string e ; print_string " " ; print_list l in
     print_list(build_list(ic))
