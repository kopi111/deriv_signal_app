#!/bin/bash
# Retry the 5m prefetch until Deriv's API recovers from the 520.
for attempt in $(seq 1 40); do
  echo "=== attempt $attempt $(date -Is) ==="
  if python3 prefetch_5m.py 2>&1 | tee /tmp/claude-1000/-home-kopi/61858c8b-15fc-45ed-8371-9bbf96240d4e/scratchpad/fetch5m_last.log | grep -q " bars"; then
    echo "=== 5m data arrived ==="
    exit 0
  fi
  sleep 180
done
echo "=== gave up after 40 attempts ==="
exit 1
