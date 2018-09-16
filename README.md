# twitter-analysis
This set of code contains all of the work done at the Call For Code Hackathon at Rensselaer Polytechnic Institute in Troy, NY.

For the `retriever` program, there are several environment variables that must be set.
- `API_KEY_TWITTER_CONSUMER`: Twitter API Consumer Key
- `API_SECRET_TWITTER_CONSUMER`: Twitter API Consumer Secret
- `API_KEY_TWITTER_ACCESS_TOKEN`: Twitter API Access Token Key
- `API_SECRET_TWITTER_ACCESS_TOKEN`: Twitter API Access Token Secret
- `URL_REDIS`: Redis (Complete) URI

One of the following environment variables must be set:
- `KEYWORD_FILTER`: Keyword to filter tweets by
- `LOCATIONS_FILTER`: An array of geolocation data (lat,long) to filter tweets by
