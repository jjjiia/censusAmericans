# censusAmericans
Automatically posting short bios of Americans from the census to twitter.

Data:
  - American Community Survey's Public Use Microdata Sample (PUMS) dataset
  - Got it from http://www.census.gov/acs/www/data_documentation/public_use_microdata_sample/

Code:
  - Based on everywordbot code from Allison Parrish NYU - her projects: http://www.decontextualize.com/

Running:
  - posts one line from a file every 4 hours, keeps a index file to track which line.
  - running on server with screen.
  - run with twitter credentials from slack - for tests use test credentials

TODO:
  - make notification email for when script fails
