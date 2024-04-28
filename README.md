# pyWanted

## The idea behind the program

This program sends requests to the FBI Most Wanted API to consume it, get valuable information about suspects
and display it in a user-friendly way.

The base project aimed to show all the FBI offices (ordered alphabetically) and the number of suspects wanted by
each of them (in the case of suspects not related to any field office, that is shown as well as 'No office related').



## Other

### Ideas for further versions

[ ] Implement database management (SQL) or Python's Pandas to make easier consults (GROUP BY could help a lot here).

[ ] Filter suspects with known possible locations.

[ ] Filter suspects with active rewards.

[ ] Use Python's Matplotlib to display statistics.

[ ] Browse suspect information by name (and exporting it to a file).

[ ] Retrieve information about all the suspects relative to a certain field office.

[ ] Check the most-recently updated suspects information.



### Petitions:

Please, Mr. FBI, let me know (in the HTTP response):

- How many requests I can make per minute.
- How many pages I'd need to consult to get all suspects' info.
- How many suspects are there in the currently consulted page.

### Abandoned ideas:

- At first, recursion was used to deal with '429 Too Many Requests', repeating the check_ok_conn() function over
and over until '200 OK' was received or an Error happened. This was replaced with a 'retries system', although
further changes might be done in that bit of the program.


- The 'retries system' failed catastrophically, so it had to be replaced by a 'preventive lapse system', meaning
that after retrieving the information of one page, the program always waits a fixed lapse of time (~2 seconds)
before attempting to make the next request. If the response sent by the FBI contained the data about how many
requests can be made per minute or how much time one should wait until the next request, this could be done in
a much more elegant way. God bless ´Murica!

### Sources and useful info:

#### On the API: 
- [FBI Wanted API](https://api.fbi.gov/wanted/v1/list)
- [FBI webpage with examples of requests with Python](https://www.fbi.gov/wanted/api)

#### Some notes on HTTP:
- [About HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [CodeReview on "handling HTTP status codes"](https://codereview.stackexchange.com/questions/282754/python-handling-different-http-status-codes-using-the-requests-library)
- [StackOverflow on "getting around 429 Too Many Requests"](https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python) 
- [Exponential Backoff](https://en.wikipedia.org/wiki/Exponential_backoff)

#### Pythonic Shenanigans:
- [A progress bar in Python](https://www.youtube.com/watch?v=x1eaT88vJUA) 
- [Bar graphs with Matplotlib](https://www.youtube.com/watch?v=zwSJeIcRFuQ)
- [Fixing matplotlib graphs issues](https://www.youtube.com/watch?v=C8MT-A7Mvk4)

