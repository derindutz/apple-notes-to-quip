#!/usr/bin/python

import argparse
import quip

def main():
    parser = argparse.ArgumentParser(description="Create a Quip document")
    parser.add_argument("--access_token", required=True, help="Quip access token")
    parser.add_argument("--body", required=True, help="Document body")
    parser.add_argument("--folder_id", required=True, help="Destination folder id")
    args = parser.parse_args()

    client = quip.QuipClient(access_token=args.access_token)
    client.new_document(args.body, member_ids=[args.folder_id])

if __name__ == "__main__":
    main()