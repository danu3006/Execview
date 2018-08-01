# Execview Coding Challenge

This application processes the attached CSV file (chicago-bulls.csv), then loads the file, and create a report in JSON which will contain the following:

* Sorted players based on the PPG descending
* Calculates the average point for the team (based on the PPG)
* Finds the gold, silver and bronze player based on PPG
* Counts the number of players playing on each position
* Calculates the average height in cm.

Please see the example output below:

```
{
   "Players":[
      {
         "Id":"4",
         "Position":"SG",
         "Number":"23",
         "Country":"United States",
         "Name":"Jordan, Michael",
         "Height":"6 ft 6 in",
         "Weight":"215 lb",
         "University":"North Carolina",
         "PPG":32.6
      },
      { ... },
      { ... },
      { ... },
      { ... },
      { ... },
      { ... },
      { ... },
   ],
   "AveragePPG":8.44,
   "Leaders":[
      {
         "Gold":"Jordan, Michael",
         "PPG":32.6
      },
      {
         "Silver":"Pippen, Scottie",
         "PPG":18.6
      },
      {
         "Bronze":"Grant, Horace",
         "PPG":13.2
      }
   ],
   "Count":{
      "PG":3,
      "C":2,
      "PF":4,
      "SG":3,
      "SF":2
   },
   "AverageHeight":"200.7 cm"
}
```

## Deployment
To run this script simply invoke the python command followed by the `run.py`.

```
python run.py
```

Please note that this script was written in Python 3.x and will not compile with any prior versions.
