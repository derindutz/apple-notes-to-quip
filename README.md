# Upload Apple Notes to Quip

A simple script that uploads [Apple (iCloud) Notes](https://www.icloud.com/notes) as [Quip](https://quip.com/) documents.

## Prerequisite
Python 2.x

## Use the script

1. Get your [Quip API access token](https://quip.com/api/personal-token)
2. If you don't have `argparse` installed, install it or run `pip install -r requirements.txt`
3. Run `./apple_notes_to_quip.py --access_token="YOUR_ACCESS_TOKEN"`
4. Your notes will now be available on Quip in a folder titled "Uploaded Apple Notes"

If, like me, your Apple Notes used to have syncing problems and you have duplicate notes, you can skip notes that have the same title when uploading to Quip. Instead of running the script above, run `./apple_notes_to_quip.py --access_token="YOUR_ACCESS_TOKEN" --skip_duplicates`
