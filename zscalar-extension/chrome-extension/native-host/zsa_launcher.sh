#!/bin/bash
# Native messaging host for ZSA Token Launcher Chrome extension.
# Chrome sends JSON messages prefixed with a 4-byte length header (little-endian).

# Read the 4-byte message length
read_message() {
  local length_bytes
  length_bytes=$(dd bs=4 count=1 2>/dev/null | od -An -tu4 | tr -d ' ')
  if [ -z "$length_bytes" ] || [ "$length_bytes" -eq 0 ]; then
    exit 0
  fi
  dd bs="$length_bytes" count=1 2>/dev/null
}

# Send a JSON response back to Chrome
send_response() {
  local msg="$1"
  local length=${#msg}
  printf "$(printf '\\x%02x' $((length & 0xFF)) $(((length >> 8) & 0xFF)) $(((length >> 16) & 0xFF)) $(((length >> 24) & 0xFF)))"
  printf "%s" "$msg"
}

# Read incoming message from Chrome
MESSAGE=$(read_message)

# Extract the zsa:// URL from the JSON payload
ZSA_URL=$(echo "$MESSAGE" | python3 -c "import sys,json; print(json.load(sys.stdin)['url'])" 2>/dev/null)

if [ -n "$ZSA_URL" ]; then
  EDGE_URL="file://mac/Home/Documents/open_zscalar.html?url=${ZSA_URL}"
  open -a "Microsoft Edge" --args "$EDGE_URL" 2>/dev/null
  send_response '{"status":"ok"}'
else
  send_response '{"status":"error","message":"no url found"}'
fi
