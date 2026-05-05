#!/bin/bash
# Paperclip issue update helper - handles status and comment updates with proper JSON encoding

set -e

ISSUE_ID=""
STATUS=""
COMMENT=""

while [[ $# -gt 0 ]]; do
  case $1 in
    --issue-id)
      ISSUE_ID="$2"
      shift 2
      ;;
    --status)
      STATUS="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

# Read comment from stdin if provided
if [ -t 0 ]; then
  : # stdin is terminal, no comment
else
  COMMENT=$(cat)
fi

if [ -z "$ISSUE_ID" ]; then
  echo "Error: --issue-id required" >&2
  exit 1
fi

# Build JSON payload
PAYLOAD=$(jq -n \
  --arg status "$STATUS" \
  --arg comment "$COMMENT" \
  '{} | 
   if $status != "" then .status = $status else . end |
   if $comment != "" then .comment = $comment else . end')

# Make the API call
curl -f -X PATCH \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID" \
  -H "Content-Type: application/json" \
  "$PAPERCLIP_API_URL/api/issues/$ISSUE_ID" \
  -d "$PAYLOAD"
