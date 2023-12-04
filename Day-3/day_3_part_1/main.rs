use std::io::{BufRead, BufReader};
use std::fs::File;

pub fn main() {

    let debug = false;

    let f = BufReader::new(File::open("Day3.txt").expect("open failed"));

    let mut schematic = Vec::<Vec<char>>::new();
    
    //SET LENGTH OF EACH LINE HERE
    let schematic_width = 140;
    let spacer: Vec<Vec<char>> = vec![vec![' '; schematic_width + 2]];

    //adding outer spacers
    schematic.extend(spacer.iter().cloned());
    for line in f.lines() {
        if debug { println!(); }
        let mut temp = Vec::<char>::new();
        temp.push(' ');
        for c in line.expect("lines failed").chars() {
            temp.push(c);
            if debug { print!("{} ", c); }
        }
        temp.push(' ');
        schematic.push(temp);
    }

    //adding outer spacers
    schematic.extend(spacer.iter().cloned());

    //testing print all output
    
    // Iterate through all elements
    for row in &mut schematic {
        for i in row.iter_mut() {
            if *i == '.' { *i = ' '; }
            if debug { print!("{} ", i); }
        }
        if debug { println!(); }
    }
    
      
    // Declare function variables
    let mut sum = 0;
    let mut temp = String::new();
    let mut has_symbol = false;

    //iterating through a line
    for x in 0..schematic.len()-1 {
        //iterating through each character
        for y in 0..schematic[x].len()-1 {
            if debug { print!("Character: '{}', ", schematic[x][y]); }

            if schematic[x][y].is_digit(10) {
                
                //super long drawn out checking surrounding values
                // Iterate through adjacent positions (assuming a 3x3 grid)
                for i in -1..=1 {
                    for j in -1..=1 {
                        let new_x = x as isize + i;
                        let new_y = y as isize + j;

                        // Declare c outside the match block
                        let c = schematic[new_x as usize][new_y as usize];

                        // Finding symbols
                        if c != ' ' && !c.is_digit(10) { has_symbol = true; }
                    }
                }

                temp.push(schematic[x][y]);
                if debug { println!("Digit: '{}', Temp: '{}'", schematic[x][y], temp); }
            } 
            else {
                if !temp.is_empty() {
                    // Handle the case when temp is not empty
                    if has_symbol {
                        if let Ok(parsed_value) = temp.parse::<i32>() {
                        sum += parsed_value;
                        }
                        else {
                            // Handle the case when parsing fails
                            println!("Failed to parse: '{}'", temp);
                        }
                    }
                    temp.clear();
                    has_symbol = false;
                }
                if debug { println!("Not a digit"); }
            }
        }
        if debug { println!(); }
    }    
    
    print!("Sum is {}",sum);
    
}