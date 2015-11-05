Random copy generator by Andrew Fuchs.

From an idea presented by Nick Parlante somewhere in the Google Python Class
(available at https://www.youtube.com/playlist?list=PLA7A9A70ABFF92B08).

Reads a text and then generate random prose in the style of that text.
Best to groom text before ingestion to remove headings, quotation marks, and
other things that frustrate the algorithm. Especially any [.!?] that don't
denote sentence ends.

A number of suitable pre-groomed .txt files are included.

Why? I've been writing random language generators since sometime in the 20th
century, and this approach gives nice results.
