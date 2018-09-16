# twitter-analysis
This set of code contains all of the work done at the Call For Code Hackathon at Rensselaer Polytechnic Institute in Troy, NY.

For the `retriever` program, there are several environment variables that must be set.
- `API\_KEY\_TWITTER\_CONSUMER`: Twitter API Consumer Key
- `API\_SECRET\_TWITTER\_CONSUMER`: Twitter API Consumer Secret
- `API\_KEY\_TWITTER\_ACCESS\_TOKEN`: Twitter API Access Token Key
- `API\_SECRET\_TWITTER\_ACCESS\_TOKEN`: Twitter API Access Token Secret
- `URL\_REDIS`: Redis (Complete) URI

One of the following environment variables must be set:
- `KEYWORD\_FILTER`: Keyword to filter tweets by
- `LOCATIONS\_FILTER`: An array of geolocation data (lat,long) to filter tweets by
