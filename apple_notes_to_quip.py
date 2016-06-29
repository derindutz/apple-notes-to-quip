#!/usr/bin/python

import argparse
import quip
from subprocess import Popen, PIPE

UPLOAD_FOLDER_NAME = "Uploaded Apple Notes"

def upload_notes(access_token, folder_id, skip_duplicates):
    p = Popen(["osascript", "run_script_on_each_note.scpt", "create_document.py", access_token, folder_id, str(skip_duplicates)], stderr=PIPE)
    logged_lines = iter(p.stderr.readline, "")
    for logged_line in logged_lines:
        yield logged_line
    p.stderr.close()
    p.wait()

def main():
    parser = argparse.ArgumentParser(description="Create a Quip document")
    parser.add_argument("--access_token", required=True, help="Quip access token")
    parser.add_argument("--skip_duplicates", required=False, action="store_true", help="Skip notes with the same title")
    parser.set_defaults(skip_duplicates=False)
    args = parser.parse_args()

    access_token = args.access_token
    skip_duplicates = args.skip_duplicates

    client = quip.QuipClient(access_token=access_token)
    folder = client.new_folder(UPLOAD_FOLDER_NAME)
    folder_id = folder["folder"]["id"]

    print "Uploading Apple Notes to Quip..."
    for logged_line in upload_notes(access_token, folder_id, skip_duplicates):
        print logged_line.replace("<div>", "").replace("</div>", "").replace("\n", "")[0:60] + "..."

if __name__ == '__main__':
    main()