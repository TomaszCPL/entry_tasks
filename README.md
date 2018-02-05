# Entry tasks to Clearcode.

## Hack Power:
This program was expected to return power of given hack meeting following criteria:
- Each hack may use only specific letters: “a”, “b” and “c”. Hacks containing other
letters are ineffective.  :heavy_check_mark:
- Each letter adds specific power to the hack.  :heavy_check_mark:
- Each repeated letter in a hack brings more power than its previous iteration. First
instance of a letter in a hack is worth base power (for “b” it is 2), second instance of
the letter is worth 2 times its base power, third instance of a letter is worth 3 times its
base power, etc.  :heavy_check_mark:
- In addition to the power from letters, hacks can also contain special phrases. Those
phrases add specific values to the hack power.  :heavy_check_mark:
- Each hack uses the maximal power from letters and phrases. Letters always
contribute to the hack power (even if they are part of a phrase) but power of phrases
is exclusive (if phrases overlap — only the non-overlapping phrases generate power).  :heavy_check_mark:

My program is divided into two main parts. In the first one I focus on letters, counting them and calculating their power in one for loop. There is also validation of letters. Special phrases were a little more tricky so I've decided to use regex in order to find them in given hack.

## Page Report:
This program was expected to take all the urls from given file, process them and rewrite to a new file meeting following criteria:
- Script should count requests for each url  :heavy_check_mark:
- It should ignore the protocol, ending slash and query string parameters  :heavy_check_mark:
- The log file path should be read from the command line argument and the generated report written to the standard output.  :heavy_check_mark:
- The records in the result should be sorted by the number of requests in descending order.  :heavy_check_mark:
- If two URLs are requested equally often, they should be sorted lexicographically.  :heavy_multiplication_x:

The way my program works is to loop over every line in the input file with a specific "regex" function which finds the url(if exists). Then it adds the result (as a key) to the special dictionary which stores all requests with their numbers.    
