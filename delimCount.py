#Script to count delimiters.

#Usage:
#python delimCount.py <file_name> "<delimiter_to_count>"

import sys
import collections
import os

def main():

    if(len(sys.argv)!=3):
        print('python delimCount.py <file_name> "<delimiter_to_count>"')
        sys.exit()

    #command line args
    #sys.argv[0] = name of the script
    passed_file=sys.argv[1]
    search_delim=sys.argv[2]

    if not os.path.isfile(passed_file):
        print("File doesn't exist. Exiting...")
        sys.exit()

    #create dictionary
    delim_counts = {}

    # dict: { num_count: [ (line_num, line), ... ], ... }
    # map the # of occurrences of a delimiter to tuples specifying every line which has that count.

    #internal structure of delim_counts:
    #0: [ ( 0, "this line has no delimiters" ), ( 1, "neither does this one" ), ( 5, "this line (line 5) doesn't have any delimiters either" ) ],
    #3: [ ( 2, "line / with / three / delimiters" ), ( 4, "another / line / with / three delimiters" ) ],
    #2: [ ( 3, "one with / only / two instances" ) ]

    #go through every line
    #enumerate- gives an index in addition to the actual string representation of the given line
    #readlines()- returns a list of strings representing each line
    for line_num, line_text in enumerate( open(passed_file,'r').readlines() ):
        # occurrences of search_delim on this line
        delim_count = line_text.count( search_delim )

        #delim_counts[n] needs to return all lines which have n occurrences of the delimiter in them
        #create the first entry if delim_counts[delim_count] would error
        if delim_count not in delim_counts:
            delim_counts[ delim_count ] = [ ( line_num, line_text ) ]
        #otherwise there's already at least one line with delim_count occurences of the delimiter, so just add this line to that list
        else:
            delim_counts[ delim_count ].append( ( line_num, line_text ) )

    #special case for if the input is empty:
    #line_text.count(search_delim) will return 0 if there are no occurences
    if len( delim_counts ) == 0:
        print( "Empty file; no occurences of `" + search_delim + "`" )
        return

    #*******************************************************************#
    # case for if all lines of the file contain the same # of delimiters:
    #if there's only one entry, then all the lines have the same number of delimiters-because all lines were added to that single entry in the delim_counts dictionary
    if len( delim_counts ) == 1:
        print( "All the lines have the same number of delimiters:", list( delim_counts.keys() )[0] )
        return

    #sort the dictionary's keys(all the different delimiter counts) in descending order, for the print statements
    sorted_delim_counts = sorted( delim_counts, reverse=True )

    print( "Lines with different delimitation and the count:" )
    for delim_count in sorted_delim_counts:
        #go through every delimiter count and print all the lines which have that delimiter count on a single line
        print( "line(s)", ", ".join( [ str(c[0]) for c in delim_counts[ delim_count ] ] ) + ":", delim_count, "occurrences of `" + search_delim + "`" )
    print()
    #sorted_delim_counts[0] is the collections of all lines with the greatest delimiter count
    print( "Max Delimiter Count:", sorted_delim_counts[ 0], "in line(s)", ", ".join( [ str(c[0]) for c in delim_counts[ sorted_delim_counts[ 0] ] ] ) )
    #sorted_delim_counts[-1] is the collection of lines with the least delimitation count
    print( "Min Delimiter Count:", sorted_delim_counts[-1], "in line(s)", ", ".join( [ str(c[0]) for c in delim_counts[ sorted_delim_counts[-1] ] ] ) )

if __name__=='__main__':
    main()
