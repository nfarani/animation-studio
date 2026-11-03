#!/bin/zsh
# usage: gen.sh <project dir> <output path inside it, no extension> <model> [higgsfield params...]
# Creates one Higgsfield job, waits, downloads the result, logs it to <project>/.jobs.tsv and the prompt to <project>/prompts/used_prompts.md.
# If submission returns an error, checks the account for a job created in the last 2 minutes before reporting failure (a 503 can still create a charged job).
P="$1"; out="$2"; model="$3"; shift 3
mkdir -p "$(dirname "$P/$out")" "$P/prompts"
{ echo "## $out"; echo "- model: $model"; prev=""; for a in "$@"; do if [ "$prev" = "--prompt" ]; then echo; echo "$a"; echo; elif [ -n "$prev" ] && [ "${prev#--}" != "$prev" ]; then echo "- ${prev#--}: $a"; fi; prev="$a"; done; echo; } >> "$P/prompts/used_prompts.md"
parse='import sys,json
try:
    d=json.load(sys.stdin); d=d[0] if isinstance(d,list) else d; print(d.get(sys.argv[1]) or "")
except Exception: print("")'
json=$(higgsfield generate create "$model" "$@" --wait --wait-timeout 25m --json 2>&1)
url=$(printf '%s' "$json" | python3 -c "$parse" result_url); id=$(printf '%s' "$json" | python3 -c "$parse" id)
if [ -z "$url" ]; then
  echo "submit error for $out: $(printf '%s' "$json" | tail -2 | tr '\n' ' ' | cut -c1-200)"
  if printf '%s' "$json" | grep -q "rate_limit\|not_enough_credits\|Too many positional\|Invalid\|Missing"; then echo "FAIL $out (not created)"; exit 1; fi
  sleep 20
  # only accept a job that is not already logged in this project (avoids grabbing a sibling job)
  id=$(higgsfield generate list --size 6 2>/dev/null | awk 'NR>1 && $0 ~ /in_progress|completed/ {print $1}' | while read j; do grep -q "$j" "$P/.jobs.tsv" 2>/dev/null || { echo $j; break; }; done)
  [ -z "$id" ] && { echo "FAIL $out"; exit 1; }
  higgsfield generate wait "$id" --timeout 25m --quiet >/dev/null 2>&1
  url=$(higgsfield generate get "$id" --json 2>/dev/null | python3 -c "$parse" result_url)
  [ -z "$url" ] && { echo "FAIL $out [$id]"; exit 1; }
  echo "recovered $out from the account [$id] - CHECK it is the right job"
fi
ext="${url##*.}"; curl -sSL "$url" -o "$P/$out.$ext" && echo "OK $out.$ext [$id]"
printf '%s\t%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$out" "$model" "$id completed" >> "$P/.jobs.tsv"
